from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(
    __name__,
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'css')),
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages'))
)

# MongoDB connection
client = MongoClient("mongodb+srv://ml_dept_project:ml_dept_project@ml-project.gkigx.mongodb.net/")
db = client['livenfit']
users_collection = db['users']
design_collection = db['designs']

app.secret_key = 'your_secret_key'  # Set a strong secret key!

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/design_form_portal', methods=['GET', 'POST'])
def design_portal():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        # Store the data in the database
        design_collection.insert_one(form_data)
        return render_template('2d-design.html', form_data=form_data)
    return render_template('design_form_portal.html')
 
@app.route('/my_designs_gallery')
def designs_gallery():
    return render_template('my_designs_gallery.html')

@app.route('/technology_deep_dive')
def tech_deep_dive():
    return render_template('technology_deep_dive.html')

@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        # Simple price prediction logic (customize as needed)
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
        return render_template('pricing.html', form_data=form_data, price=price)
    else:
        return render_template('pricing.html', form_data=None, price=None)

@app.route('/2d-design', methods=['GET', 'POST'])
def design_2d():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return render_template('2d-design.html', form_data=form_data)
    else:
        return render_template('2d-design.html', form_data=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            # You can use Flask session here for login persistence
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
            return jsonify({'error': 'Email already registered'}), 400

        hashed_password = generate_password_hash(password)
        users_collection.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password
        })
        return jsonify({'message': 'Registration successful'}), 200

    return render_template('register.html')

# Example API endpoint for family grid (GET/POST)
@app.route('/api/family', methods=['GET', 'POST'])
def family_api():
    if request.method == 'POST':
        data = request.json
        return jsonify({"status": "success", "received": data}), 200
    else:
        return jsonify({
            "children": 2,
            "couples": 1,
            "singles": 1,
            "teens": 1
        })

if __name__ == '__main__':
    app.run(debug=True)
