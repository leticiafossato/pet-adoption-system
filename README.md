# pet-adoption-system

Slides:
https://drive.google.com/file/d/1r4Yz2EtTEtVsi5UT_zQWrkVkfXpbvsAm/view?usp=sharing




<p align="center">
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/bBzdVnN/patah.jpg" alt="patah" border="0"></a>
</p>
<h1 align="center">🧹 Final Project | Pet Adoption System</h>

## Project Status
👣 In progress

## Table of Contents:

- [Objective](#Objective)
- [Motivation](#motivation)
- [Process](#process)
- [Results](#results)
- [Learning Process](#learning-process)
- [Author](#Author)

## Objective
Create an app to recommend animals (cats and dogs). This system will always recommend the ten pets which low probability of adoption.
The idea here is to make partnetship with ONGs, but for now, was developed only a prototype of the system using a Kaggle dataset <a href="https://www.kaggle.com/c/petfinder-adoption-prediction">PetFinder.my Adoption Prediction</a>.

### Motivation
There are 170 thousand of abandoned animals under ONGs care in Brazil, and a lot of people only adopt looking for the appearence.<br>
The proposal here is to suggest animal that in most part of times are not even looked.<br>

## Process
1. Create a baseline to find the best model;
2. Use pipeline to create the final model;
3. Filter the dataset to create the search from user;
4. Order the results by percentage;
5. Create the app using streamlit.


## Results 
You can check the slides <a href="https://drive.google.com/file/d/1r4Yz2EtTEtVsi5UT_zQWrkVkfXpbvsAm/view?usp=sharing">here</a>.

## Learning Process
### Theory Applied
- [x] Pandas <br>
- [x] Numpy<br>
- [x] Target Encoder<br>
- [x] Standard Scaler<br>
- [x] Logistic Regression<br>
- [x] ROC Score <br>
- [x] YellowBrick<br>
- [x] Decision Tree Classifier<br>
- [x] Pipelines<br>
- [x] JobLib<br>
- [x] Streamlit<br>


### Challenges
- Find a good model to predict the probabilities;

### Improvements
- Load the site into Heroku;
- Build a dataset using data from a Brazilian ONG;
- Improve streamlit design;
- Implement a search by image;

### Thanks
André Aguiar
Yuri Felix Guimarães

## Author
Letícia Fossato
