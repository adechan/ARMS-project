from flask import Flask, render_template, request
from Backend.BiancaCrawler import Search, Rank
import json

app = Flask(__name__)

dates = None
records = None

@app.route("/")
def main():
    return render_template("interfata.html")

@app.route('/rank', methods=['POST'])
def rank():
    categoryName = request.form['categories']
    print("category name: " + categoryName)

    if dates is None:
        datelist = Search.searchAWord('coronavirus')
    else:
        datelist = dates

    if records is None:
        recordslist = Search.categories(datelist)
    else:
        recordslist = records

    rankings = Rank.sort(datelist, recordslist, categoryName)

    print(f'{len(rankings)} rankings saved')

    return render_template("interfata.html", dates=datelist, records=recordslist, rankings=rankings)

@app.route('/', methods=['POST'])
def getValue():
    name = request.form['fname']
    global dates
    global records

    # with open('dates.json', 'r') as datesFile:
    #     dates = json.load(datesFile)
    #
    # with open('records.json', 'r') as recordsFile:
    #     records = json.load(recordsFile)

    dates = Search.searchAWord(name)
    print('dates loaded')

    records = Search.categories(dates)
    print(f'records loaded')

    #
    # print(f'{len(dates)} dates saved')
    #
    # print(f'{len(records)} records saved')

    return render_template("interfata.html", dates=dates, records=records)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=10)
