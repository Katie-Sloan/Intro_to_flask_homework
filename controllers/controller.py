from app import app

@app.route('/')

@app.route('/<name>')
def greet(name):
    return "Not long till Christmas!"