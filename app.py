from datetime import datetime
# הוספנו את request כדי לקרוא את השדות מהטופס, ואת send_from_directory בשביל אדסנס
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


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


# 4. ניווט לעמוד אודות וצור קשר - מעודכן לטיפול בשליחת הטופס (POST)
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # קליטת הנתונים מתוך שדות ה-HTML שהגולש הקליד
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')

        # לקיחת הזמן המדויק של השליחה
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # כתיבה מסודרת בשורה אחת לתוך קובץ הטקסט (במצב a - הוספה לסוף)
        bug_line = f"[{current_time}] שם: {user_name} | מייל: {user_email} | הודעה: {user_message}\n"

        with open('bugs.txt', mode='a', encoding='utf-8') as file:
            file.write(bug_line)

        # מחזיר קוד 204 שאומר לדפדפן: "הכל נשמר, אל תרענן ואל תעשה כלום במסך"
        return '', 204

    return render_template('about.html')


# 5. ניווט לעמוד מדיניות הפרטיות
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


# 6. נתיב חובה עבור קובץ האימות של גוגל אדסנס
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory(app.root_path, 'ads.txt')


if __name__ == '__main__':
    # מריץ את האתר על השרת המקומי במחשב שלך
    app.run(debug=True)
