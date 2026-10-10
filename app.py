
from pathlib import Path
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)

# שמירת bugs.txt באותה תיקייה שבה נמצא app.py
BUGS_FILE = Path(app.root_path) / 'bugs.txt'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guide')
def guide():
    return render_template('guide.html')


@app.route('/updates')
def updates():
    return render_template('updates.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        print("התקבלה בקשת POST!")

        # קבלת הנתונים מהטופס
        user_name = request.form.get('name', '').strip()
        user_email = request.form.get('email', '').strip()
        user_message = request.form.get('message', '').strip()

        print("שם:", repr(user_name))
        print("אימייל:", repr(user_email))
        print("הודעה:", repr(user_message))

        # בדיקה שכל השדות מלאים
        if not user_name or not user_email or not user_message:
            print("שגיאה: אחד או יותר מהשדות ריקים")
            return "נא למלא את כל השדות בטופס", 400

        try:
            # כתיבת הנתונים לקובץ
            with open(BUGS_FILE, 'a', encoding='utf-8') as file:
                file.write(
                    f"שם: {user_name} | "
                    f"מייל: {user_email} | "
                    f"הודעה: {user_message}\n"
                )

            print("ההודעה נשמרה בהצלחה!")
            print("מיקום הקובץ:", BUGS_FILE.resolve())

        except OSError as error:
            print("שגיאה בשמירת הקובץ:", error)
            return "אירעה שגיאה בשמירת ההודעה", 500

        # חזרה לעמוד אודות לאחר השליחה
        return redirect(url_for('about'))

    return render_template('about.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/ads.txt')
def ads_txt():
    return send_from_directory(app.root_path, 'ads.txt')


if __name__ == '__main__':
    app.run(debug=True)

