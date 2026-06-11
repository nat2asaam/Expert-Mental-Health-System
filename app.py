from flask import Flask, render_template, request,jsonify,redirect,url_for,make_response,session
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import db
from models import User,Patient
from flask_mail import Mail, Message
import random
import json
from datetime import datetime, timedelta
from SentimentAndEmotion.sentiment_and_emotion import analyze_text
app = Flask(__name__)
app.secret_key = 'ga91nxvdgdt^&anaiete5%' # Use a long, random string in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'equicksalessupport'
app.config['MAIL_DEFAULT_SENDER'] = 'equicksalessupport@gmail.com'
app.config['MAIL_PASSWORD'] = 'ymij hyay cjsg kbhu'
mail = Mail(app)
db.init_app(app)

@app.route('/')
@app.route('/login')
def index():
    session.clear()
    return render_template('index.html')
@app.route("/dummy-register") 
def dummy_register():
    username = "admin"
    email = "admin@example.com"
    password = "admin123"
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password,active=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': f'User {username} registered successfully'})
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get("email")
        hashed_password = generate_password_hash(password)
        one_hour_from_now = datetime.now() + timedelta(hours=1)
        otp="".join([str(random.randint(0, 9)) for _ in range(6)])
        new_user = User(username=username, email=email, password=hashed_password,otp_expiry=one_hour_from_now,otp=otp,active=False)
        db.session.add(new_user)
        db.session.commit()
        session["otp"]=otp
        return redirect(url_for('send_otp', email=email, username=username))
    return render_template('register.html')
@app.route("/send-otp/<string:email>/<string:username>")
def send_otp(email, username):
    msg = Message(
        subject="Email Verification OTP",
        recipients=[email],
        body="This is a test email sent from a Flask application using Flask-Mail."
    )
    # You can also send HTML content
    otp=session.get("otp")
    if otp:
        msg.html = "<p>Hello "+username+",<br>Thank you for signing up! Please verify your email address by using the OTP code below: </p><div style='width:200px; background-color: #f0f0f0; padding: 10px; border: 1px solid #ccc;'>"+otp+"</div>"
        mail.send(msg)
        session.clear()
        return render_template('otp.html')
    return "OTP not found in cookies", 400
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form.get('email')
    otp = request.form.get('otp')
    user = User.query.filter_by(email=email).first()
    if user and user.otp == otp and user.otp_expiry > datetime.now():
        user.active = True
        user.otp = None
        user.otp_expiry = None
        db.session.commit()
        return redirect(url_for('login'))
    return jsonify({'message': 'Invalid OTP or OTP has expired'}), 400
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user:
        is_valid = check_password_hash(user.password, password)
        if is_valid:
            session['username'] = username
            if user.active:
                return redirect(url_for('dashboard'))
    return jsonify({'message': 'Invalid username or password'}), 401
@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('dashboard.html',username=username)
@app.route('/analytics')
def analytics():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('analytics.html',username=username)
@app.route('/patients')    
def patients():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('patients.html',username=username)
@app.route("/consultations")
def consultations():
    username=session.get("username")
    if not username:
        return redirect(url_for('index'))
    return render_template('consultation.html',username=username)
@app.route("/analyze-text", methods=['POST'])
def analyze_data_text():
    text = request.form.get('text')
    result = analyze_text(text)
    json_result = json.loads(result)
    keywords = json_result.get('keywords', [])
    entities = json_result.get('entities', [])
    usage = json_result.get('usage', {})
    #return json_result
    return jsonify({'text': f'Analysis result for: {text}', 'keywords': keywords, 'entities': entities, 'usage': usage})
if __name__ == '__main__':
    # Create the database tables before starting the app
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0',port=8080)

