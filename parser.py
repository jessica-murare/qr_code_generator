import csv

def extract_iccids(file_path):
    """
    Extracts ICCIDs from a file.
    The file can be a CPD file (semicolon-separated) or a CSV file (comma-separated).
    It auto-detects the delimiter and the header row.
    """
    iccids = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_row_idx = -1
    for i, line in enumerate(lines):
        if "ICCID" in line:
            header_row_idx = i
            break

    if header_row_idx == -1:
        return []  # No ICCID header found

    header_line = lines[header_row_idx]
    delimiter = ';' if ';' in header_line else ','

    reader = csv.reader(lines[header_row_idx:], delimiter=delimiter)
    header = next(reader)
    
    try:
        iccid_idx = header.index("ICCID")
    except ValueError:
        return [] # ICCID not in header

    for row in reader:
        if not row:
            continue

        if len(row) > iccid_idx:
            iccid = "".join(filter(str.isdigit, row[iccid_idx]))
            if iccid:
                iccids.append(iccid)
                
    return iccids