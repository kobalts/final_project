from flask import Flask, request, render_template
from EmotionDetection import emotion_detector as ed

app=Flask(__name__)


@app.route("/",  methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/emotionDetector",  methods=["GET"])
def check_emotions():
    text=request.args.get("textToAnalyze", "", type=str)
    #text = request.form.get("textToAnalyze", "")
    
    if text is None:
        result="no text provided to analyze"
        return result
    else:
        result=ed(text)
        return result


if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)