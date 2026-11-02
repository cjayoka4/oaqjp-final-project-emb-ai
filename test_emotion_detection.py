from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for dominant JOY emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertIn('dominant_emotion : joy', result_1)
        
        # Test case for dominant ANGER emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertIn('dominant_emotion : anger', result_2)

        # Test case for dominant DISGUST emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertIn('dominant_emotion : disgust', result_3)

        # Test case for dominant SAD emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertIn('dominant_emotion : sadness', result_4)

        # Test case for dominant FEAR emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertIn('dominant_emotion : fear', result_5)

if __name__ == '__main__':
    unittest.main()