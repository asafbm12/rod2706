from flask import Flask, render_template

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

# 4. ניווט לעמוד אודות וצור קשר
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bug_line = f"[{current_time}] שם: {user_name} | מייל: {user_email} | באג: {user_message}\n"

        with open(BUGS_FILE, mode='a', encoding='utf-8') as file:
            file.write(bug_line)

        # מחזיר תשובת אימות מהירה לדפדפן (סטטוס הצלחה) במקום לרענן את העמוד
        return jsonify({"status": "success", "message": "הפנייה התקבלה בהצלחה"})

    return render_template('about.html')


# 5. ניווט לעמוד מדיניות הפרטיות
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    # מריץ את האתר על השרת המקומי במחשב שלך
    app.run(debug=True)
