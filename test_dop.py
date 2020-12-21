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
        ["Ссылка instagram.com"],
        ["Получить все данные"]
    ]

    def test_keyboard(self):
        self.assertEqual(get_keyboard(), self.keyboard)

    def test_not(self):
        self.assertNotEqual(get_keyboard(), "ФИО")

    def test_error(self):
        self.assertEqual(test('dfghj11'), 'error')


if __name__ == "__main__":
    unittest.main()



