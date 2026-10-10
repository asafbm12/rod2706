from datetime import datetime
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)

BUGS_FILE = 'bugs.txt'


# 1. ניווט לעמוד הבית והמשחק
@app.route('/')
def home():
    return render_template('index.html')


# 2. ניווט לעמוד המדריך למשתמש
@app.route('/guide')
def guide():
    return render_template('guide.html')


# 3. ניווט לבלוג העדכונים
@app.route('/updates')
def updates():
    return render_template('updates.html')


# 4. עמוד אודות - קבלת הנתונים מהטופס ורינדור מחדש
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # פייתון מושך את הנתונים מה-HTML
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bug_line = f"[{current_time}] שם: {user_name} | מייל: {user_email} | הודעה: {user_message}\n"

        # כתיבה לקובץ הטקסט הקיים שלך
        with open(BUGS_FILE, mode='a', encoding='utf-8') as file:
            file.write(bug_line)

        # פקודת פייתון שמנקה את הטופס ומבצעת רינדור מחדש של הדף
        return redirect(url_for('about'))

    return render_template('about.html')


# 5. ניווט לעמוד מדיניות הפרטיות
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


# 6. קובץ האימות עבור גוגל אדסנס
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory(app.root_path, 'ads.txt')


if __name__ == '__main__':
    app.run(debug=True)
