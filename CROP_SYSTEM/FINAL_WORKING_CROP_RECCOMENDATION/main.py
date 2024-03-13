from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy# used for connection to postgresql database
import joblib  # to dump the hoblib file into flask
import numpy as np # for numeric operation like array for prediction
import psycopg2 # database connection

app = Flask(__name__)  # intializing the app
app.secret_key = "secret-key"#torecoed seesion here we are not recording any session of from data
# Load the trained model
model = joblib.load('mod.joblib')  # this is used to import the joblib model that we converetd into the this
# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:king001@localhost/flask'  # database  credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

# Create a User model
class User(db.Model):
    __tablename__ = 'crop_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=True)

    def __init__(self, username,email, password, address):
        self.username = username
        self.email = email
        self.password = password
        self.address = address


# Initialize the app and the database
db.init_app(app)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is not None and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
            return render_template('index.html', error=error)

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email=request.form['email']
        password = request.form['password']
        address=request.form['address']

        user = User.query.filter_by(username=username).first()

        if user is None:
            new_user = User(username,email,password,address)
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id

            return redirect(url_for('dashboard'))
        else:
            error = 'Username already exists'
            return render_template('register.html', error=error)

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        return render_template('d.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template('about.html')
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    form_data = session.get('form_data', {})
    N = form_data.get('nitrogen', 0)
    P = form_data.get('Phosphorous', 0)
    PO = form_data.get('Potassium', 0)
    T = form_data.get('Temperature', 0)
    H = form_data.get('Humidity', 0)
    PH = form_data.get('ph', 0)
    R = form_data.get('Rainfall', 0)
    # Make the predictions
    predict1 = model.predict(np.array([N, P, PO, T, H, PH, R]).reshape(1, -1))
    crop_name = str()
    if predict1 == 0:  # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required.
        crop_name = 'Apple(सेब)'
    elif predict1 == 1:
        crop_name = 'Banana(केला)'
    elif predict1 == 2:
        crop_name = 'Blackgram(काला चना)'
    elif predict1 == 3:
        crop_name = 'Chickpea(काबुली चना)'
    elif predict1 == 4:
        crop_name = 'Coconut(नारियल)'
    elif predict1 == 5:
        crop_name = 'Coffee(कॉफ़ी)'
    elif predict1 == 6:
        crop_name = 'Cotton(कपास)'
    elif predict1 == 7:
        crop_name = 'Grapes(अंगूर)'
    elif predict1 == 8:
        crop_name = 'Jute(जूट)'
    elif predict1 == 9:
        crop_name = 'Kidneybeans(राज़में)'
    elif predict1 == 10:
        crop_name = 'Lentil(मसूर की दाल)'
    elif predict1 == 11:
        crop_name = 'Maize(मक्का)'
    elif predict1 == 12:
        crop_name = 'Mango(आम)'
    elif predict1 == 13:
        crop_name = 'Mothbeans(मोठबीन)'
    elif predict1 == 14:
        crop_name = 'Mungbeans(मूंग)'
    elif predict1 == 15:
        crop_name = 'Muskmelon(खरबूजा)'
    elif predict1 == 16:
        crop_name = 'Orange(संतरा)'
    elif predict1 == 17:
        crop_name = 'Papaya(पपीता)'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas(कबूतर के मटर)'
    elif predict1 == 19:
        crop_name = 'Pomegranate(अनार)'
    elif predict1 == 20:
        crop_name = 'Rice(चावल)'
    elif predict1 == 21:
        crop_name = 'Watermelon(तरबूज)'

    # Pass the result and form data to the template
    return render_template('d.html', result=crop_name, form_data=form_data)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
