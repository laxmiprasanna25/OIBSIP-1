import unittest

from bmi_calculator import calculate_bmi, get_bmi_category


class TestBMICalculator(unittest.TestCase):
    def test_calculates_bmi(self):
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)

    def test_rejects_zero_or_negative_weight(self):
        for weight in (0, -5):
            with self.subTest(weight=weight):
                with self.assertRaises(ValueError):
                    calculate_bmi(weight, 1.70)

    def test_rejects_zero_or_negative_height(self):
        for height in (0, -1.70):
            with self.subTest(height=height):
                with self.assertRaises(ValueError):
                    calculate_bmi(70, height)

    def test_bmi_categories(self):
        self.assertEqual(get_bmi_category(18.4), "Underweight")
        self.assertEqual(get_bmi_category(18.5), "Normal")
        self.assertEqual(get_bmi_category(24.9), "Normal")
        self.assertEqual(get_bmi_category(25.0), "Overweight")
        self.assertEqual(get_bmi_category(29.9), "Overweight")
        self.assertEqual(get_bmi_category(30.0), "Obese")


if __name__ == "__main__":
    unittest.main()
