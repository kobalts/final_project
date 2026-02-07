import requests

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
    emotions=response.json()["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)
        
    return emotions




