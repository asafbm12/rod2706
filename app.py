
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BUGS_FILE = Path(__file__).resolve().parent / "bugs.txt"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guide")
def guide():
    return render_template("guide.html")


@app.route("/updates")
def updates():
    return render_template("updates.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        print("קיבלתי טופס!")

        print("כל הנתונים:", request.form)

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        try:
            with open(bugs.txt, "a", encoding="utf-8") as file:
                file.write(
                    f"שם: {name} | מייל: {email} | הודעה: {message}\n"
                )
                file.flush()

            print("נשמר בהצלחה!")
            print("הנתיב לקובץ:", bugs.txt)
            print("גודל הקובץ:", bugs.txt.stat().st_size)

        except Exception as error:
            print("שגיאה בכתיבה:", repr(error))
            return "שגיאה בשמירת ההודעה. בדוק את ה-Terminal.", 500

        return redirect(url_for("about"))

    return render_template("about.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/ads.txt")
def ads_txt():
    return app.send_static_file("ads.txt")


if __name__ == "__main__":
    app.run(debug=True)
