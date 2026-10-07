from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for dominant JOY emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1, 'joy')

        # Test case for dominant ANGER emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2, 'anger')

        # Test case for dominant DISGUST emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3,'disgust')

        # Test case for dominant SAD emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4, 'sadness')

        # Test case for dominant FEAR emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5, 'fear')

if __name__ == '__main__':
    unittest.main()