from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for dominant JOY emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assert ()'dominant_emotion': joy') in result_1.text
        

if __name__ == '__main__':
    unittest.main()