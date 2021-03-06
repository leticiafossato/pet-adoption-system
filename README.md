<p align="center">
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/bBzdVnN/patah.jpg" alt="patah" border="0"></a>
</p>
<h1 align="center">Pet Adoption System </h>
<h2 align="center">IronHack Final Project</h>

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
Create an app to recommend animals (cats and dogs). This system will always recommend the ten pets which have low probability of adoption.<br>
The idea here is to make partnership with ONGs, but for now, was developed only a prototype of the system using a Kaggle dataset <a href="https://www.kaggle.com/c/petfinder-adoption-prediction">PetFinder.my Adoption Prediction</a>.

## Motivation
There are 170 thousand of abandoned animals under ONGs care in Brazil, and a lot of people only adopt looking for their appearence.<br>
The proposal here is to suggest animals that in most part of times aren't even looked.<br>

## Process
1. Create a baseline to find the best model;
2. Use pipeline to create the final model;
3. Filter the dataset to create the search from user;
4. Order the results by percentage;
5. Create the app using streamlit.


## Results 

### Streamlit
Link of app: *pendent, to add*<br>
Demo video  *pendent, to add*<br>

### Slides
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
- Improve the model (considering images and descriptions);
- Build a dataset using some Brazilian ONG information;
- Improve streamlit design;
- Implement a search by image;
- Load the site into Heroku;

### Thanks
A special thanks for IronHack teachers, who helped me a lot during the development of project.<br>
<a href="https://github.com/aguiarandre">André Aguiar</a><br>
Yuri Felix Guimarães

## Author
Letícia Fossato
