from flask import Flask, jsonify, request

app = Flask(__name__)

class Todo:
  def __init__(self, description, id, completed=False):
    self.id = id
    self.description = description
    self.completed = completed

  def __str__(self):
    return f"[{self.id}] {self.description} {'finished' if self.completed else 'still to do'}"
  
  def to_dict(self):
    return {"description": self.description, "id": self.id, "completed": self.completed}

# Database ... some api 
todos = [Todo("Learn flask", 1)]

@app.get('/todos')
def get_all_todos():
  return jsonify([todo.to_dict() for todo in todos])

@app.post("/todos")
def create_new_todo():
  body = request.json
  id = len(todos) + 1 # Naive! 
  description = body.get("description")

  if not description:
    return jsonify({"message": "Whoops! You forgot to provide a description!", "error":True}), 400
  
  todo = Todo(description, id)
  todos.append(todo)
  return jsonify(todo.to_dict())

@app.get("/todos/<int:id>")
def get_single_todo(id):
  for todo in todos:
    if todo.id == id:
      return jsonify(todo.to_dict())
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404

@app.put("/todos/<int:id>")
def update_single_todo(id):
  for todo in todos:
    if todo.id == id:
      data = request.json
      todo.description = data.get("description", todo.description)
      todo.completed = data.get("completed", todo.completed)
      return jsonify(todo.to_dict())
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404

@app.delete("/todos/<int:id>")
def delete_single_id(id):
  for todo in todos:
    if todo.id == id:
      todos.remove(todo)  
      return "", 204
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404


if __name__ == "__main__":
  todo = Todo('Interesting thing', 1)
  print(todo.to_dict())