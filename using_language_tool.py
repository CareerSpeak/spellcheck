import language_tool_python
import PyPDF2

# Open the PDF file
pdfFileObj = open('resume.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

tool = language_tool_python.LanguageTool('en-US')
errors_by_section = {}

# Define section headers
section_headers = ['summary', 'objective',
                   'experience', 'skills', 'personal information']

# Iterate through all pages
for page_num in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[page_num]
    pdfText = pageObj.extract_text()

    # Initialize the current section as None
    current_section = None

    # Iterate through the lines of text
    for line in pdfText.split('\n'):
        # Check if the line matches any section header
        for header in section_headers:
            if header in line.lower():
                current_section = header
                break
        if current_section:
            # If we are in a section, check for grammar errors
            matches = tool.check(line)
            if matches:
                if current_section not in errors_by_section:
                    errors_by_section[current_section] = []
                errors_by_section[current_section].extend(matches)

# Close the PDF file
pdfFileObj.close()


for section, errors in errors_by_section.items():
    print(f'{section}:\n')
    for error in errors:
        print(f'{error}\n')
