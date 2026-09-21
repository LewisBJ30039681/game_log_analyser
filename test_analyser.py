import unittest
from analyser import analyse_log

class TestAnalyseLog(unittest.TestCase):
    def test_analyse_log(self):
        lines = [
            "[time] ERROR: apples failed to grow",
            "[time] INFO: line2",
            "[time] WARNING: bananas are not ripe",
            "[time] WARNING: bananas are not ripe ah",
            "[time] ERROR: apples failed to grow ah",
            "[time] INFO: line5",
            "[time] ERROR:",
            "[time] WARNING:"
        ]

        expected_error_count = 3
        expected_warning_count = 3
        expected_errors = [
            "[time] ERROR: apples failed to grow",
            "[time] ERROR: apples failed to grow ah",
            "[time] ERROR:"
        ]
        expected_warnings = [
            "[time] WARNING: bananas are not ripe",
            "[time] WARNING: bananas are not ripe ah",
            "[time] WARNING:"
        ]
        expected_error_frequency = {
            "apples failed to grow": 1,
            "apples failed to grow ah": 1
        }
        expected_warning_frequency = {
            "bananas are not ripe": 1,
            "bananas are not ripe ah": 1
        }

        result = analyse_log(lines)

        self.assertEqual(result[0], expected_error_count)
        self.assertEqual(result[1], expected_warning_count)
        self.assertEqual(result[2], expected_errors)
        self.assertEqual(result[3], expected_warnings)
        self.assertEqual(dict(result[4]), expected_error_frequency)
        self.assertEqual(dict(result[5]), expected_warning_frequency)