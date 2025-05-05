import json
import requests

def emotion_detector(text_to_analyze):
    """Emotion detection function"""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload, timeout=10)

    response_dict = json.loads(response.text)

    emotions = response_dict['emotionPredictions'][0]['emotion']
    emotion_scores = {
        'anger' : emotions['anger'],
        'disgust' : emotions['disgust'],
        'fear' : emotions['fear'],
        'joy' : emotions['joy'],
        'sadness' : emotions['sadness']
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores

    