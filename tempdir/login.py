import ipapi
from flask import Flask, request, render_template
 
app = Flask(__name__, static_url_path='')
 
@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5050)