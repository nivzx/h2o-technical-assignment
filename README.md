# H2O.ai Technical Assesment

## Introduction

This is an app built using H2O wave, with H2O's DeepLearning models. It is an app for predicting if patients are vulerable for future heart diseases based on their current medical data

I uses [this dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) with more than 1000 datapoints for training and validation of the model.
I used [Google Colab](https://colab.research.google.com/drive/14E5uij9zbBW1TdRGGLkAAl-yFF0EeejJ?usp=sharing) for training the model, using H2O's deep learning tools.

You can watch a small go through of the application in below video

[![IMAGE ALT TEXT HERE](https://images.squarespace-cdn.com/content/v1/5daddb33ee92bf44231c2fef/60533e7f-5ab0-4913-811c-9a4c56e93a5c/AI-in-healthcare2.jpg)](https://youtu.be/JtG0GZEk6_k?si=EvmPj7XGs0Kh0AaE)

## Running the app

Make sure you have activated a Python virtual environment with `h2o-wave` installed.

If you haven't created a python env yet, simply run the following command (assuming Python 3.7 is installed properly).

For MacOS / Linux:

```sh
python3 -m venv venv
source venv/bin/activate
pip install h2o-wave
```

For Windows:

```sh
python3 -m venv venv
venv\Scripts\activate
pip install h2o-wave
```

Once the virtual environment is setup and active, run:

```sh
wave run app.py
```

Which will start a Wave app at <http://localhost:10101>.

## Interactive examples

If you prefer learning by doing, you can run `wave fetch` command that will download all the existing small Python examples that show Wave in action. The best part is that all these examples are interactive, meaning you can edit their code directly within the browser and observe the changes.

## Learn More

To learn more about H2O Wave, check out the [docs](https://wave.h2o.ai/).
