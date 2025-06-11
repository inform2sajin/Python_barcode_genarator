import barcode
from barcode.writer import ImageWriter
from PIL import Image

#Input from user
user_data = input("Enter the data to encode in the barcode: ")

#Generate barcode and save as PNG file
code = barcode.get('code128',user_data, writer=ImageWriter())
filename = code.save(f"{user_data}_barcode") #Saves as user_data_barcode

#Convert the PNG to PDF
image = Image.open(filename)
pdf_filename = f"{user_data}_barcode.pdf"
image.convert('RGB').save(pdf_filename)

# Saved file name
print(f"Barcode saved as PNG: {filename}")
print(f"Barcode saved as PDF: {pdf_filename}")


