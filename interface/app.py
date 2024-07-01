from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
MODEL_PATH = '../model.pkl'
model = joblib.load(MODEL_PATH)

# Define the list of column names globally
columns = ['radius_mean', 'texture_mean', 'perimeter_mean',
           'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
           'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
           'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
           'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
           'fractal_dimension_se', 'radius_worst', 'texture_worst',
           'perimeter_worst', 'area_worst', 'smoothness_worst',
           'compactness_worst', 'concavity_worst', 'concave points_worst',
           'symmetry_worst', 'fractal_dimension_worst']

@app.route('/')
def home():
    return render_template('index.html', columns=columns)

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from form
    # Initialize an empty list to store the input values
    inputs = []

    # Loop through the column names
    for column in columns:
        # Retrieve the value of the input field from the form
        input_value_str = request.form[column]
        
        # Check if the input value is empty
        if len(input_value_str) == 0:
            # Assign a default value of 0 if the input value is empty
            input_value_float = 0.0
        else:
            # Convert the input value to float
            input_value_float = float(input_value_str)
        
        # Append the converted input value to the list of inputs
        inputs.append(input_value_float)
    
    # Print the inputs to the console
    print("User Inputs: \n", inputs)

    # Make prediction
    prediction = model.predict([inputs])

    # Return prediction as a response
    return f'Prediction: {prediction}'
    #return f'Inputs: {inputs}'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
