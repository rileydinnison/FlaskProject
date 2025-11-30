from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/RileyDinnison')
def greet(name="RileyDinnison"):
    return f"Hello {name}"

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

@app.route('/f/<celsius>')
def show_fahrenheit(celsius):
    return str(convert_celsius_to_fahrenheit(float(celsius)))

if __name__ == '__main__':
    app.run()
