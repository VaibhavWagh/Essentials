import os
import re
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# Define a function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(resource_manager, string_io, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)
    
    with open(pdf_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file):
            interpreter.process_page(page)
    
    text = string_io.getvalue()
    device.close()
    string_io.close()
    
    return text

# Set the directory where your PDF files are located
pdf_dir = '/home/vaibhav/Documents/Python/PDF_Read/pdf'

# Set the path to the output text file
output_path = '/home/vaibhav/Documents/Python/PDF_Read/rs_IDS_all_caps.txt'

# Define a regular expression pattern to match words that start with "rs" or "Rs" followed by a number
pattern = r'\bRS\d+\w*\b'

# Loop over each PDF file in the directory
with open(output_path, 'w') as output_file:
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, filename)
            
            # Extract text from the PDF file
            pdf_text = extract_text_from_pdf(pdf_path)
            
            # Search for words that match the pattern
            words = re.findall(pattern, pdf_text,re.IGNORECASE)
            
            # Write the words to the output file
            for word in words:
                output_file.write(word + '\n')
