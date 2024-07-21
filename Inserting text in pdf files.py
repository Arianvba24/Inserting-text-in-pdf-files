from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def write_file(file,text, output_name):
    
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 40)
    can.drawString(10, 100, text)

    can.save()

    packet.seek(0)

    new_pdf = PdfReader(packet)

    existing_pdf = PdfReader(open(file, "rb"))
    output = PdfWriter()

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    output_stream = open(fr"C:\Users\Cash\Documents\pruebas_python\proyectos\pdf/{output_name}.pdf", "wb")
    output.write(output_stream)
    output_stream.close()

if __name__=="__main__":
    write_file(r"C:\Users\Cash\Documents\pruebas_python\proyectos\pdf\invoice.pdf", "DELETE FILE", 1)