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

    def test_no_errors_or_warnings(self):
        lines = [
            "[time] INFO: line1",
            "[time] INFO: line2"
        ]

        expected_error_count = 0
        expected_warning_count = 0
        expected_errors = []
        expected_warnings = []
        expected_error_frequency = {}
        expected_warning_frequency = {}

        result = analyse_log(lines)

        self.assertEqual(result[0], expected_error_count)
        self.assertEqual(result[1], expected_warning_count)
        self.assertEqual(result[2], expected_errors)
        self.assertEqual(result[3], expected_warnings)
        self.assertEqual(dict(result[4]), expected_error_frequency)
        self.assertEqual(dict(result[5]), expected_warning_frequency)

    def test_repeated_errors_and_warnings(self):
        lines = [
            "[time] ERROR: apples failed to grow",
            "[time] ERROR: apples failed to grow",
            "[time] WARNING: bananas are not ripe",
            "[time] WARNING: bananas are not ripe"
        ]

        expected_error_count = 2
        expected_warning_count = 2
        expected_errors = [
            "[time] ERROR: apples failed to grow",
            "[time] ERROR: apples failed to grow"
        ]
        expected_warnings = [
            "[time] WARNING: bananas are not ripe",
            "[time] WARNING: bananas are not ripe"
        ]
        expected_error_frequency = {
            "apples failed to grow": 2
        }
        expected_warning_frequency = {
            "bananas are not ripe": 2
        }

        result = analyse_log(lines)

        self.assertEqual(result[0], expected_error_count)
        self.assertEqual(result[1], expected_warning_count)
        self.assertEqual(result[2], expected_errors)
        self.assertEqual(result[3], expected_warnings)
        self.assertEqual(dict(result[4]), expected_error_frequency)
        self.assertEqual(dict(result[5]), expected_warning_frequency)