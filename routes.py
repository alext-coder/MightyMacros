from flask import Flask, jsonify, request
import plan
import json

app = Flask(__name__)

@app.route('/fetch_meal_plan', methods=['GET'])
def fetch_meal_plan():
    intolerances = request.args.get('intolerances', None)
    meal_type = request.args.get('type', None)
    return json.dumps(plan.process_recipes(intolerances, meal_type)[0])

@app.route('/fetch_day_plan', methods=['GET'])
def fetch_day_plan():
    intolerances = request.args.get('intolerances', None)
    return plan.process_day(intolerances)




if __name__ == "__main__":
    app.run(debug=True)