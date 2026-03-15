from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])
    d = float(request.form["d"])

    prediction = model.predict([[a,b,c,d]])

    return render_template("index.html", result=prediction)

    import os
    
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port)
