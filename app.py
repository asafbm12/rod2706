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
@app.route('/about')
def about():
    return render_template('about.html')

# 5. ניווט לעמוד מדיניות הפרטיות
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    # מריץ את האתר על השרת המקומי במחשב שלך
    app.run(debug=True)
