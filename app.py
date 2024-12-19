from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_joke', methods=['GET'])
def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return jsonify({
            "setup": joke["setup"],
            "punchline": joke["punchline"]
        })
    return jsonify({"error": "Could not fetch a joke at the moment!"})

if __name__ == '__main__':
    app.run(debug=True)
