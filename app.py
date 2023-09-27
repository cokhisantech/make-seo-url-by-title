from flask import Flask, render_template, request
import re
from unidecode import unidecode
import threading
import pyperclip

app = Flask(__name__)

def convert_to_seo_url(title):
    cleaned_title = unidecode(title)
    cleaned_title = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_title)
    seo_url = '-'.join(cleaned_title.split()).lower()
    return seo_url

@app.route('/', methods=['GET', 'POST'])
def index():
    seo_url = None
    copied = False
    if request.method == 'POST':
        title = request.form['title']
        seo_url = convert_to_seo_url(title)
        pyperclip.copy(seo_url)
        copied = True
    elif 'reset' in request.args:
        pyperclip.copy('')
        
    return render_template('index.html', seo_url=seo_url, copied=copied)

if __name__ == '__main__':
    app.run()
