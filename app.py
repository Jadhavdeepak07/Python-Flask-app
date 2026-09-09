from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python App</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }

            .box {
                margin-top: 150px;
                padding: 40px;
            }

            h1 {
                font-size: 50px;
            }

            p {
                font-size: 22px;
            }

            button {
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                background: white;
                color: #764ba2;
                cursor: pointer;
            }

            button:hover {
                background: #ffd369;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>🚀 Python App is Running!</h1>
            <p>Welcome to My Flask Application</p>
            <p>☁️ AWS EC2 | 🐍 Python | 🌐 Flask</p>

            <button onclick="alert('Server is Working! 🎉')">
                Check Server
            </button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
