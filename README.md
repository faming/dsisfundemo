# Iris Species Prediction Web App
## Flask web app which predicts the species of Iris flower.

## Introduction 

It uses 3 trained ML models - 
1. Logistic Regression
2. K Nearest Neighbours
3. SVM

These models have been trained on my local machine and saved using pickle library in Python. Then the saved models are called using Flask.

BulmaCSS is used for the frontend.

## Requirements
1. flask
2. scikit-learn
3. pandas
4. numpy

## Instructions
> python app.py

## Docker commands
docker image build -t iris:app .

docker run -p 5000:5000 iris:app

docker system prune

# dsisfundemo
