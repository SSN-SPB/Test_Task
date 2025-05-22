from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/view')
def view():
    return "Que vista!"

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000 displays 'Hello, World!!'
# http://127.0.0.1:5000/view displays 'Que vista!'