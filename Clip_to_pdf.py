from fpdf import FPDF
import pyperclip

def clipboard_to_pdf(output_file):
    # Get text from clipboard
    clipboard_text = pyperclip.paste()

    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Add text to PDF
    pdf.multi_cell(0, 10, clipboard_text.encode('latin-1', 'replace').decode('latin-1'))

    # Output PDF
    pdf.output(output_file)

# Specify output file
output_file = "/home/jasvir/Documents/CliptoPDF/clipboard_content1.pdf"

# Create PDF from clipboard content
clipboard_to_pdf(output_file)

print(f"PDF created: {output_file}")
