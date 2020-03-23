from flask import Flask, render_template      
import scraper

app = Flask(__name__)

consoles = scraper.GetConsoles()
print(consoles)

#Get average price
average = scraper.AveragePrice(consoles)

@app.route("/")
def home():
    return render_template("home.html", len1 = len(consoles)-1, list1 = consoles, average = average)

if __name__ == "__main__":
    app.run(debug=True)