import os
import sys
from pathlib import Path
from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import UPLOAD_DIR
from prediction import predict_image


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            if "image" not in request.files:
                flash("No image uploaded")
                return redirect(request.url)

            file = request.files["image"]
            if file.filename == "":
                flash("No image selected")
                return redirect(request.url)

            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_DIR, filename)
            file.save(save_path)

            try:
                disease, confidence = predict_image(save_path)
            except FileNotFoundError as exc:
                flash(str(exc))
                return redirect(request.url)

            return render_template(
                "result.html",
                disease=disease,
                confidence=confidence,
                image_name=filename,
                image_path=f"/static/uploads/{filename}",
            )

        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")
