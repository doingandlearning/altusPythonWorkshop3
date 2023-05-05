from todo import app
import pytest

@pytest.fixture()
def client():
    return app.test_client()

def test_get_all_todos_works(client):
  response = client.get("/todos")
  # self.assertEqual(response.status_code, 200)
  assert response.status_code == 200

def test_create_new_todo_works_with_correct_header(client):
  response = client.post("/todos", 
                            json={"title": "This is a todo"}
                          )

  assert response.status_code == 201

  data = response.get_json()


  assert data['title'] ==  "This is a todo"
  assert data['completed'] == False
  assert data['id'] == 1
