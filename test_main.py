import unittest

from dop import get_keyboard
from main import test


class dopTest(unittest.TestCase):
    keyboard = [
        ["ФИО"],
        ["Почта ВШЭ"],
        ["Почта МИЭМ"],
        ["Номер в группе"],
        ["Ссылка vk.com"],
        ["Ссылка instagram.com"]
    ]

    def test_keyboard(self):
        self.assertNotEqual(get_keyboard(),self.keyboard)

    def test_surname(self):
        self.assertEqual(test('Павлова'), 10)

    def test_name(self):
        self.assertEqual(test('11'),'Пашина Ксения Игоревна')


if __name__ == "__main__":
    unittest.main()
