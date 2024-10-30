

import pyttsx3
import PyPDF2

# Open the PDF file
file = open("book.pdf", "rb")

# Initialize the PDF reader
pdf_reader = PyPDF2.PdfReader(file)
pages = len(pdf_reader.pages)
print("Number of pages:", pages)

# Initialize the text-to-speech engine
melo = pyttsx3.init()

# Select the page you want to read (page numbers start from 0)
page = pdf_reader.pages[6]  # This reads the 7th page (index 6)
text = page.extract_text()

# Use the text-to-speech engine to say the text
melo.say(text)
melo.runAndWait()

# Close the file
file.close()

