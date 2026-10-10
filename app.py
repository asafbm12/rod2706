from flask import Flask,render_template,redirect,url_for,request

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

@app.route('/about', methods=['POST'])
def save_bug():
    # 1. קליטת הנתונים שהמשתמש רשם בטופס ה-HTML שלך
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_message = request.form.get('message')

    # 2. כתיבה ושמירה בתוך קובץ ה-TXT בשורה חדשה
    with open('bugs.txt', mode='a', encoding='utf-8') as file:
        file.write(f"שם: {user_name} | מייל: {user_email} | הודעה: {user_message}\n")

    # 3. הפינאלה - הפקודה הזו מחליפה את תג ה-A!
    # היא לוקחת את הדפדפן בחזרה לעמוד הבית ומאלצת אותו לבצע רינדור מחדש מלא.
    return redirect(url_for('home'))


# 5. ניווט לעמוד מדיניות הפרטיות
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    # מריץ את האתר על השרת המקומי במחשב שלך
    app.run(debug=True)
