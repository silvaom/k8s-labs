from flask import Flask

import config

@app.route("/")
def hello():
    return "Dang it"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
