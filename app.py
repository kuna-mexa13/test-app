from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def info():
    return {
        "app": "K8s Info App",
        "version": "1.0.1",
        "environment": os.getenv("ENV", "development"),
        "message": "Hello from Kubernetes!"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

