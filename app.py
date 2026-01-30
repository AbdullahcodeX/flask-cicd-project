import os
from flask import Flask

app = Flask(__name__)

# Logic: If environment is 'live', use port 5000; otherwise use 4000
ENVIRONMENT = os.getenv("APP_ENV", "dev")

if ENVIRONMENT == "live":
    PORT = int(os.getenv("APP_PORT", 5000))
else:
    PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")
def home():
    if ENVIRONMENT == "live":
        return "Abdullah how are you? Welcome to Live environment"
    else:
        return "Welcome to Dev environment"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
