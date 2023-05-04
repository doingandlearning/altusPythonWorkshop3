from flask import Flask, request

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

if __name__ == "__main__":
  app.run(debug=True)