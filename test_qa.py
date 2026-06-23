from services.document_qa_service import DocumentQAService

qa = DocumentQAService()

answer = qa.ask(
    "sample.pdf",
    "What is this report about?"
)

print(answer)