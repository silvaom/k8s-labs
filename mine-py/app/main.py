from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hola desde Argentina para todo el site de Chile"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
