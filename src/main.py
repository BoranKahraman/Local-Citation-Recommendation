import os
import PyPDF2
import re

# Define the citation patterns
citation_patterns = {
    'APA': r'\(\w+,\s\d{4}\)',
    'APA-Page': r'\(\w+(\s\w+)+,\s\d{4},\s?p\.\s\d+\)',
    'MLA': r'\(\w+\s\d+\)',
    'MLA-Page': r'\(\w+\s\d+,\s?p\.\s\d+\)',
    'Chicago Author-Year': r'\(\w+\s\d{4}\)',
    'Chicago Author-Year-Page': r'\(\w+(\s\w+)+\s\d{4},\s\d+\)',
    'IEEE Numeric': r'\[\d+\]',
    'IEEE-Text': r'\[\d+,\s"[\w\s]+"[,.]?\]',
    'Harvard Author-Year': r'\(\w+\s\d{4}\)',
    'Harvard-Text': r'\(\w+\s\d{4},\s"[\w\s]+"[,.]?\)',
    'Vancouver Numeric': r'\[\d+\]',
    'AMA': r'\[\d+\]',
    'ACS': r'\[\d+\]',
    'CSE': r'\[\d+\]',
    'Bluebook': r'\(\w+\s\d+\)',
    'ASA': r'\(\w+\s\d+\)',
    'AIP': r'\[\d+\]',
    'ISO 690 Numeric': r'\[\d+\]',
    'GSA Style': r'\(\w+\s\d{4}\)',
    'Turabian Style': r'\(\w+\s\d{4}\)',
    'Legal Bluebook': r'\(\w+\s\d+\)',
    'Vancouver Superscript': r'\[\d+\]',
    'Bluebook Law Review': r'\(\w+\s\d+\)',
    'APA Parenthetical': r'\(\w+,\s\d{4}\)',
    'ASA Parenthetical': r'\(\w+\s\d+\)',
    'CMS Author-Date': r'\(\w+\s\d{4}\)',
    'Custom': r'\w+(\sve\s\w+)?\s\(\d{4}:\s\d+-\d+\)',
    'Legal Citations with Statutes': r'\(\w+\s\d+\)',
    'Legal Citations with Court Cases': r'\(\w+\s\d+\)',
    'ISO 690-2 Numeric': r'\[\d+\]',
    'ISO 690-2 Author-Date': r'\(\w+\s\d{4}\)',
    'APA Parenthetical': r'\(\w+,\s\d{4}\)',
    'ASA Parenthetical': r'\(\w+\s\d+\)',
    'CMS Author-Date': r'\(\w+\s\d{4}\)',
    'Legal Citations with Statutes': r'\(\w+\s\d+\)',
    'Legal Citations with Court Cases': r'\(\w+\s\d+\)',
    'ISO 690-2 Numeric': r'\[\d+\]',
    'ISO 690-2 Author-Date': r'\(\w+\s\d{4}\)',
}

# Combine the regex patterns into a list
regex_patterns = list(citation_patterns.values())

class Pdf2Text(object):

    def __int__(self):
        pass

    def pdf2txt(self, pdf_path):
        text = ""

        # Open the PDF file in read-binary mode
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Iterate through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        return text

    def pdfs2txt(self, directory_path):
        # Initialize an empty list to store the text from each PDF
        text_list = []

        # Iterate through the files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                # Construct the full path to the PDF file
                pdf_file_path = os.path.join(directory_path, filename)

                # Open the PDF file in read-binary mode
                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)

                    # Initialize text for the current PDF
                    pdf_text = ""

                    # Iterate through each page in the PDF
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        pdf_text += page.extract_text()

                    # Append the extracted text to the list
                    text_list.append(pdf_text)

        return text_list


class CitationExtractor(object):

    def __int__(self):
        pass

    def extractCitationSingleDocument(self, text, style):

        pairs = {
            'APA': [],
            'APA-Page': [],
            'MLA': [],
            'MLA-Page':[],
            'Chicago Author-Year':[],
            'Chicago Author-Year-Page': [],
            'IEEE Numeric': [],
            'IEEE-Text': [],
            'Harvard Author-Year': [],
            'Harvard-Text': [],
            'Vancouver Numeric': [],
            'AMA': [],
            'ACS': [],
            'CSE': [],
            'Bluebook': [],
            'ASA': [],
            'AIP': [],
            'ISO 690 Numeric': [],
            'GSA Style': [],
            'Turabian Style': [],
            'Legal Bluebook': [],
            'Vancouver Superscript': [],
            'Bluebook Law Review': [],
            'APA Parenthetical': [],
            'ASA Parenthetical': [],
            'CMS Author-Date': [],
            'Custom': [],
            'Legal Citations with Statutes':[],
            'Legal Citations with Court Cases': [],
            'ISO 690-2 Numeric': [],
            'ISO 690-2 Author-Date': [],
            'APA Parenthetical': [],
            'ASA Parenthetical': [],
            'CMS Author-Date': [],
            'Legal Citations with Statutes': [],
            'Legal Citations with Court Cases': [],
            'ISO 690-2 Numeric':[],
            'ISO 690-2 Author-Date': [],
        }

        sentences = re.split(r'(?<=[.!?])\s+', text)

        if style == "all":
            for sentence in sentences:
                for pattern_name, pattern in citation_patterns.items():
                    matches = re.findall(pattern, sentence)
                    if matches:
                        pairs[pattern_name].append(sentence)

            return pairs

        for sentence in sentences:
                matches = re.findall(citation_patterns[style], sentence)
                if matches:
                    pairs[style].append(sentence)

        return pairs





