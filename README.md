# Immo Eliza - Price prediction for Belgian Real Estate market


## Author

Vitaly Shalem [LinkedIn](https://www.linkedin.com/in/vitaly-shalem-26aab265/) | [GitHub](https://github.com/vitaly-shalem).


## Objectives

Immo Eliza is a multi stage project @ [BeCode.org](www.becode.org).

THe purpose of the project to create an app that can estimate a real estate property sale price targeting Belgian market. 

The project consists of the follwoing stages:

1. Data collection (Done in a group)
2. Data processing and analysis
3. Model training
4. Deployment

Each stage explained below in more details.


### General usage and installation

Regardless of the project stage, the following steps has to be done to use the code:

- Clone this repository to your local machine
- Create virtual enviroment
- Install required libraries by running `pip install requiremnets.txt`

Stage sections contain **Usage** steps specific for each stage.


### Repository structure and content

The repository and its content are organized as follws:

- data: Data files
- doc: Documents
- models: Model files, as well as, *transformer* and *scaler* files
- notebooks:
    - data-exploration: Data exploration and analysis notebooks
    - deployment: Deployment related notebooks
    - model-building: Model building and data preparaation and conversion notebooks
- output:
    - data-exploration: Data related output files (visuals, tables, etc.)
    - model-building: Model related output filers (experiments overviews, results tables, etc.)
- src: py source files
- root files:
    - .gitignore
    - app.py
    - main.py
    - README.md
    - requirements.txt


## Stage 1: Data collection

Data collection was a group activity and the first stage of the project.

See more details in [Immo Eliza - Data Scraper](https://github.com/vitaly-shalem/ImmoEliza-DataScraper) repository.


## Stage 2: Data processing and analysis

### Description

This stage of a Real Estate project meant to consolidtae the knowledge about data handling and data analysis by using Pandas and visualisation libraries (Matplotlib and/or Searborn).


### Data

The data was obtained during Stage 1 of the project. See the link to the repo above.


## Stage 3: Model training

### Description

This stage of the project is to train and test the Machine Learning models for prediction property price for Belgian Real Estate market.


### Challenge

Learn about Machine Learning and implement the model/s training pipeline:
- Data preparation
- Data conversion to the formats required by ML
- Model traininf and testing


### Data

The data shape was take from the deliverables of Data analsysis (Satge 2).


### Usage

After the steps described above in **General usage and installation**:

- Run the pipeline by running `python main.py`
- Pipeline:
    - Data preparation
    - Data conversion
    - Model training


## Stage 4: Deployment

### Description

The deployment is done with **FastAPI**.

The app requests information for a new property in `json` format.

The entered information is checked and if it is insufficient or there are some errors, the error message is presented.

Once the information is correctly entered, the app continued to the 2 main steps:

- Data preprocessing
- Prediction with the model

The results are delivered in `json` format.


### Usage

After the steps described above in **General usage and installation**, follow the following steps to test model deployment:

- Open `Git bash` and navigate to project folder
- Run `uvicorn app:app --reload`
- Open browser and enter `http://127.0.0.1:8000/` in the Address bar
    - This is a Welcome page
- Enter `http://127.0.0.1:8000/docs` in the Address bar to navigate to **FastAPI** documentation page
- Oped `\predict` bar and press `Try it out` button
- Edit the `json` data to enter your inforamtion about a real estate property
    - Please, follow the hints presented in `json`
    - Make sure to erase the redundant information
- Hit the `Execute` button
- Scroll down to check for server response, where the following can be found:
    - The **error messages** in case of problematic input
        - In this case, go back edit the information accordingly and hit `Execute` again
    - The **predicted price**:
        - Please, note! The price is rounded to thousands to ease the understanding
- All server responses are in `json` format


## Timeline

This project is part of AI Bootcamp / Data Science training at [<\/becode>](www.becode.org)

July, 2023 | Ghent