#Streamlit Libraries
import streamlit as st
import pandas as pd
import numpy as np 
import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform
from PIL import Image

#Streamlit Option
st.set_option('deprecation.showfileUploaderEncoding', False)

#Display all columns
pd.set_option('display.max_columns', None)

#Pipeline
pipeline = joblib.load('../model-v2.pkl')
df_model = pd.read_csv('../final_dataset/train.csv')
X_model = df_model[['Type', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2','Color3', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed','Sterilized', 'Health', 'State', 'Fee_y']]
y_model = df_model['NonAdopted']
pipeline.fit(X_model, y_model)

#Import Breed Dictionary
breed_labels = pd.read_csv('../BreedLabels.csv')

#Import Colors Dictionary
color_labels = pd.read_csv('../ColorLabels.csv')

#Import State Dictionary
state_labels = pd.read_csv('../StateLabels.csv')

#Dictionary
my_dict = {state_labels.iloc[i,0]: state_labels.iloc[i,1] for i in range(len(state_labels['StateName']))}
my_dict_breed = {breed_labels.iloc[i,0]: breed_labels.iloc[i,2] for i in range(len(breed_labels['BreedName']))}
my_dict_gender = {1: 'Male', 2: 'Female', 3: 'Mixed'}
my_dict_color = {color_labels.iloc[i,0]: color_labels.iloc[i,1] for i in range(len(color_labels['ColorName']))}
my_dict_maturity = {1: 'Small', 2: 'Medium', 3: 'Large', 4: 'Extra Large', 0: 'Not Specified'}
my_dict_length = {1: 'Short', 2: 'Medium', 3: 'Long', 0: 'Not Specified'}
my_dict_vaccinated = {1: 'Yes', 2: 'No', 3: 'Not Sure'}
my_dict_dewormed = {1:'Yes', 2:'No', 3:'Not Sure'}
my_dict_sterilized = {1:'Yes', 2:'No', 3:'Not Sure'}
my_dict_health = {1:'Healthy', 2:'Minor Injury', 3:'Serious Injury', 0:'Not Specified'}
my_dict_fee = {0:'Free', 1:'Not Free'}
my_dict_type = {1:'Dog', 2:'Cat'}

#Functions:
def ong():
	st.title('Pet Adoption System')
	st.header('Welcome to ONGs Space! 🐾')
	st.subheader('• How it Works?')
	st.write("Here you can upload your pet's dataset to discover which of your pets have less chance to be adopted.")
	st.subheader('• What my file should have?')
	st.write('Your file should contain the following information: Type (Cat or Dog), Age, Breed (if have one or two), Gender, Colors, Maturity, Length, Vaccinated or not, Derwormed, Sterilized or not, Healthy or not, if the adoption have some tax or not, and what is the state that your ONG.')
	#st.write('Our mission is to give the same chances for all the animals.')
	st.subheader('• What I should do with these information?')
	st.write('After discover which pets have low chances to be adopted, you could improve your marketing campaign to increse their chances. Also, this site is created to help you with this process. How? Putting these pets in spotlight, for all people which comes search for a friend here.')
	st.subheader('• I will need to pay for it?')
	st.write("No, this service it's offered for free.")
	#Upload the file
	st.subheader("Let's start?")
	file = st.file_uploader('Insert your database • here:',type=['csv']) 

	#File not None
	if file is not None:
		df = pd.read_csv(file)
		st.write(df)
	
	#Probability of file uploaded
		X= df[['Type', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2','Color3', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed','Sterilized', 'Health', 'State', 'Fee_y']]
		P_non_adopt = pipeline.predict_proba(X)[:,1]
		df['P_non_adopt'] = P_non_adopt
		df.sort_values(['P_non_adopt'], ascending = False, inplace = True)

	#Renaming columns

		df = df.replace({'State':my_dict,'Breed1':my_dict_breed ,'Breed2':my_dict_breed, 'Gender':my_dict_gender, 'Color1':my_dict_color, 
                'Color2':my_dict_color,'Color3':my_dict_color,'State':my_dict, 'MaturitySize':my_dict_maturity,
               'FurLength':my_dict_length, 'Vaccinated':my_dict_vaccinated, 'Dewormed':my_dict_dewormed,
               'Sterilized':my_dict_sterilized, 'Health':my_dict_health})
	
	#Filtro df_cat
		df_cat = df[df['Type']==2]

	#Filtro df_dog
		df_dog = df[df['Type']==1]

		st.header('You should give a special attention to:')

		for a,i in zip(df.head(10).index,range(1,11)):
			try:
				st.subheader(f'{i}')
				image = Image.open(f'../test_images/{df["Photo"][a]}.jpg')
				st.image(image, caption=f'{df["Name"][a]}',width=300)
				st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
				st.write('Sterilized:',df["Sterilized"][a])	
				st.write('Gender:',df["Gender"][a])	
				st.write('Age:',df["Age"][a],'months')	
				st.write('State:',df["State"][a])	
				st.write('Description:',df["Description"][a])
				st.write('\n')
			except:
				if df["Breed2"][a]==0:
					x = 'None'
				else:
					x = df["Breed2"][a]
				st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
				st.write('Sterilized:',df["Sterilized"][a])	
				st.write('Gender:',df["Gender"][a])		
				st.write('Age:',df["Age"][a],'months')	
				st.write('State:',df["State"][a])	
				st.write('Description:',df["Description"][a])
				st.write('\n')

def adopter():
	df= pd.read_csv('../final_dataset/test.csv')
	st.title("Pet Adoption System")
	st.header("Searching for a pet?🐾")
	st.write("Here you can meet your best friend, according to your preferences.")
	st.write ("Attention: Before adopting a dog, reflect if - do you have time to care for it? Are you or someone in your family allergic to animals? Do you have the financial means to provide the necessary care?")
	st.subheader("Let's start? Please select your options:")
	X= df[['Type', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2','Color3', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed','Sterilized', 'Health',  'State', 'Fee_y']]
	from scipy.spatial.distance import pdist
	X_example = pd.DataFrame({'Type': [1],
           'Breed1': [307],
           'Breed2': [0],
           'Gender' : [2],
           'Color1': [1],
           'Color2': [0],
           'Color3':[0],
           'MaturitySize': [2],
           'FurLength':[1],
           'Vaccinated': [1],
           'Dewormed': [1],
           'Sterilized': [2],
           'Health': [1],
           'Quantity': [1],
           'State': [41326],
           'Fee_y': [0],
           }, 
           )
	type_choice1 = st.radio('Type:',['Dog','Cat'])
	if type_choice1=='Dog':
		X_example['Type']=1
		#st.write(X_example) 
	if type_choice1=='Cat':
		X_example['Type']=2
		#st.write(X_example)

	type_choice2 = st.radio('Gender:',['Male','Female'])
	if type_choice2=='Male':
		X_example['Gender']=1
		#st.write(X_example) 
	if type_choice2=='Female':
		X_example['Gender']=2
		#st.write(X_example)

	type_choice3 = st.radio('Size:',['Small','Medium','Large','Extra Large'])
	if type_choice3=='Small':
		X_example['MaturitySize']=1
		#st.write(X_example) 
	if type_choice3=='Medium':
		X_example['MaturitySize']=2
		#st.write(X_example)
	if type_choice3=='Large':
		X_example['MaturitySize']=3
		#st.write(X_example)
	if type_choice3=='Extra Large':
		X_example['MaturitySize']=4
		#st.write(X_example)

	button = st.button('Search')
	if button:
		X= df[['Type', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2','Color3', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed','Sterilized', 'Health', 'State', 'Fee_y']]
		P_non_adopt = pipeline.predict_proba(X)[:,1]
		df['P_non_adopt'] = P_non_adopt
		df.sort_values(['P_non_adopt'], ascending = False, inplace = True)
		X_results = df.copy()
		filtered = X_results[(X_results['Type']==(int(X_example['Type'])))&(X_results['Gender']==(int(X_example['Gender'])))&(X_results['MaturitySize']==(int(X_example['MaturitySize'])))]
		filtered.head(10)
		filtered.loc[filtered.Name.isna(),'Name'] = 'No Name'
		#st.write(list(filtered.index))

		if list(filtered.index)==[]:
			filtered2 = X_results[(X_results['Type']==(int(X_example['Type'])))]
			st.header("We don't have any pet with this features.")
			st.subheader("Please, take a look on these:")
			for a,i in zip(filtered2.head(3).index,range(1,4)):
				try:
					st.subheader(f'{i}')
					image = Image.open(f'../test_images/{df["Photo"][a]}.jpg')
					st.image(image, caption=f'{df["Name"][a]}',width=300)
					st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
					st.write('Sterilized:',df["Sterilized"][a])	
					st.write('Gender:',df["Gender"][a])	
					st.write('Age:',df["Age"][a],'months')	
					st.write('State:',df["State"][a])	
					st.write('Description:',df["Description"][a])
					st.write('\n')
				except:
					if df["Breed2"][a]==0:
						x = 'None'
					else:
						x = df["Breed2"][a]
					st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
					st.write('Sterilized:',df["Sterilized"][a])		
					st.write('Age:',df["Age"][a],'months')	
					st.write('Description:',df["Description"][a])
					st.write('\n')

		else:

		#st.write(filtered.head(10))

			df = df.replace({'State':my_dict,'Breed1':my_dict_breed ,'Breed2':my_dict_breed, 'Gender':my_dict_gender, 'Color1':my_dict_color, 
	        'Color2':my_dict_color,'Color3':my_dict_color,'State':my_dict, 'MaturitySize':my_dict_maturity,
	       'FurLength':my_dict_length, 'Vaccinated':my_dict_vaccinated, 'Dewormed':my_dict_dewormed,
	       'Sterilized':my_dict_sterilized, 'Health':my_dict_health})
			st.header('What about?')
			for a,i in zip(filtered.head(10).index,range(1,11)):
				try:
					st.subheader(f'{i}')
					image = Image.open(f'../test_images/{df["Photo"][a]}.jpg')
					st.image(image, caption=f'{df["Name"][a]}',width=300)
					st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
					st.write('Sterilized:',df["Sterilized"][a])	
					st.write('Gender:',df["Gender"][a])	
					st.write('Age:',df["Age"][a],'months')	
					st.write('State:',df["State"][a])	
					st.write('Description:',df["Description"][a])
					st.write('\n')
				except:
					if df["Breed2"][a]==0:
						x = 'None'
					else:
						x = df["Breed2"][a]
					st.write('Breed1, Breed2:',df["Breed1"][a],',',x)
					st.write('Sterilized:',df["Sterilized"][a])		
					st.write('Age:',df["Age"][a],'months')	
					st.write('Description:',df["Description"][a])
					st.write('\n')

		#X_results = X.copy()
		#X_results['score'] = pipeline['modelling'].predict_proba(X_results)[:, 1]

		#concatted = pd.concat([X_example, X]).reset_index(drop=True)
		#concatted2 = concatted[(concatted['Type']==(int(X_example['Type'])))&(concatted['Gender']==(int(X_example['Gender'])))&(concatted['MaturitySize']==(int(X_example['MaturitySize'])))]
		#index = pd.DataFrame(squareform(pdist(concatted2, p=1)), columns=concatted2.index, index=concatted2.index).iloc[:, 0].sort_values().head(11).index
		#Z = concatted2.loc[index].drop(0)
		#Z.drop(columns='Quantity', inplace=True)
		#Z['score'] = pipeline['modelling'].predict_proba(Z)[:, 1]
		#sug = Z.sort_values(by='score', ascending = False).drop(columns='score')

		#sug = X_results.loc[index].sort_values(by='score', ascending = False)

		#sug2 = sug.replace({'Breed1':my_dict_breed ,'Breed2':my_dict_breed, 'Gender':my_dict_gender, 'Color1':my_dict_color, 
		#                'Color2':my_dict_color,'Color3':my_dict_color,'State':my_dict, 'MaturitySize':my_dict_maturity,
		#               'FurLength':my_dict_length, 'Vaccinated':my_dict_vaccinated, 'Dewormed':my_dict_dewormed,
		#               'Sterilized':my_dict_sterilized, 'Health':my_dict_health, 'Type':my_dict_type})

		#st.write(sug2)


def petsinfo():
	st.title('Having daughts about your choice?')

	st.header("Qual o gasto médio com pets?")

	st.subheader('• Gasto médio com cães:')
	st.write("O gasto médio com cães no Brasil é de R$ 338,76, segundo o IPB (Instituto Pet Brasil). Esse custo varia conforme o tamanho do bicho. Cães pequenos (até 10 kg) custam R$ 266,18 ao mês; os médios (de 11 kg a 25 kg) consomem R$ 327,51, e os grandes (mais de 26 kg) geram gasto mensal de R$ 422,59")
	st.subheader('• Gasto médio com gatos:')
	st.write("O custo mensal médio para ter um gato é de R$ 196,56, segundo o IPB.")

	st.write("Souce: ValorInveste.globo.com")

	
	st.header("Quais as principais caracteristicas de cada raça?")
	st.subheader('Breed1:')
	st.write('bla bla bla')
	

#Sidebar
st.sidebar.title("Searching for a friend?")
radio = st.sidebar.radio(label="Who are you?", options=["ONG", "Adopter", "+Pets Info"])

#st.sidebar.subheader("Thank's for coming!")

image = Image.open('../Streamlit/pegada.png')
st.sidebar.image(image, caption='',width=50)
st.sidebar.write("Status: In construction...🔨")
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("Suggestions? Please contact me on:")
st.sidebar.write("Linkedin: leticiafossato")

if radio == "ONG":
	ong()

if radio == "Adopter":
	adopter()

if radio == "+Pets Info":
	petsinfo()