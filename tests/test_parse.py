import unittest

from autoquest import QuestAPI

RAW = {
    "id": "1234567890123456789",
    "config": {
        "messages": {"quest_name": "Test Game"},
        "expires_at": "2099-01-01T00:00:00.000Z",
        "application": {"id": "42", "name": "Test Game"},
        "assets": {"hero": "1234567890123456789"},
        "rewards_config": {
            "rewards": [{"messages": {"name": "50 Orbs"}, "orb_quantity": 50}],
            "platforms": [0],
        },
        "task_config_v2": {"tasks": {"WATCH_VIDEO": {"target": 900}}},
    },
    "user_status": {"progress": {"a": {"value": 450}}},
}


class TestParse(unittest.TestCase):
    def test_watch_video(self):
        q = QuestAPI._parse(RAW)
        self.assertEqual(q["name"], "Test Game")
        self.assertEqual(q["reward"], "50 Orbs")
        self.assertEqual(q["task_type"], "WATCH_VIDEO")
        self.assertEqual(q["max"], 900)
        self.assertEqual(q["cur"], 450)
        self.assertEqual(q["progress"], 50)
        self.assertFalse(q["expired"])

    def test_expired(self):
        raw = {**RAW, "config": {**RAW["config"], "expires_at": "2020-01-01T00:00:00.000Z"}}
        self.assertTrue(QuestAPI._parse(raw)["expired"])

    def test_completed(self):
        raw = {**RAW, "user_status": {"completed_at": "2026-01-01T00:00:00.000Z"}}
        self.assertEqual(QuestAPI._parse(raw)["progress"], 100)

    def test_no_id(self):
        self.assertIsNone(QuestAPI._parse({"id": ""}))


if __name__ == "__main__":
    unittest.main()
