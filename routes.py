from flask import Flask, jsonify, request
import plan

app = Flask(__name__)

@app.route('/fetch_plan', methods=['GET'])
def fetch_plan():
    intolerances = request.args.get('intolerances', None)
    return plan.process_recipes(intolerances)


if __name__ == "__main__":
    app.run(debug=True)