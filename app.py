from flask import Flask, render_template, request, jsonify
from campus import shortest_path, campus

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/locations")
def locations():
    return jsonify(list(campus.keys()))


@app.route("/route")
def route():
    start = request.args.get("start")
    end = request.args.get("end")

    if start not in campus or end not in campus:
        return jsonify({"error": "Location not found"})

    path, distance = shortest_path(start, end)

    return jsonify({
        "path": path,
        "distance": distance
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)