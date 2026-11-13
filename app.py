import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        formspree_form_id=os.environ.get("FORMSPREE_FORM_ID"),
    )
