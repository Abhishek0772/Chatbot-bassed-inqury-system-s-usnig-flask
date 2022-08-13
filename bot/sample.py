from flask import Flask,render_template,request
import json
import random

app = Flask(__name__) 

with open("data.json") as f:
    a = json.load(f)

def chat(value):
     chatResponse = " Sorry not found"
     for i in a["chatbot"]:
          if value in i["questions"]:
               chatResponse = random.choice(i["responses"])
     return chatResponse
               


@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():

     ans = "not found"
     userText = request.args.get("msg") 

     ans = chat(userText)

               #get data from input,we write js  to index.html
     return str(ans)


if __name__ == "__main__":
     app.run(debug = True, host='0.0.0.0')


