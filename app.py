from pathlib import Path
import os
import uuid
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Request, UploadFile, File, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import config
from workflow_manager import WorkflowManager
from history_store import add_entry, latest_entry, all_entries

load_dotenv()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/analyzer", response_class=HTMLResponse)
async def analyzer(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="analyzer.html"
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
Path(UPLOAD_DIR).mkdir(exist_ok=True)
MAX_BYTES = int(os.getenv("MAX_UPLOAD_SIZE_MB", config.MAX_UPLOAD_SIZE_MB)) * 1024 * 1024
SUPPORTED_EXTENSIONS = config.ALLOWED_EXTENSIONS

workflow = WorkflowManager()


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename or not file.content_type or "pdf" not in file.content_type.lower():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Uploaded file must be a PDF")

    total = 0
    ext = os.path.splitext(file.filename)[1].lower() or ".pdf"
    if ext not in SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Uploaded file must have a .pdf extension")

    safe_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, safe_name)

    try:
        with open(file_path, "wb") as buffer:
            while True:
                chunk = await file.read(1024 * 64)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BYTES:
                    buffer.close()
                    os.remove(file_path)
                    raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                                        detail="File too large (max 10MB)")
                buffer.write(chunk)

        results = workflow.run(file_path)
        entry = {
            "id": uuid.uuid4().hex,
            "filename": file.filename,
            "stored_as": safe_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "analysis": results
        }
        add_entry(entry)

        return JSONResponse({
            "filename": file.filename,
            "stored_as": safe_name,
            "analysis": results,
            "id": entry["id"]
        })

    except HTTPException:
        raise
    except Exception:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to process uploaded PDF")


@app.get("/api/analysis/latest")
async def get_latest_analysis():
    latest = latest_entry()
    if not latest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No analysis found")
    return latest


@app.get("/api/analysis/history")
async def get_analysis_history():
    return all_entries()


@app.get("/investor-report", response_class=HTMLResponse)
async def investor_report(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="investor-report.html"
    )


@app.get("/pitchdeck", response_class=HTMLResponse)
async def pitchdeck(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pitchdeck.html"
    )