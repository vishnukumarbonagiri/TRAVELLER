from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text):

    file_name = "TRAVELLER_itinerary.pdf"

    doc = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        story.append(
            Paragraph(line, styles["Normal"])
        )

        story.append(
            Spacer(1, 12)
        )

    doc.build(story)

    return file_name