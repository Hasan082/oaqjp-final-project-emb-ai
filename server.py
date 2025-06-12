"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=['GET'])
def emotion_detection():
    """
    Handle emotion detection for the given text input.
    Returns formatted result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if not result or "dominant_emotion" not in result or result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result

if __name__ == '__main__':
    app.run(port=9001)
