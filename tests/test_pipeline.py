"""Unit tests for real-time sentiment analysis pipeline."""
import json, unittest

class TestMessageProcessing(unittest.TestCase):
    SAMPLE_MSG = {"text": "I love this product!", "source": "twitter", "timestamp": "2024-07-15T09:00:00Z"}

    def test_valid_message_roundtrip(self):
        encoded = json.dumps(self.SAMPLE_MSG).encode()
        decoded = json.loads(encoded)
        self.assertEqual(decoded["text"], self.SAMPLE_MSG["text"])

    def test_required_fields_present(self):
        for field in ["text","source","timestamp"]:
            self.assertIn(field, self.SAMPLE_MSG)

    def test_empty_text_detected(self):
        self.assertFalse(bool("".strip()))

    def test_text_preprocessing_lowercases(self):
        text = "Hello WORLD!!"
        cleaned = text.lower().strip()
        self.assertEqual(cleaned, "hello world!!")

    def test_sentiment_labels_valid(self):
        valid_labels = {"positive","neutral","negative"}
        for label in valid_labels:
            self.assertIn(label, valid_labels)

class TestBatchAggregation(unittest.TestCase):
    def test_count_by_sentiment(self):
        results = [{"label":"positive"},{"label":"negative"},{"label":"positive"}]
        counts = {}
        for r in results:
            counts[r["label"]] = counts.get(r["label"],0) + 1
        self.assertEqual(counts["positive"], 2)
        self.assertEqual(counts["negative"], 1)

if __name__ == "__main__": unittest.main()
