import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'CRIM': float(request.form['CRIM']),
        'ZN': float(request.form['ZN']),
        'INDUS': float(request.form['INDUS']),
        'RM': float(request.form['RM']),
        'PTRATIO': float(request.form['PTRATIO']),
        'LSTAT': float(request.form['LSTAT'])
    }
    final_input = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(final_input)
    return render_template('home.html', prediction_text="The House Price Prediction is ${:.2f}".format(output[0]))


if __name__ == "__main__":
    app.run(debug=True)
