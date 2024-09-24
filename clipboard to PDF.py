import pyperclip
from fpdf import FPDF


def clipboard_to_pdf(output_file):
    # Get text from clipboard
    text = pyperclip.paste()

    # Create instance of FPDF class
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add clipboard text to PDF
    pdf.multi_cell(0, 10, text)

    # Save the PDF to a file
    pdf.output(output_file)


if __name__ == "__main__":
    output_file = "/home/jasvir/Documents/CliptoPDF/Fanu.pdf"  # Specify your desired output file name
    clipboard_to_pdf(output_file)
    print(f"PDF created successfully: {output_file}")
