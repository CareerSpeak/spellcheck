from flask import Flask, jsonify, request

from pdf_parser import PdfParser
from using_language_tool import GrammarChecker
import subprocess

app = Flask(__name__)


@app.route('/', methods=['POST'])
def check():
    args = request.args
    text = PdfParser('/resume/'+args.get('file') or '').parse()
    matches = GrammarChecker().check(text)
    grammar = [{'ruleID': match.ruleId,
                'message': match.message,
                'replacements': match.replacements,
                'offset': match.offset,
                'errorLength': match.errorLength,
                'sentence': match.sentence}
               for match in matches]
    
    terminal = (subprocess.check_output(matches, shell=True, encoding='utf-8')).strip()
    # terminal = matches.stdout(encoding='utf-8')
    print(terminal)

    return jsonify(
        {
            'grammar': f'{grammar}',
            'text': f'{text}',
            'terminal': f'{terminal}'
        })


@app.route('/', methods=['GET'])
def hello():
    return '<h2>Grammar</h2>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
