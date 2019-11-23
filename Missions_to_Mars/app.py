from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_all


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars_data= mongo.db.mars.find_one()
    return render_template("index.html",mars=mars_data)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_info = scrape_all()
    mars.update({}, mars_info, upsert = True)
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)
