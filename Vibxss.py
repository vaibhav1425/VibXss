import re
from flask import Flask, request, render_template

app = Flask(__name__)

def sanitize_input(input_str):
    # Remove any HTML tags
    input_str = re.sub(r'<[^>]*>', '', input_str)
    
    # Escape special characters
    input_str = input_str.replace('&', '&amp;')
    input_str = input_str.replace('<', '&lt;')
    input_str = input_str.replace('>', '&gt;')
    input_str = input_str.replace('"', '&quot;')
    input_str = input_str.replace("'", '&#x27;')
    input_str = input_str.replace('/', '&#x2F;')
    
    return input_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')
    
    sanitized_input1 = sanitize_input(input1)
    sanitized_input2 = sanitize_input(input2)
    
    # Process the sanitized inputs
    # ...
    
    return render_template('result.html', input1=sanitized_input1, input2=sanitized_input2)

if __name__ == '__main__':
    app.run()
