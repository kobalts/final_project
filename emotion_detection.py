from flask import Flask, request

import requests


app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detector(text_to_analyse):
    response = requests.post(
        url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        timeout=10,
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={
            "raw_document": {
                "text": text_to_analyse
            }
        
        }
        
    )
    return response.text

emotion_detector("I am very happy!")


if __name__ == '__main__':
    app.run(debug=True)