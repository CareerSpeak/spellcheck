from flask import Flask, jsonify, request

from pdf_parser import PdfParser
from using_language_tool import GrammarChecker

app = Flask(__name__)


@app.route('/', methods=['POST'])
def check():
    args = request.argsN
    text = '/resume/'+PdfParser(args.get('file') or '').parse()
    grammar = GrammarChecker().check(text)
    return jsonify(
        {
            'grammar': f'{grammar}',
            'text': f'{text}'
        })


@app.route('/', methods=['GET'])
def hello():
    return '<h2>Grammar</h2>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
