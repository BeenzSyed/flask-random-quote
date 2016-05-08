from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2016-04/28/12/enhanced/webdr12/enhanced-29129-1461860373-8.jpg?no-auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2016-04/30/14/enhanced/webdr01/enhanced-24273-1462041310-2.png?no-auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2016-04/27/10/enhanced/webdr05/enhanced-14286-1461768299-1.jpg?no-auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2016-04/27/10/enhanced/webdr06/enhanced-21513-1461767619-8.jpg?no-auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2016-04/27/10/enhanced/webdr07/enhanced-26588-1461767482-2.jpg?no-auto"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
