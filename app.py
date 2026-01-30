import os
from flask import Flask

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "dev")
<<<<<<< HEAD
PORT = int(os.getenv("APP_PORT", 5000))
=======
PORT = int(os.getenv("APP_PORT", 4000))
>>>>>>> 2b7cb24720acafada1cbdd3788f1bfc01e0dd9ff


@app.route("/")
def home():
    if ENVIRONMENT == "live":
<<<<<<< HEAD
        return "Abdullah how are you"
=======
        return "Welcome to Live environment"
    else:
        return "Welcome to Dev environment"

>>>>>>> 2b7cb24720acafada1cbdd3788f1bfc01e0dd9ff

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
