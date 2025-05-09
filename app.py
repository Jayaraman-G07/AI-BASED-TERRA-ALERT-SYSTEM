from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import joblib
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Load trained model and preprocessing tools
rf_model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Blynk API URLs
ACCEL_URL = "https://blynk.cloud/external/api/get?token=a0R-kWpg-zJ6EX7r0U67MfkoKd72XTwK&V0"
VIBRATION_URL = "https://blynk.cloud/external/api/get?token=a0R-kWpg-zJ6EX7r0U67MfkoKd72XTwK&V1"
LOCATION_URL = "https://blynk.cloud/external/api/get?token=a0R-kWpg-zJ6EX7r0U67MfkoKd72XTwK&V4"

RESULT_UPLOAD_URL = "https://blynk.cloud/external/api/update?token=a0R-kWpg-zJ6EX7r0U67MfkoKd72XTwK&V2={}"  

# Dummy user credentials (replace with a database in production)
users = {'admin': '1234'}

# Function to fetch accelerometer data
def get_accelerometer_data():
    try:
        response = requests.get(ACCEL_URL)
        response.raise_for_status()
        data = response.text.replace(" ", "").split("y:")
        accel_x = float(data[0].split(":")[1])
        accel_y = float(data[1].split("Z:")[0])
        accel_z = float(data[1].split("Z:")[1])
        return accel_x, accel_y, accel_z
    except:
        return None, None, None

# Function to fetch sensor values (vibration/location)
def get_sensor_value(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except:
        return "Unavailable"

# Function to predict landslide
def predict_disaster(accel_x, accel_y, accel_z, vibration):
    try:
        new_data = pd.DataFrame({'Accel_X': [accel_x], 'Accel_Y': [accel_y], 'Accel_Z': [accel_z], 'Vibration': [vibration]})
        new_data_scaled = scaler.transform(new_data)
        prediction = rf_model.predict(new_data_scaled)
        result = label_encoder.inverse_transform(prediction)[0]
        return "Landslide Detected" if result == 1 else "Normal"
    except:
        return "Prediction Error"

# Upload result to Blynk
def upload_result_to_blynk(result):
    try:
        requests.get(RESULT_UPLOAD_URL.format(result))
    except:
        pass

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        return "Invalid credentials. Try again."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['GET'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    accel_x, accel_y, accel_z = get_accelerometer_data()
    vibration = get_sensor_value(VIBRATION_URL)
    location = get_sensor_value(LOCATION_URL)

    if None in [accel_x, accel_y, accel_z] or vibration == "Unavailable":
        return render_template('result.html', prediction='Failed to fetch sensor data', location="Unknown")

    result = predict_disaster(accel_x, accel_y, accel_z, float(vibration))
    upload_result_to_blynk(result)

    return render_template('result.html', prediction=result, accel_x=accel_x, accel_y=accel_y, accel_z=accel_z,vibration=vibration, location=location)

if __name__ == '__main__':
    app.run(debug=True)
