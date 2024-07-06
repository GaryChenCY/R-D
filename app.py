from flask import Flask
from flask import request
from flask import render_template
import pdfplumber

with pdfplumber.open("220104003防癌1.pdf") as p: 
    for i in range(50): 
        page = p.pages[i] 
        textdata = page.extract_text() 
        print(textdata) 
        data = open("text.text", "a") 
        data.write(textdata)



app=Flask(__name__)

# 建立路徑/對應的處理函式
@app.route("/")
def index():
    return render_template("index.html")
    
app.run()



