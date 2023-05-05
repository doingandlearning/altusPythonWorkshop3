from todo import app
import unittest
from pathlib import Path

class TestTodo(unittest.TestCase):
  def setUp(self) -> None:
    self.app = app.test_client()
    return super().setUp()

  def test_get_all_todos_works(self):
    response = self.app.get("/todos")
    self.assertEqual(response.status_code, 200)

  def test_create_new_todo_works_with_correct_header(self):
    response = self.app.post("/todos", 
                              json={"title": "This is a todo"}
                            )

    self.assertEqual(201, response.status_code)

    data = response.get_json()

    self.assertEqual(data['title'], "This is a todo")
    self.assertEqual(data['completed'], False)
    self.assertEqual(data['id'], 1)





if __name__ == "__main__":
  unittest.main()
