from flask import Flask, request, jsonify
import h2o
from h2o.estimators import H2ODeepLearningEstimator

# Initialize Flask app
app = Flask(__name__)

# Load the H2O MOJO model
model_path = "https://h2o-tech-assignment.s3.amazonaws.com/model/heart_failure_dl_model.zip"  # Provide the path to your MOJO file
h2o.init()
model = h2o.import_mojo(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from request
        data = request.json

        # Format input data into H2O frame
        h2o_df = h2o.H2OFrame(data)

        categorical_cols = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
        for col in categorical_cols:
            h2o_df[col] = h2o_df[col].asfactor()

        # Make predictions
        predictions = model.predict(h2o_df)

        # Check the structure of predictions
        print(predictions)

        # Convert predictions to list
        if isinstance(predictions, h2o.H2OFrame):
            predictions_list = h2o.as_list(predictions)
        else:
            return jsonify({'error': 'Unexpected prediction format'}), 400

        return jsonify({'predictions': predictions_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)