import sys
from docx2pdf import convert

def convert_docx_to_pdf(input_path, output_path):
    try:
        convert(input_path, output_path)
        print(f"Conversion successful. PDF saved to {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_docx_to_pdf.py input.docx output.pdf")
        sys.exit(1)

    input_docx = sys.argv[1]
    output_pdf = sys.argv[2]

    convert_docx_to_pdf(input_docx, output_pdf)
