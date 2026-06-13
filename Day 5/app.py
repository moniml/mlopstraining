import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from rag.retrieval import retrieve
from rag.generator import generate_answer

# ================= APP =================
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# ================= CONFIG =================
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ================= STATE =================
latest_video_path = None


# ================= HOME =================
@app.route("/")
def home():
    return "Videxa API Running"


# ================= UPLOAD VIDEO =================
@app.route("/upload", methods=["POST"])
def upload_video():
    global latest_video_path

    if "video" not in request.files:
        return jsonify({"error": "No video file received"}), 400

    file = request.files["video"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(file_path)

    # ✅ store latest uploaded video
    latest_video_path = file_path

    return jsonify({
        "message": "Upload successful",
        "video_path": file_path
    })


# ================= ASK QUESTION =================
@app.route("/ask", methods=["POST"])
def ask():
    global latest_video_path

    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Missing query"}), 400

    query = data["query"]

    if not latest_video_path:
        return jsonify({"error": "No video uploaded yet"}), 400

    # ================= RAG FLOW =================
    context = retrieve(query + " " + latest_video_path)
    answer = generate_answer(query, context)

    return jsonify({
        "answer": answer
    })


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)