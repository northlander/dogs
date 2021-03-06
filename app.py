from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def dogs():
    return jsonify(["Bulldog", "Boxer", "Bolognese", "Terrier", "Border Collie"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=False,host='0.0.0.0',port=port)