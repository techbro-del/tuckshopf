#app.py
from flask import Flask, request, jsonify, render_template, url_for, redirect
from firebase_admin import credentials, initialize_app, firestore
# Path to the service account key
SERVICE_KEY_PATH = r'C:\Users\brigh\OneDrive\Desktop\Tuck_shop\credentials\servicekey.json'

# Initialize Firebase app
try:
    cred = credentials.Certificate(SERVICE_KEY_PATH)
    initialize_app(cred)
    print("Firebase successfully initialized.")
except FileNotFoundError:
    print(f"Error: The service key file '{SERVICE_KEY_PATH}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred during Firebase initialization: {e}")
# Initialize Firestore client
db = firestore.client()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def handle_register():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    email = request.form['email']
    student_number = request.form['student_number']

    # Check if the form data is valid
    if not all([first_name, second_name, email, student_number]):
        return render_template('register.html', error="All fields are required!")

    # Handle form data (e.g., save to Firestore under the 'users' collection)
    try:
        # Add the user's data to Firestore
        user_data = {
            "first_name": first_name,
            "second_name": second_name,
            "email": email,
            "student_number": student_number
        }
        # Add the user to the 'users' collection
        db.collection('users').add(user_data)

        # Return a success message and redirect back to the register page or a thank-you page
        return render_template('register.html', success="Registration successful!")

    except Exception as e:
        # In case of any errors while saving to Firestore
        return render_template('register.html', error=f"An error occurred: {str(e)}")

       
if __name__ == '__main__':
    app.run(debug=True) 
