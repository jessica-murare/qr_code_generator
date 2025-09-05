# QR Code Generator from CPD/CSV

This project provides a simple and efficient way to generate QR codes from ICCID data found in `.cpd` or `.csv` files. The generated QR codes are then compiled into a single, easy-to-use PDF file.

## Features

*   **File Support:** Supports both `.cpd` (semicolon-separated) and `.csv` (comma-separated) files.
*   **Automatic Delimiter Detection:** Automatically detects the delimiter used in the input file.
*   **QR Code Generation:** Generates QR codes for each ICCID found in the input file.
*   **PDF Compilation:** Compiles all generated QR codes into a single PDF document.
*   **Two Interfaces:**
    *   **Command-Line Interface (CLI):** A simple command-line script for quick generation.
    *   **Graphical User Interface (GUI):** An intuitive GUI for users who prefer a visual interface.
*   **Download Functionality:** The GUI allows you to download the generated PDF to your desired location.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

This project can be used in two ways: through the command-line interface (CLI) or the graphical user interface (GUI).

### Command-Line Interface (CLI)

To generate the QR codes from the command line, run the `main.py` script:

```bash
python main.py
```

This will read the `sample.CPD` file in the project directory and generate a `ICCID_QR_Codes.pdf` file.

### Graphical User Interface (GUI)

To use the GUI, run the `gui.py` script:

```bash
python gui.py
```

This will open a window with the following options:

1.  **Select File:** Click this button to choose a `.cpd` or `.csv` file from your computer.
2.  **Generate QR Codes:** After selecting a file, click this button to generate the QR codes. The PDF content will be created in memory.
3.  **Download PDF:** Once the PDF content is generated, this button will be enabled. Click it to open a "save as" dialog and choose where to save your PDF file.

## Screenshots

*(Add screenshots of the GUI here to showcase the application's interface.)*

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.