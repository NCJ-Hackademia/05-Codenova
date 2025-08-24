# Live N Fit

A web application for personalized home design using AI and user preferences.

---

## Features

- 2D home design generation using GAN (Generative Adversarial Network)
- Personalized design recommendations
- Cost and room estimation using ML models
- User authentication and design gallery

---

## Getting Started

The project uses GANs for generating 2D home designs based on user preferences, enabling realistic and personalized design outputs.

### Prerequisites

- Python 3.9+
- MongoDB

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/NCJ-Hackademia/05-Codenova.git
    cd live_n_fit
    ```

2. **Run the batch file to set up and start the app:**
    ```sh
    run_app.bat
    ```
    This will:
    - Create a virtual environment (if not present)
    - Install required packages
    - Start the Flask app

#### Manual Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
2. Activate the environment:
    ```sh
    venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the app:
    ```sh
    python app.py
    ```

---

## File Structure

```
live_n_fit/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── run_app.bat             # Windows batch file for setup and running
├── README.md               # Project documentation
├── tailwind.config.js      # Tailwind CSS configuration
├── package.json            # Node.js dependencies (for Tailwind build)
├── model_price.pkl         # ML model for price prediction
├── model_rooms.pkl         # ML model for room prediction
├── model_baths.pkl         # ML model for bath prediction
│
├── css/                    # Stylesheets
│   ├── main.css
│   └── tailwind.css
│
├── pages/                  # HTML templates (Jinja2)
│   ├── index.html
│   ├── homepage.html
│   ├── about.html
│   ├── contact.html
│   ├── design_form_portal.html
│   ├── 2d-design.html
│   ├── my_designs_gallery.html
│   ├── pricing.html
│   ├── register.html
│   ├── login.html
│   ├── forgot_password.html
│   └── technology_deep_dive.html
│
├── public/                 # Static files (favicon, manifest)
│   ├── favicon.ico
│   └── manifest.json
│
└── __pycache__/            # Python bytecode cache
    └── app.cpython-313.pyc
```

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `run_app.bat` - Windows batch file for setup and running
- `pages/` - HTML templates
- `css/` - Stylesheets
- `model_price.pkl`, `model_rooms.pkl`, `model_baths.pkl` - ML models

---

## Environment Variables

- Set your MongoDB connection string in `app.py` if needed.
- Change the Flask secret key in `app.py` for production.

---

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
- Batch scripting (`run_app.bat`)

---

## License

MIT

---

## Hackathon Info

This project was developed as part of **Hackademia 2025 – Codenova** at National College Jayanagar.

- **Team Name:** Codenova  
- **Team Captain (GitHub):** [@giripriyansenthilkumar](https://github.com/giripriyansenthilkumar)  
- **Repository Name:** 05-Codenova  

---

Good luck and happy hacking! 🎉
