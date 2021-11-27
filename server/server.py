from flask import Flask, render_template, send_from_directory, jsonify
from botty import setup, reply as rep
from markdown import markdown as md

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template("wapp.html")

@app.route('/tailwind.css')
def tailwind():
    return send_from_directory('.','tailwind.css')

@app.route('/inp/<name>')
def reply(name):
    msg = rep(name)
    img = None
    print(msg)
    if type(msg)==tuple:
        msg, img = msg[0], msg[1]
    return jsonify({"message": md(msg), "image": img})

def main():
    setup("botty")
    app.run() 

if __name__=="__main__":
    main()   
