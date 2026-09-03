from pypdf import PdfReader

PDF_PATH = "documents/agentic_ai_sample.pdf"

reader = PdfReader(PDF_PATH)

print("PDF loaded successfully!")
print("Number of pages:", len(reader.pages))

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

print("\n--- Extracted Text ---\n")
print(text)
