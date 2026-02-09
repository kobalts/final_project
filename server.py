from flask import Flask, request, render_template
from EmotionDetection import emotion_detector as ed

app=Flask(__name__)


@app.route("/",  methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/emotionDetector",  methods=["GET"])
def check_emotions():
    result=""
    text=request.args.get("textToAnalyze", "", type=str)
    full_response=ed(text)

    if full_response['dominant_emotion']==None:
        return "Invalid text! Please try again!"

    result = ", ".join(
        f"{key}: {val}"
        for key, val in full_response.items()
        if key != "dominant_emotion"
    )
   

    return (
        f"For the given statement, the system response is {result}. "
        f"The dominant emotion is {full_response['dominant_emotion']}."
    )


if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)