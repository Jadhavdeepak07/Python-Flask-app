# 🐍 Python Flask App

A simple Python Flask web application created for learning and practicing **Python, Flask, Git, GitHub, and AWS EC2 deployment**.

## 🚀 Features

- Simple Flask web application
- Colorful homepage
- Runs on AWS EC2
- Uses Python 3 and Flask
- Easy to deploy and test

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML
- CSS
- AWS EC2
- Git & GitHub

## 📁 Project Structure

Python-Flask-app/  
│  
├── app.py  
└── README.md

## ⚙️ Installation

Clone the repository:

git clone <https://github.com/Jadhavdeepak07/Python-Flask-app.git>

Go to the project directory:

cd Python-Flask-app

Install Flask:

python3 -m pip install flask

## ▶️ Run the Application

python3 app.py

The application will run on:

<http://0.0.0.0:5000>

For AWS EC2, open:

<http://YOUR-EC2-PUBLIC-IP:5000>

## 🔐 AWS EC2 Security Group

Allow inbound traffic on port **5000**:

Type: Custom TCP  
Port: 5000  
Source: 0.0.0.0/0

For production, restrict the source or use a reverse proxy such as Nginx.

## 📌 Git Commands

git add .  
git commit -m "Add Python Flask app"  
git push origin main

## 👨‍💻 Author

**Deepak Jadhav**

## 📄 License

This project is created for learning and practice purposes.
