from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(country, prediction, risk):

    os.makedirs("reports", exist_ok=True)
    file_path = f"reports/{country}_report.pdf"

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(file_path)

    content = []

    content.append(Paragraph("Child Mortality Report", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Country: {country}", styles['Normal']))
    content.append(Paragraph(f"Predicted Value: {prediction}", styles['Normal']))
    content.append(Paragraph(f"Risk Level: {risk}", styles['Normal']))

    doc.build(content)

    return file_path

# from fpdf import FPDF

# def generate_pdf(country, prediction, risk):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(200, 10, 'Child Mortality Prediction Report', ln=True, align='C')

#     pdf.set_font('Arial', '', 12)
#     pdf.ln(10)
#     pdf.cell(200, 10, f'Country: {country}', ln=True)
#     pdf.cell(200, 10, f'Prediction: {prediction}', ln=True)
#     pdf.cell(200, 10, f'Risk Level: {risk}', ln=True)

#     file_path = 'prediction_report.pdf'
#     pdf.output(file_path)
#     return file_path