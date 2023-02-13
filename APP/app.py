from flask import Flask, url_for, render_template
import os
from markupsafe import escape #Use Escape whenever there's possibility of a user variable
os.chdir('/Users/haoyang/Documents/Coding/Python/PokerNow_Project/APP')

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

