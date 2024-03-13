Crop Recommendation System

Introduction
The Crop Recommendation System is a web-based application designed to assist farmers in making informed decisions about which crops to cultivate based on various environmental factors. It utilizes machine learning algorithms to predict suitable crops for a given set of conditions such as soil nutrients, temperature, humidity, and rainfall.

Features
- User Authentication: Users can register and login to access the system.
- Input Form: Users can input data such as nitrogen content, phosphorous content, potassium content, temperature, humidity, pH level, and rainfall.
- Prediction: The system uses a trained machine learning model to predict the most suitable crops based on the input data.
- User Dashboard: Registered users can view their profile and previous predictions.

Technologies Used
- Python: Used for backend development and machine learning model training.
- Flask: A micro web framework used for building the web application.
- SQLAlchemy: An ORM (Object-Relational Mapping) tool used for database management.
- *PostgreSQL: A powerful open-source relational database management system used for storing user data.
- Scikit-learn: A machine learning library used for building and training the crop recommendation model.
- HTML/CSS: Used for frontend development and styling of the web pages.
- JavaScript: Used for client-side scripting and enhancing user interactivity.

Installation
1. Clone the repository

2. Navigate to the project directory:

    cd crop-recommendation-system
    

3. Install the required dependencies:
4. 
    pip install -r requirements.txt

5. Set up the PostgreSQL database. You may need to update the database URI in the `app.py` file to match your PostgreSQL configuration.

6. Run the application:

    python app.py

7. Access the application in your web browser at `http://localhost:5000`.

Usage
1. Register an account or login if you already have one.
2. Input the required data on the prediction form.
3. Click the "Predict" button to view the recommended crops.
4. Logout when you are done using the system.

Acknowledgements
- This project was inspired by the need to provide farmers with actionable insights for optimizing crop cultivation.
- The dataset used for training the machine learning model was obtained from Kaggle.
