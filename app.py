from flask import Flask, render_template, request, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form.get("lang", "en")

        # gTTS object create
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save audio file inside static folder
        file_path = os.path.join("static", "output.mp3")
        tts.save(file_path)

        audio_file = url_for("static", filename="output.mp3")

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)
