import os
from parser import extract_iccids
from qr import generate_iccid_qr_pdf

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "sample.CPD")  # your CPD file
    iccids = extract_iccids(file_path)
    generate_iccid_qr_pdf(iccids)
