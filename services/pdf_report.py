import io
import textwrap
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def build_pdf_report(user_input, probability, category, shap_points, recommendations):

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 45

    # ---------- helper functions ----------
    def new_page():
        nonlocal y
        pdf.showPage()
        y = height - 45

    def write(text, size=11, pad=16):
        nonlocal y
        pdf.setFont("Helvetica", size)
        pdf.drawString(45, y, text)
        y -= pad
        if y < 70:
            new_page()

    def write_wrapped(lines, prefix="- "):
        for line in lines:
            for wrapped in textwrap.wrap(prefix + str(line), width=95):
                write(wrapped)

    def section(title):
        nonlocal y
        y -= 6
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(45, y, title)
        y -= 18

    pdf.setFont("Helvetica-Bold", 16) #title
    pdf.drawString(45, y, "Heart Disease Prediction Report")
    y -= 24
    write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", size=10, pad=20)

    section("1) User Input Details")
    write_wrapped([f"{k}: {v}" for k, v in user_input.items()])

    section("2) Prediction Result")
    write(f"- Predicted Risk Level: {probability * 100:.2f}%")
    write(f"- Risk Category: {category}")

    section("3) Model Explanation")
    write_wrapped(shap_points)

    section("4) Personalized Recommendations")
    write_wrapped(recommendations)

    pdf.save()
    buffer.seek(0)
    return buffer
