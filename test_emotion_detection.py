import unittest

from EmotionDetection import emotion_detector as ed

class TestEmotions(unittest.TestCase):

    def test1(self):
        test_cases=  [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for i in test_cases:
            self.assertEqual(
                ed(i[0])['dominant_emotion'],
                i[1]
            )
            

unittest.main()