import language_tool_python
import argparse

from pdf_parser import PdfParser


class GrammarChecker:
    def __init__(self, language: str = 'en-US') -> None:
        self.tool = language_tool_python.LanguageTool(
            language, config={'cacheSize': 1000, 'pipelineCaching': True})
        self.errors_by_section = {}
        self.section_headers = ['summary', 'objective',
                                'experience', 'skills', 'personal information']

    def check(self, text: str):
        output = []
        current_section = None

        # Iterate through the lines of text
        for line in text.split('\n'):
            # Check if the line matches any section header
            for header in self.section_headers:
                if header in line.lower():
                    current_section = header
                    break
            if current_section:
                # If we are in a section, check for grammar errors
                matches = self.tool.check(line)
                if matches:
                    if current_section not in self.errors_by_section:
                        self.errors_by_section[current_section] = []
                    self.errors_by_section[current_section].extend(matches)

        for _, errors in self.errors_by_section.items():
            for error in errors:
                output.append(error)
        return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    text = PdfParser(args.file).parse()

    matches = language_tool_python.LanguageTool('en-US').check(text)
    for match in matches:
        print(match)

    # grammar = GrammarChecker().check(text)
    # print(grammar)
