from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    line1 = "Logic will get you from A to B. Imagination will take you anywhere."
    line2 = "There are 10 kinds of people. Those who know binary and those who don't"
    line3 = "There are two ways of constructing a software design. One way is to make it so simple that there are " + \
            "obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies."
    line4 = "It's not pitch dark. You are likely to be eaten by a grue"
    line5 = "It's not that I'm so smart, it's just that I stay with problems longer."
    sentenceList = [line1, line2, line3, line4, line5]

    return render_template('index.html', sentence=sentenceList[random.randint(0,4)])


if __name__ == '__main__':
    app.run()
