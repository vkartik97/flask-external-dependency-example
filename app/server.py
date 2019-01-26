from flask import Flask


app = Flask(__name__)

# Crawler should be called here
@app.route("/run_crawler")
def index():
    # This is where Crawler is be called
    return "Hello World!"


@app.route("/test")
def test():
    return "Server is working!"


if __name__ == '__main__':
   app.run()