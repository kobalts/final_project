from flask import Flask, request, url_for,

app=Flask(__name__)

@app.route('/emotionDetector',  methods=['GET,''POST'])
    return



if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)