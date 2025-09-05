import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import re
from reportlab.lib.utils import ImageReader
import io

def clean_iccid(value: str) -> str:
    """
    Clean ICCID string:
    - Strip spaces/newlines
    - Remove any non-digit characters (so QR only has numbers)
    """
    return re.sub(r'\D', '', value.strip())

def generate_iccid_qr_pdf(iccids, output_file=None):
    if output_file:
        c = canvas.Canvas(output_file, pagesize=A4)
    else:
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=A4)

    x, y = 50, 750  # starting position

    for iccid in iccids:
        # Clean ICCID
        clean_value = clean_iccid(iccid)

        # Create QR in memory
        qr_img = qrcode.make(clean_value)

        # Save PIL image to a byte stream
        img_buffer = io.BytesIO()
        qr_img.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Add QR + text to PDF from the byte stream
        c.drawImage(ImageReader(img_buffer), x, y, width=100, height=100)
        c.drawString(x, y - 30, f"ICCID: {clean_value}")

        # Move position to the next line
        y -= 150
        if y < 100:  # new page if full
            c.showPage()
            x, y = 50, 750

    c.save()

    if output_file:
        print(f"PDF created: {output_file}")
        return None
    else:
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()