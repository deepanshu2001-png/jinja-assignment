from flask import Flask, redirect, render_template
import datetime
app = Flask(__name__)

def date():
    dateObject= datetime.datetime.now()
    return dateObject
def end_suffix():
    dateTime=date()
    day =int(dateTime.strftime("%d"))
    if 4 <= day <= 20 or 24 <= day <= 30:
        end_suffix = "th"
    else:
        end_suffix = ["st", "nd", "rd"][day % 10 - 1]
    return end_suffix
def image():
    return "https://i.pravatar.cc/300"

def randomimage():
    return "https://picsum.photos/"

def todayDate():
    dateTime=date()
    return {
        "year": dateTime.year,
        "month": dateTime.strftime("%b"),
        "day": dateTime.strftime("%d"),
        "suffix": end_suffix(),
        "image": image(),
    }
@app.route("/jinjatemplate")
def home():
    todayDate1=todayDate()
    return render_template('index.html', Heading_h1 = 'Sample Page', todayDate1=todayDate1)

@app.route('/image')
def getRandom():
    return redirect('/jinjatemplate')

app.run(debug=True)

