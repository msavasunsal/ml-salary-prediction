import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Ensuring all form data is converted to integer
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # Converting prediction result to integer for display
    output = int(prediction[0])

    return render_template('index.html', prediction_text=f'Predicted Employee Salary: ${output}')

if __name__ == "__main__":
    app.run(debug=True)
