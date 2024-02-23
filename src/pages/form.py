import h2o

from h2o_wave import Q, ui

from helpers.card_helpers import add_card


def display_form(q: Q):
    add_card(q, 'form', create_form())


def create_form():
    form = ui.form_card(box='horizontal', items=[
        ui.text('Enter Patient Information', size='m'),
        ui.textbox(name='age', label='Age (years)', required=True),
        ui.combobox(name='sex', label='Sex', choices=[
            'Male',
            'Female'
        ], required=True),
        ui.combobox(name='chest_pain_type', label='Chest Pain Type', choices=[
            'Typical Angina',
            'Atypical Angina',
            'Non-Anginal Pain',
            'Asymptomatic'
        ], required=True),
        ui.textbox(name='resting_bp', label='Resting Blood Pressure (mm Hg)', required=True),
        ui.textbox(name='cholesterol', label='Serum Cholesterol (mm/dl)', required=True),
        ui.textbox(name='fasting_bs', label='Fasting Blood Sugar (mg/dl)', required=True),
        ui.combobox(name='resting_ecg', label='Resting ECG Results', choices=[
            'Normal',
            'ST-T Wave Abnormality',
            'Left Ventricular Hypertrophy'
        ], required=True),
        ui.textbox(name='max_hr', label='Maximum Heart Rate Achieved', required=True),
        ui.combobox(name='exercise_angina', label='Exercise-Induced Angina', choices=[
            'Yes',
            'No'
        ], required=True),
        ui.textbox(name='oldpeak', label='Oldpeak (ST Depression)', required=True),
        ui.combobox(name='st_slope', label='ST Slope', choices=[
            'Upsloping',
            'Flat',
            'Downsloping'
        ], required=True),
        ui.buttons([
            ui.button(name='submit_button', label='Submit', primary=True),
        ])
    ])
    return form

async def handle_interaction(q: Q):
  try:
    age = int(q.args.age)
    sex = 'M' if q.args.sex == 'Male' else 'F'
    chest_pain_type_map = {'Typical Angina': 'TA', 'Atypical Angina': 'ATA', 'Non-Anginal Pain': 'NAP', 'Asymptomatic': 'ASY'}
    chest_pain_type = chest_pain_type_map[q.args.chest_pain_type]
    resting_bp = float(q.args.resting_bp)
    cholesterol = float(q.args.cholesterol)
    fasting_bs = 1 if int(q.args.fasting_bs) == 120 else 0
    resting_ecg_map = {'Normal': 'Normal', 'ST-T Wave Abnormality': 'ST', 'Left Ventricular Hypertrophy': 'LVH'}
    resting_ecg = resting_ecg_map[q.args.resting_ecg]
    max_hr = float(q.args.max_hr)
    exercise_angina = 'Y' if q.args.exercise_angina == 'Yes' else 'N'
    oldpeak = float(q.args.oldpeak)
    st_slope_map = {'Upsloping': 'Up', 'Flat': 'Flat', 'Downsloping': 'Down'}
    st_slope = st_slope_map[q.args.st_slope]
  except ValueError:
    print("Error: One or more form fields contain invalid data.")
    return
  
  # Create H2OFrame
  try:
      # Initialize H2O
      h2o.init()
      # Create H2OFrame
      data = {
          'Age': [age],
          'Sex': [sex],
          'ChestPainType': [chest_pain_type],
          'RestingBP': [resting_bp],
          'Cholesterol': [cholesterol],
          'FastingBS': [fasting_bs],
          'RestingECG': [resting_ecg],
          'MaxHR': [max_hr],
          'ExerciseAngina': [exercise_angina],
          'Oldpeak': [oldpeak],
          'ST_Slope': [st_slope]
      }
      h2o_frame = h2o.H2OFrame(data)
      h2o.connect(ip='localhost', port=54321)
    
      model = h2o.import_mojo('https://h2o-tech-assignment.s3.amazonaws.com/model/heart_failure_dl_model.zip')

      prediction = model.predict(h2o_frame)

      vulnerable_to_heart_disease = prediction[0, 'predict'] == 1

      # Display card based on prediction
      if vulnerable_to_heart_disease:
          q.page['result'] = ui.markdown_card(
              box='vertical',
              title='Heart Disease Prediction',
              content="You are vulnerable to heart diseases."
          )
      else:
          q.page['result'] = ui.markdown_card(
              box='vertical',
              title='Heart Disease Prediction',
              content="You are not vulnerable to heart diseases."
          )

      

  except Exception as e:
      print(f"Error: {e}")
  finally:
      pass



    

