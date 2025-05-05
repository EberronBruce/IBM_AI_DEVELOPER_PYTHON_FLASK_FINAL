"""Flask server to use for analyzing emotions by inputed text"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """ Use to fext the html page for the index"""
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
        Used to call the endpoint to anazlye text and return the result
    """
    text = request.args.get("textToAnalyze")
    result, status_code = emotion_detector(text)

    if status_code == 400:
        return  "Invalid text! Please try again!"

    # Build the response string
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
        f"\n"
    )

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    