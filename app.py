import sys
from flask_cors import CORS

# Ensure the current directory is in the sys.path
sys.path.append(".")

from Yoha import create_app

app = create_app()

# Set up application context
with app.app_context():
    # Initialize CORS extension within the application context
    cors_options = {
        "origins": "*",  # Allow requests from any origin
        "methods": ["GET", "POST", "DELETE", "PUT"],  # Allow specified methods
        "allow_headers": ["Content-Type"]  # Allow specified headers
    }
    # Enable CORS with the specified options
    CORS(app, resources={r"/*": cors_options})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5984)
