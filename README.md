# Live N Fit

A web application for personalized home design using AI and user preferences.

## Features
- User registration and login
- Save and view design drafts
- Predict home price, rooms, and baths using ML models
- Interactive design form portal
- MongoDB backend

## Getting Started

### Prerequisites
- Python 3.9+
- Git (optional)

### Setup
1. Clone the repository or download the source code.
2. Open a terminal in the project directory.
3. Run the batch file to set up and start the app:
	```
	run_app.bat
	```
	This will:
	- Create a virtual environment (if not present)
	- Install required packages
	- Start the Flask app

### Manual Setup
If you prefer manual setup:
1. Create a virtual environment:
	```
	python -m venv venv
	```
2. Activate the environment:
	```
	venv\Scripts\activate
	```
3. Install dependencies:
	```
	pip install -r requirements.txt
	```
4. Run the app:
	```
	python app.py
	```


## File Structure

```
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
```

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `run_app.bat` - Windows batch file for setup and running
- `pages/` - HTML templates
- `css/` - Stylesheets
- `model_price.pkl`, `model_rooms.pkl`, `model_baths.pkl` - ML models

## Environment Variables
- Set your MongoDB connection string in `app.py` if needed.
- Change the Flask secret key in `app.py` for production.

## License
MIT
