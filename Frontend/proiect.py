from flask import Flask, render_template, request
from Backend.BiancaCrawler import Search

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("interfata.html")


@app.route('/', methods=['POST'])


def getValue():
    name = request.form['fname']
    dates = Search.searchAWorld(name)
    records = Search.categories(dates)
    return render_template("interfata.html", dates=dates, records=records)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=10)
