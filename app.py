from flask import Flask, render_template, jsonify

app = Flask(__name__)

open_positions = [
  {
    "id": 1,
    "title": "Fashion Designer",
    "location": "Nairobi, Kenya",
    "salary": "$25000"
  },
  {
    "id": 1,
    "title": "Pattern Maker",
    "location": "Nairobi, Kenya",
    "salary": "$20000"
  },
  {
    "id": 1,
    "title": "Sample Maker",
    "location": "Nairobi, Kenya",
    "salary": "$18000"
  },
  {
    "id": 1,
    "title": "Sketch Illustrator",
    "location": "Nairobi, Kenya",
    "salary": "$15000"
  }
]

@app.route("/")
def home():
  return render_template("index.html", jobs=open_positions)

@app.route("/api/open-positions")
def list_open_positions():
  return jsonify(open_positions)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)