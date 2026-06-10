from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

PDF_BYTES = b"%PDF-1.1\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 72 128 Td (Test PDF page) Tj ET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000060 00000 n \n0000000111 00000 n \n0000000225 00000 n \n0000000315 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n389\n%%EOF"


def test_site_routes_available():
    for path in ['/', '/analyzer', '/dashboard', '/investor-report', '/pitchdeck']:
        response = client.get(path)
        assert response.status_code == 200


def test_upload_rejects_non_pdf():
    response = client.post('/upload', files={'file': ('test.txt', b'Not a pdf', 'text/plain')})
    assert response.status_code == 400
    assert 'Uploaded file must be a PDF' in response.text


def test_upload_rejects_bad_extension():
    response = client.post('/upload', files={'file': ('test.docx', PDF_BYTES, 'application/pdf')})
    assert response.status_code == 400


def test_analysis_history_endpoint():
    response = client.get('/api/analysis/history')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
