import unittest
from EmotionDetection import emotion_detector
class TestEmotionDetection(unittest.TestCase):

    

    def test1(self):
        statements = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
    ]
        for statement, expected_emotion in statements:
            result = emotion_detector(statement)
            detected_emotion = max(result, key=result.get)
            message = f"Statement: '{statement}' | Expected: {expected_emotion} | Detected: {detected_emotion}"
            self.assertEqual(expected_emotion, detected_emotion, message) 


unittest.main()
