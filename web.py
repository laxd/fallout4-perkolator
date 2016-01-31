from flask import Flask
from flask import render_template
from flask import jsonify
from attribute import Attribute
from perks import Perk
import perk_utils

app = Flask(__name__)

@app.route('/')
def show_perks():
    return render_template("perks.html",
            perks=perk_utils.perks,
            attributes=[a for a in Attribute])

@app.route('/get-suggestion', methods=["POST"])
def get_suggestion():
    print("Received get-suggestion request!")

    suggestions = perk_utils.get_suggestion(perk_utils.attributes, [])

    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
