from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
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

