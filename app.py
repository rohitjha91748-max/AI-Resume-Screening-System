from flask import Flask, render_template, request
from services.pdf_parser import extract_text
from services.skill_extractor import extract_skills
from services.matcher import calculate_score
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

JOB_SKILLS = [
    "python",
    "sql",
    "flask",
    "html"
]

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(path)

    text = extract_text(path)

    skills = extract_skills(text)

    score = calculate_score(
        skills,
        JOB_SKILLS
    )

    return render_template(
        "result.html",
        skills=skills,
        score=score
    )

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)