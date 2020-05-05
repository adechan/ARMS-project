import nltk
from nltk.corpus import stopwords
import json
import datetime
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

# get top 3 words met in a category
def sort(dates, records, categoryName):
    print(f'{len(dates)} dates loaded')
    # print(f'{len(records)} records loaded')
    # records: [(string, category, article_title, date)]

    datetimeEnd = datetime.datetime.now()
    datetimeStart = datetimeEnd - datetime.timedelta(weeks=20)

    clean_tokens = []
    count = 0
    important_news = dict()

    for data in dates:
        # print(data)
        if data[1] != categoryName:
            continue
        print(data[1])
        date = data[3].replace('.', '')
        date = date.replace('Sept', 'September')
        date = date.replace('Oct', 'October')
        # print(data)
        try:
            # print(data)
            date = datetime.datetime.strptime(date, '%B %d, %Y')
            # print(data)
            if datetimeStart < date < datetimeEnd:
                print(f'{data[2]}: {date}')
                # tokens = [t for t in data[2].split()]

                # print(tokens)
                words = nltk.word_tokenize(data[2])
                tokens = list(filter(lambda token: token not in string.punctuation, words))

                tagger = nltk.pos_tag(tokens)

                for token in tagger:
                    print(token)
                    if token[0] not in stopwords.words('english') and (token[1] != "ADJ" and token[1] != "ADP" and
                            token[1] != "CONJ" and token[1] != "DET" and token[1] != "NUM" and token[1] != "PRT" and
                            token[1] != "PRON" and token[1] != "VERB" and token[1] != "DT" and token[1] != "IN" and
                            token[1] != "CC" and token[1] != "PRP$" and token[1] != "RB" and token[1] != "VBZ" and
                            token[1] != "PRP" and token[1] != "VRD" and token[1] != "VBD" and token[1] != "JJ" and
                            token[1] != "WRB" and token[0] != "’" and token[0] != "‘" and token[0] != "Are" and
                            token[0] != "What" and token[0] != "Has" and token[1] != "WP" and token[1] != "VBP"
                            and token[1] != "VBN" and token[1] != "PDT" and token[1] != "TO" and token[0] != "No"
                            and token[1] != "NN" and token[0] != "Been" and token[0] != "Met"
                            ):
                        clean_tokens.append(token[0])
        except ValueError as e:
            print(e)

    for token in clean_tokens:
        if token not in important_news:
            count = 1
            important_news[token] = count
        else:
            count = count + 1
            important_news[token] = count

    sorted_news = list(important_news.items())
    sorted_news.sort(key=lambda x: x[1], reverse=True)
    print(sorted_news)

    final_list = []
    for element in sorted_news:
        final_list.append(element[0])
        print(element[0])

    print(f"final list: {final_list}")
    return final_list[0:3]

if __name__ == "__main__":
    with open('../../Frontend/dates.json', 'r') as datesFile:
        dates = json.load(datesFile)

    with open('../../Frontend/records.json', 'r') as recordsFile:
        records = json.load(recordsFile)

    sort(dates, records, "Politics")