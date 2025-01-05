"""
This module defines a Flask application for detecting emotions in text.
It provides a homepage and an endpoint for emotion detection.
"""

import json

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Create a Flask app instance
app = Flask(__name__)

@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text and return the detected emotions."""
    message = request.args.get("textToAnalyze")
    if not message:
        return "Invalid text! Please provide a valid input."

    result = emotion_detector(message)
    valid_emotions = {emotion: value for emotion, value in result.items() if value is not None}

    if not valid_emotions:
        return "No valid emotions detected. Please try again."

    detected_emotion = max(valid_emotions, key=valid_emotions.get)
    result_formatted = json.dumps(valid_emotions, indent=2)

    return (
        f"For the given statement, the system response is:\n{result_formatted}\n"
        f"The dominant emotion is: {detected_emotion}."
    )

if __name__ == "__main__":
    app.run(debug=True)
