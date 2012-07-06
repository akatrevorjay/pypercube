from datetime import datetime
import unittest

from pypercube import time_utils


class TestMetric(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2012, 7, 6, 20, 33, 16, 573225)

    def test_yesterday(self):
        self.assertEqual(time_utils.yesterday(self.now),
                datetime(2012, 7, 5, 20, 33, 16, 573225))

    def test_last_week(self):
        self.assertEqual(time_utils.last_week(self.now),
                datetime(2012, 6, 29, 20, 33, 16, 573225))

    def test_start_of_month(self):
        self.assertEqual(time_utils.start_of_month(self.now),
                datetime(2012, 7, 1))

    def test_floor(self):
        self.assertEqual(time_utils.floor(self.now, time_utils.STEP_10_SEC),
                datetime(2012, 7, 6, 20, 33, 10))
        self.assertEqual(time_utils.floor(self.now, time_utils.STEP_1_MIN),
                datetime(2012, 7, 6, 20, 33))
        self.assertEqual(time_utils.floor(self.now, time_utils.STEP_5_MIN),
                datetime(2012, 7, 6, 20, 30))
        self.assertEqual(time_utils.floor(self.now, time_utils.STEP_1_HOUR),
                datetime(2012, 7, 6, 20))
        self.assertEqual(time_utils.floor(self.now, time_utils.STEP_1_DAY),
                datetime(2012, 7, 6))
        self.assertRaisesRegexp(ValueError, "is not a valid resolution",
                time_utils.floor, self.now, 12345)
