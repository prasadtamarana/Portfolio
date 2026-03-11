from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    user_info = {
        "name": "Rajendra Prasad",
        "role": "Aspiring Data Scientist",
        "email": "prasadtamarana11@gmail.com"
    }
    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)