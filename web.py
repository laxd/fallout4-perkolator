from flask import Flask
from flask import render_template
from attribute import Attribute
import perks

app = Flask(__name__)

@app.route('/')
def show_perks():
    all_perks = perks.get_all_perks()
    attributes = [a for a in Attribute]
    return render_template("perks.html", perks=all_perks, attributes=attributes)

if __name__ == '__main__':
    app.run(debug=True)
