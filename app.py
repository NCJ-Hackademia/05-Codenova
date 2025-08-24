from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
import smtplib
from email.mime.text import MIMEText
from bson.objectid import ObjectId
import pickle

# Helper function to convert ObjectId to string for JSON serialization
def sanitize_for_json(data):
    if isinstance(data, list):
        return [sanitize_for_json(item) for item in data]
    if isinstance(data, dict):
        return {key: sanitize_for_json(value) for key, value in data.items()}
    if isinstance(data, ObjectId):
        return str(data)
    return data

app = Flask(
    __name__,
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'css')),
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages'))
)

# Set a secret key for session management
app.secret_key = 'your-very-secret-key'  # Change this to a strong, random value in production

# Temporary storage for design preferences
design_data_store = {}

# MongoDB connection
try:
    client = MongoClient("mongodb+srv://ml_dept_project:ml_dept_project@ml-project.gkigx.mongodb.net/")
    db = client['livenfit']
    users_collection = db['users']
    design_collection = db['designs']
    draft_collection = db['drafts']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

def send_email(subject, recipient, body):
    sender_email = "noreply@livenfit.com"
    print("--- Sending Email ---")
    print(f"To: {recipient}")
    print(f"From: {sender_email}")
    print(f"Subject: {subject}")
    print("--- Body ---")
    print(body)
    print("---------------------")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    user_name = session.get('user_name', None)
    return render_template('homepage.html', user_name=user_name)

@app.route('/about')
def about():
    user_name = session.get('user_name', None)
    return render_template('about.html', user_name=user_name)

@app.route('/contact')
def contact():
    user_name = session.get('user_name', None)
    return render_template('contact.html', user_name=user_name)

@app.route('/design_form_portal', methods=['GET', 'POST'])
def design_portal():
    user_name = session.get('user_name', None)
    email = session.get('email')
    if request.method == 'POST':
        design_preferences = request.form.to_dict()
        design_preferences.setdefault('children-count', '0')
        design_preferences.setdefault('couples-count', '0')
        design_preferences.setdefault('singles-count', '0')
        session['design_preferences'] = sanitize_for_json(design_preferences)
        if email:
            design_data_store[email] = design_preferences
            print("--- Temporarily Stored Design Preferences ---")
            for key, value in design_preferences.items():
                print(f"{key}: {value}")
            print("-------------------------------------------")
        if email:
            design_preferences['user_email'] = email
            draft_collection.delete_one({'user_email': email})
            try:
                email_subject = "Your Live N Fit Design Submission"
                email_body = f"Hello {user_name},\n\nThank you for submitting your design preferences.\n\nHere is a summary of your submission:\n"
                for key, value in design_preferences.items():
                    display_key = key.replace('-', ' ').replace('_', ' ').title()
                    email_body += f"- {display_key}: {value}\n"
                email_body += "\nWe will review your design and get back to you shortly.\n\nBest regards,\nThe Live N Fit Team"
                send_email(email_subject, email, email_body)
                flash("Design submitted and a confirmation email has been sent.", "success")
            except Exception as e:
                flash(f"There was an error sending the confirmation email: {e}", "danger")
        design_collection.insert_one(design_preferences)
        sanitized_form_data = sanitize_for_json(design_preferences)
        return render_template('2d-design.html', form_data=sanitized_form_data, user_name=user_name)
    draft_data = session.get('design_preferences')
    if not draft_data and email:
        draft_data_from_db = draft_collection.find_one({'user_email': email})
        if draft_data_from_db:
            draft_data = sanitize_for_json(draft_data_from_db)
    else:
        if draft_data:
            draft_data = sanitize_for_json(draft_data)
    return render_template('design_form_portal.html', user_name=user_name, draft_data=draft_data)

@app.route('/save_draft', methods=['POST'])
def save_draft():
    if 'email' not in session:
        return jsonify({'status': 'error', 'message': 'User not logged in'}), 401
    email = session['email']
    draft_data = request.json
    # Save draft
    draft_collection.update_one(
        {'user_email': email},
        {'$set': draft_data},
        upsert=True
    )
    # If this is a final save (from pricing), also save to designs
    if draft_data.get('final_save'):
        draft_data['user_email'] = email
        # Remove any _id if present (to avoid duplicate key error)
        draft_data.pop('_id', None)
        design_collection.insert_one(draft_data)
    return jsonify({'status': 'success', 'message': 'Draft saved successfully'})
 
@app.route('/my_designs_gallery')
def designs_gallery():
    user_name = session.get('user_name', None)
    email = session.get('email')
    if email:
        user_designs_from_db = list(design_collection.find({'user_email': email}))
        user_designs = sanitize_for_json(user_designs_from_db)
    else:
        user_designs = []
    return render_template('my_designs_gallery.html', user_name=user_name, designs=user_designs)

@app.route('/technology_deep_dive')
def tech_deep_dive():
    user_name = session.get('user_name', None)
    return render_template('technology_deep_dive.html', user_name=user_name)

@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    user_name = session.get('user_name', None)
    if request.method == 'POST':
        form_data = request.form.to_dict()
        base_price = 1500  # per sq ft
        size = int(form_data.get('size-btn', 1000))
        floors = int(form_data.get('floor-btn', 1))
        style_factor = {
            'modern': 1.2,
            'traditional': 1.0,
            'contemporary': 1.1,
            'farmhouse': 1.05,
            'industrial': 1.15,
            'transitional': 1.08
        }
        style = form_data.get('style-btn', 'modern').lower()
        factor = style_factor.get(style, 1.0)
        price = int(size * floors * base_price * factor)
        email = session.get('email')
        if email:
            draft_collection.delete_one({'user_email': email})
        session.pop('design_preferences', None)
        return render_template('pricing.html', form_data=form_data, price=price, user_name=user_name)
    else:
        return render_template('pricing.html', form_data=None, price=None, user_name=user_name)

@app.route('/design_2d')
def design_2d():
    return render_template('2d-design.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user_name'] = user['name']
            session['email'] = user['email']
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if users_collection.find_one({'email': email}):
            return jsonify({'error': 'Email already registered'}), 409
        hashed_password = generate_password_hash(password)
        users_collection.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password
        })
        return jsonify({'message': 'Registration successful'}), 200
    return render_template('register.html')

@app.route('/api/family', methods=['POST'])
def family_api():
    data = request.json
    return jsonify({"status": "success", "received": data}), 200

@app.route('/view_stored_data')
def view_stored_data():
    return jsonify(design_data_store)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('homepage'))

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')
    user = users_collection.find_one({'email': email})
    if user:
        return jsonify(success=True, message="Reset link sent.")
    else:
        return jsonify(success=False, message="Email not found.")

@app.route('/forgot_password')
def forgot_password_page():
    return render_template('forgot_password.html')

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')
    if not email or not new_password:
        return jsonify(success=False, field='email', message='Email and new password are required.')
    if len(new_password) < 6:
        return jsonify(success=False, field='new_password', message='New password must be at least 6 characters.')
    user = users_collection.find_one({'email': email})
    if not user:
        return jsonify(success=False, field='email', message='Email not found.')
    users_collection.update_one(
        {'email': email},
        {'$set': {'password': generate_password_hash(new_password)}}
    )
    return jsonify(success=True, message='Password changed successfully.')

@app.route('/predict-price', methods=['POST'])
def predict_price():
    data = request.get_json()
    area = data.get('area')
    rooms = data.get('rooms')
    floors = data.get('floors')
    predictions = {}
    try:
        with open('model_rooms.pkl', 'rb') as f:
            rooms_model = pickle.load(f)
        features = [[area, rooms, floors]]
        predictions['rooms'] = int(rooms_model.predict(features)[0])
    except Exception as e:
        print(f"Error with rooms model: {e}")
        predictions['rooms'] = None
    try:
        with open('model_price.pkl', 'rb') as f:
            price_model = pickle.load(f)
        features = [[area, rooms, floors]]
        predictions['price'] = int(price_model.predict(features)[0])
    except Exception as e:
        print(f"Error with price model: {e}")
        predictions['price'] = None
    try:
        with open('model_baths.pkl', 'rb') as f:
            baths_model = pickle.load(f)
        features = [[area, rooms, floors]]
        predictions['baths'] = int(baths_model.predict(features)[0])
    except Exception as e:
        print(f"Error with baths model: {e}")
        predictions['baths'] = None
    return jsonify(predictions)

@app.route('/get-design-preferences', methods=['GET'])
def get_design_preferences():
    email = session.get('email')
    if not email:
        return jsonify({'error': 'User not logged in'}), 401
    design_prefs = design_data_store.get(email) or session.get('design_preferences', {})
    if not design_prefs:
        return jsonify({'error': 'No design preferences found'}), 404
    return jsonify(sanitize_for_json(design_prefs))

@app.route('/clear_design_draft', methods=['POST'])
def clear_design_draft():
    email = session.get('email')
    if email:
        draft_collection.delete_one({'user_email': email})
        design_data_store.pop(email, None)
    session.pop('design_preferences', None)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
