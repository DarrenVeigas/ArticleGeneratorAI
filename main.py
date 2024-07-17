from flask import Flask, render_template, jsonify ,request
import google.generativeai as genai

import os

app = Flask(__name__)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        prompt=request.json.get('prompt')
        model=genai.GenerativeModel(model_name="gemini-1.5-flash")
        res = model.generate_content(["Generate an article on the topic "+prompt])
        str=res.text.replace("*","<br>")
        str=res.text.replace("##","")
        return str
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
