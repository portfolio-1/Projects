import pickle
from flask import Flask, request, jsonify, render_template

# load model
model = pickle.load(open('Bank_loan_analysis.pickle','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((X, [y]) for X, y in data.items())
    data_df = pd.DataFrame.from_dict(application_data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)