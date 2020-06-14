import unittest

from bot import content_text_answer, database


class FunctionalTest(unittest.TestCase):

    def test_add_todo_item(self):
        answer = content_text_answer('бот добавь дело №1')
        self.assertEqual('дело №1 добавлено', answer)
        self.assertEqual(1, len(database))

    def test_get_empty_list(self):
        answer = content_text_answer('бот покажи список')
        self.assertEqual('Ваш список пока пуст', answer)
