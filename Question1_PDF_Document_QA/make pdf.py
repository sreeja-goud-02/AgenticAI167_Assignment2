from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

os.makedirs("documents", exist_ok=True)

pdf_path = "documents/agentic_ai_sample.pdf"

styles = getSampleStyleSheet()

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4
)

story = []

story.append(
    Paragraph("Introduction to Agentic AI", styles["Title"])
)

story.append(Spacer(1, 20))

content = [
    (
        "What is Agentic AI?",
        "Agentic AI refers to artificial intelligence systems that can pursue goals "
        "by reasoning, planning actions, using tools, observing results, and adapting "
        "their next steps."
    ),
    (
        "Main Components of an AI Agent",
        "An AI agent generally contains an LLM as its reasoning engine, goals or "
        "instructions, tools, memory, and an execution process."
    ),
    (
        "Retrieval-Augmented Generation",
        "Retrieval-Augmented Generation, also called RAG, combines information retrieval "
        "with language generation. Documents are divided into smaller chunks and relevant "
        "chunks are retrieved when a user asks a question."
    ),
    (
        "Vector Search",
        "Vector search represents text as numerical vectors and finds content that is "
        "semantically similar to a user query."
    ),
    (
        "Agent Workflow",
        "A document question-answering agent loads a PDF, extracts its text, divides "
        "the text into chunks, retrieves relevant information, and sends the retrieved "
        "context to an LLM to generate an answer."
    ),
    (
        "Benefits of Agentic AI",
        "Agentic AI can automate multi-step tasks, use external tools, reason about "
        "problems, and complete tasks with less manual intervention."
    )
]

for heading, text in content:
    story.append(
        Paragraph(heading, styles["Heading2"])
    )
    story.append(
        Paragraph(text, styles["BodyText"])
    )
    story.append(Spacer(1, 10))

doc.build(story)

print("PDF created successfully!")
print("PDF location:", pdf_path)
print("PDF size:", os.path.getsize(pdf_path), "bytes")
