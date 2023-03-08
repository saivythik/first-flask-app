from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello! this is flask home"

if __name__ == "__main__":
    print("100")
    app.run()

