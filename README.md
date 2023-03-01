# AppsAnalysis
A data analysis project for mobile applications and its uses based on the CRISP-DM methodology.
This project includes:
<ul>
<li><strong>Backend</strong> - built with Node.js and MongoDB to store and manipulate the datasets.</li>
<li><strong>Analysis</strong> - Full Exploratory Data Analysis (EDA).</li>
<li><strong>Modeling</strong> - Data mining models evaluation.</li>
</ul>

## Business understanding:
What is the probability of an application in the google playstore to achieve success considering different varients?

## Data understanding:
Selecting relevant data from various datasources containing data of the apps in the google playstore.

ADD MORE DESCRIPTION ABOUT THE DATA: tables and features

## Data preparation:
Using star scheme design in order to decide which data to explore.

ADD SCEHMA

## Modeling:
### supervised learning in order to predict the success rate of an app based on price and rating.
  Depending on the type of the test group, we used one of the following algorithms:
  
  Continuous variable:

  1. Random forest regressor
  2. Linear rgression

  Discreet variable:

  3. Random forest classifier
  4. KNeighborsClassifier
  5. SVM classifier 

### unsupervised learning algorithms in order to predict the success rate of an app 

## Evaluation:
** Conclusions?

<img src="./figures/1.jpeg" alt="Alt text" title="Eyal 1">
<img src="./figures/2.jpeg" alt="Alt text" title="Eyal 2">
<img src="./figures/confusion.jpeg" alt="Alt text" title="Confusion Matrix">
<img src="./figures/error-rate.jpeg" alt="Alt text" title="Error Rate">

<!-- ## Phase 1:
Choose a dataset and a research question
Decide on a design for the project

## Phase 2: ETL ( Only E and T)
E - Extracting all of the available data sources
T - Transform - map all datasources to our design and fill the tables + create a software design
 
## Phase 3:
Formalize design

## Phase 4:
Exploration - Exploring tables (App, Installs, Rating, Reviews)

## Phase 5:
Standardization of each table

## Phase 6:
Queries - Joined tables ( Apps & Installs, Apps & Rating, Apps & Reviews)
- results and conclusions based on the queries

## Phase 7:
Feature importance for each of the joined tables while using random forest regressor algorithm -->
