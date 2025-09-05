import tkinter as tk
from tkinter import filedialog, messagebox
from parser import extract_iccids
from qr import generate_iccid_qr_pdf
import os

class QrCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.file_path = None
        self.pdf_content = None

        self.create_widgets()

    def create_widgets(self):
        # Frame for file selection
        file_frame = tk.Frame(self.root, padx=10, pady=10)
        file_frame.pack()

        self.select_button = tk.Button(file_frame, text="Select File", command=self.select_file)
        self.select_button.pack(side=tk.LEFT)

        self.file_label = tk.Label(file_frame, text="No file selected", width=50)
        self.file_label.pack(side=tk.LEFT, padx=10)

        # Frame for generation
        generate_frame = tk.Frame(self.root, padx=10, pady=10)
        generate_frame.pack()

        self.generate_button = tk.Button(generate_frame, text="Generate QR Codes", command=self.generate_qrs)
        self.generate_button.pack()

        # Frame for download
        download_frame = tk.Frame(self.root, padx=10, pady=10)
        download_frame.pack()

        self.download_button = tk.Button(download_frame, text="Download PDF", command=self.download_pdf, state=tk.DISABLED)
        self.download_button.pack()

        # Frame for status
        status_frame = tk.Frame(self.root, padx=10, pady=10)
        status_frame.pack()

        self.status_label = tk.Label(status_frame, text="")
        self.status_label.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("CPD files", "*.cpd"), ("All files", "*.*")]
        )
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))
            self.download_button.config(state=tk.DISABLED)
            self.pdf_content = None

    def generate_qrs(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return

        self.status_label.config(text="Extracting ICCIDs...")
        self.root.update_idletasks()

        try:
            iccids = extract_iccids(self.file_path)
            if not iccids:
                messagebox.showwarning("Warning", "No ICCIDs found in the selected file.")
                self.status_label.config(text="")
                return

            self.status_label.config(text="Generating PDF...")
            self.root.update_idletasks()

            self.pdf_content = generate_iccid_qr_pdf(iccids)

            self.status_label.config(text="PDF content generated.")
            self.download_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "PDF content has been generated. You can now download the file.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.status_label.config(text="Error occurred.")

    def download_pdf(self):
        if not self.pdf_content:
            messagebox.showerror("Error", "No PDF content to download.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=f"{os.path.splitext(os.path.basename(self.file_path))[0]}_QR_Codes.pdf"
        )

        if file_path:
            try:
                with open(file_path, "wb") as f:
                    f.write(self.pdf_content)
                messagebox.showinfo("Success", f"Successfully saved PDF to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save PDF: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QrCodeGeneratorApp(root)
    root.mainloop()
