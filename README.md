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

<strong>Inital design scheme</strong>
<img src="./figures/design-scheme.jpeg" alt="Alt text" title="Design Scheme" />

## Data preparation:
Using star scheme design in order to decide which data to explore.

## Modeling:

### (1) Supervised learning in order to predict the success rate of an app based on price:
  <u>Continuous variable:</u>

  1. Random forest regressor
  2. Linear rgression


### (2) Supervised learning in order to predict the success rate of an app based on rating:
  <u>Discreet variable:</u>

  3. Random forest classifier
  4. KNeighborsClassifier
  5. SVM classifier 

### (3) unsupervised learning algorithms in order to predict the success rate of an app

## Evaluation and Conclusions:

<strong>Sentiment in relation to price</strong>
<img src="./figures/1.jpeg" alt="Alt text" title="Price">
- Free apps recieve higher sentiment and paid apps recieve lower sentiment rating
- People react to free apps in a positive manner

<strong>Sentiment in relation to reviews</strong>
<img src="./figures/2.jpeg" alt="Alt text" title="Reviews number">
- Reviews in cluster 8 contain apps with a neutral review - not affecting the sentiment ( Sentiment is 0)
- Reviews in cluster 5 vary from -1 to 1 ( As expected)

<strong>Rating prediction</strong>
<img src="./figures/confusion.jpeg" alt="Alt text" title="Confusion Matrix">

- Rating 1/2: Not enough data in order for the algorithm to model by
- Rating 3: Prediction rate of 76%
- Rating 4: Prediction rate of 91%
- Rating 5: Prediction rate of 55%

<strong>Error rate vs K value</strong>
<img src="./figures/error-rate.jpeg" alt="Alt text" title="Error Rate">

- K=3 has the lowest error rate