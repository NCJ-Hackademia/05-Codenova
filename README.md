# Live N Fit

A web application for personalized home design using AI and user preferences.

## Features
 - 2D home design generation using GAN (Generative Adversarial Network)

## Getting Started
 The project uses GAN (Generative Adversarial Network) for generating 2D home designs based on user preferences. This enables realistic and personalized design outputs.

### Prerequisites

### Setup
1. Clone the repository or download the source code.
2. Open a terminal in the project directory.
3. Run the batch file to set up and start the app:
	
	run_app.bat
	
	This will:
	- Create a virtual environment (if not present)
	- Install required packages
	- Start the Flask app

### Manual Setup
If you prefer manual setup:
1. Create a virtual environment:
	
	python -m venv venv
	
2. Activate the environment:
	
	venv\Scripts\activate
	
3. Install dependencies:
	
	pip install -r requirements.txt
	
4. Run the app:
	
	python app.py
	


## File Structure


live_n_fit/
│   app.py
│   requirements.txt
│   run_app.bat
│   README.md
│   tailwind.config.js
│   package.json
│   model_price.pkl
│   model_rooms.pkl
│   model_baths.pkl
│
├── css/
│     main.css
│     tailwind.css
│
├── pages/
│     index.html
│     homepage.html
│     about.html
│     contact.html
│     design_form_portal.html
│     2d-design.html
│     my_designs_gallery.html
│     pricing.html
│     register.html
│     login.html
│     forgot_password.html
│     technology_deep_dive.html
│
├── public/
│     favicon.ico
│     manifest.json
│
└── __pycache__/
	app.cpython-313.pyc


- app.py - Main Flask application
- requirements.txt - Python dependencies
- run_app.bat - Windows batch file for setup and running
- pages/ - HTML templates
- css/ - Stylesheets
- model_price.pkl, model_rooms.pkl, model_baths.pkl - ML models

## Environment Variables
- Set your MongoDB connection string in app.py if needed.
- Change the Flask secret key in app.py for production.

## Technologies Used

- Python 3.9+
- Flask (web framework)
- MongoDB (database)
- PyMongo (MongoDB connector)
- scikit-learn (ML model predictions)
- GAN (Generative Adversarial Network for 2D design generation)
- HTML, CSS, JavaScript (frontend)
- Tailwind CSS (utility-first CSS framework)
- Jinja2 (template rendering)
- Werkzeug (security/password hashing)
- Batch scripting (run_app.bat)

## License
MIT
