from datetime import datetime
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)

BUGS_FILE = 'bugs.txt'


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
        # קריאת הנתונים מהטופס
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')

        # הנה פקודת הרישום האמיתית לתוך הקובץ bugs.txt:
        with open('bugs.txt', mode='a', encoding='utf-8') as file:
            file.write(f"שם: {user_name} | מייל: {user_email} | הודעה: {user_message}\n")

        # רענון ורינדור מחדש של הדף
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
