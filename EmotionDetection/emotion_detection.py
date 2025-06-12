import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using an external emotion detection service.
    Args:
        text_to_analyse (str): The text for which emotions need to be detected.
    Returns:
        dict: A dictionary containing the detected emotions or an error message.
    Raises:
        Exception: If the request to the emotion detection service fails.
    """
    # Define the URL and headers for the emotion detection service
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    try:
        # Send a POST request to the emotion detection service
        response = requests.post(URL, headers=headers, json=input_json)
    
        # Check if the response is successful
        # and return the JSON response or an error message.
        if response.status_code == 200:
            result = response.json()
            emotions = result['emotionPredictions'][0]['emotion']
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('sadness', 0)
            sadness_score = emotions.get('anger', 0)
            
            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            return {
                "error": "Failed to detect emotions",
                "status_code": response.status_code,
                "details": response.text
            }
    
    except Exception as e:
        return {
            "error": "An exception occurred during the API call",
            "details": str(e)
        }