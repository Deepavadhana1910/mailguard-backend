from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def analyze_text(subject, complaint):
    suspicious_words = ["bank", "password", "lottery", "prize", "verify", "urgent", "fee"]
    text = f"{subject} {complaint}".lower()
    for word in suspicious_words:
        if word in text:
            return "HIGH"
    return "LOW"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    subject = data.get("subject", "")
    complaint = data.get("complaint", "")
    threat_level = analyze_text(subject, complaint)
    return jsonify({"threat": threat_level})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
