import requests

def emotion_detector(text):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObject = { "raw_document": { "text": text } }
    response = requests.post(url, json=jsonObject, headers=headers)
    emotion_predicted = response.json()['emotionPredictions']
    emotion = {}
    dominant_emotion = 0
    for i in range(len(emotion_predicted)):
        emotion['anger'] = emotion_predicted[i]['emotion']['anger']
        emotion['disgust'] = emotion_predicted[i]['emotion']['disgust']
        emotion['fear'] = emotion_predicted[i]['emotion']['fear']
        emotion['joy'] = emotion_predicted[i]['emotion']['joy']
        emotion['sadness'] = emotion_predicted[i]['emotion']['sadness']
        dominant_emotion = max(dominant_emotion, emotion['anger'], emotion['disgust'], emotion['fear'], emotion['joy'], emotion['sadness'])

    emotion_key = ""
    for key, value in emotion.items():
        if(value == dominant_emotion):
            emotion_key = key

    emotion['dominant_emotion'] = emotion_key
    return emotion