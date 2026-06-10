import io
import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import app

client = TestClient(app.app)

VALID_PDF_BYTES = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF\n"


def test_home_route_returns_200_and_index_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "OriginAI" in response.text


def test_analyzer_route_returns_200_and_contains_analyzer():
    response = client.get("/analyzer")
    assert response.status_code == 200
    assert "Analyzer" in response.text


def test_dashboard_route_returns_200_and_contains_dashboard():
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "Dashboard" in response.text


def test_investor_report_route_returns_200_and_contains_investor_report():
    response = client.get("/investor-report")
    assert response.status_code == 200
    assert "Investor Report" in response.text


def test_upload_endpoint_accepts_pdf_and_returns_analysis(monkeypatch, tmp_path):
    tmp_upload_dir = tmp_path / "uploads"
    tmp_upload_dir.mkdir()
    monkeypatch.setattr(app, "UPLOAD_DIR", str(tmp_upload_dir))
    monkeypatch.setattr(app, "SUPPORTED_EXTENSIONS", {".pdf"})

    def fake_run(file_path):
        assert os.path.exists(file_path)
        return {"summary": "test"}

    monkeypatch.setattr(app.workflow, "run", fake_run)

    file_content = io.BytesIO(VALID_PDF_BYTES)
    files = {"file": ("test.pdf", file_content, "application/pdf")}
    response = client.post("/upload", files=files)

    assert response.status_code == 200
    body = response.json()
    assert body["filename"] == "test.pdf"
    assert body["analysis"] == {"summary": "test"}
    assert "id" in body
    assert Path(tmp_upload_dir / body["stored_as"]).exists()
