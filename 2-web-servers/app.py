from flask import Flask, request, make_response, jsonify
import json
from werkzeug.exceptions import HTTPException
from datetime import datetime

class AltusHTTPError(Exception):
  pass


app = Flask(__name__)

@app.get("/")
def hello():
  return "<h1>Hello, World!</h1>"

@app.get("/goodbye")
def goodbye():
  return "<h1>Goodbye, world!</h1>"

@app.post("/name")
def hello_name():
  return "Hello, name!"

@app.route("/other", methods=["GET", "POST"])
def hello_other():
  print(request.method)
  
  return "Hello, other!"

# Dynamic sections of a path
@app.get("/name/<name>/<timezone>")
def hello_named_person(name, timezone):
  return f"Hello, {name} - you are in {timezone}"


# Query parameter ?name=Person&location=Place
@app.get("/person")
def hello_and_location():
  name = request.args.get("name", "Unnamed")
  location = request.args.get("location", "Unknown")

  return f"Hi {name}, you are in {location}"


@app.get("/add")
def add():
  a = float(request.args.get("a", 0))
  b = float(request.args.get("b", 0))
  return f"{a + b}"

@app.get("/multiply/<a>/<b>")
def multiply(a,b):
  return jsonify({"result": float(a) * float(b), "valid": True})

@app.get("/divide")
def divide():
  a = request.args.get("a")  
  b = request.args.get("b")

  if not a or not b:
    return jsonify({"message": "Need valid values for a and b", "error": True}), 400

  try:
    return jsonify({"result": float(a) / float(b), "valid": True})
  except ZeroDivisionError:
    return  jsonify({"message": "Cannot divide by zero", "error": True}), 400
  except Exception as e:
    return  jsonify({"message": "There has been an error", "error": True}), 400


@app.route('/days_until')
def days_until():
    date_str = request.args.get('date', "")
    try:
        target_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return 'Invalid date format, use YYYY-MM-DD.', 400

    today = datetime.now().date()
    
    if target_date.date() < today:
        return 'The given date is in the past.', 400
    
    days_left = (target_date.date() - today).days
    try:
      raise AltusHTTPError("This is another error")
    except AltusHTTPError:
      return "This is in the custom error", 200
    return f"{days_left} days left."

@app.errorhandler(HTTPException)
def handle_exception(e):
  response = e.get_response()
  print(response, e.code)
  if e.code == 404:
    return jsonify({"message": "Resource not found", "error": True}), 404
  return jsonify({"message": "Something went wrong", "error": True}), 400

@app.errorhandler(Exception)
def handle_other_exceptions(e):
  print(e)
  return jsonify({"message": "Something went wrong", "error": True}), 400  

if __name__ == "__main__":
  app.run(debug=True)