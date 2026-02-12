import pdfplumber
import os
from pathlib import Path
from PIL import Image
import io

# PDF file path
pdf_path = r".\EXHIB PANELS_reduced.pdf"

# Output folder
output_folder = r".\extracted_images"

# Create output folder if it doesn't exist
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Extract images from PDF
try:
    print(f"Extracting images from PDF: {pdf_path}")
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}")
        
        image_count = 0
        
        # Iterate through each page
        for page_num, page in enumerate(pdf.pages, start=1):
            # Render page to image
            try:
                im = page.to_image()
                image_path = os.path.join(output_folder, f"page_{page_num:03d}.png")
                im.save(image_path)
                image_count += 1
                print(f"Extracted page {page_num} -> {image_path}")
            except Exception as page_error:
                print(f"Error extracting page {page_num}: {page_error}")
    
    print(f"\nTotal pages extracted: {image_count}")
    print(f"Images saved to: {output_folder}")

except FileNotFoundError:
    print(f"Error: PDF file not found at {pdf_path}")
except Exception as e:
    print(f"Error: {e}")
