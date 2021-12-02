# Amazon Product Customer-Review-Classification

The aim of the project is to build classification model  using LSTM post text preprocessing uasing NLP.

## Table of Content
  * [Business_Context](#Business_Context)
  * [Dataset](#Dataset)
  * [Model_Evaluation](#Model_Evaluation)
  * [Business_Recommendation](#Business_Recommendation)
  * [Credit](#Credit)
  
## Business_Context
Amazon Alexa available in multiple variants. Customer review data has been collected for each variant.In ordee to know about product performance, one of  important aspects is to know about cutsomer reviews regarding the projects. Exactly, we are trying to do using the LSTM model aftex text preprocessing using NLP



 
 ## Dataset
 The dataset consists of the following attributes:
 Variables - 
 * Prodcut Name
 * Review
 * Rating
### Dataset shape - Rows - 1409 , Colums = 3


 <img src="/Data.png" width="300">   

 
        


## Model_Evaluation
* XG Boost performs better than other models
* Hyperparameters tuning is done by RandomizedSearchCV for xgboost
* It has a higher accuracy of83.24%
* True Negative is almost double than false negative
* Rest of the models have very poor performance in terms of predicting true negative values
* True negative values are crucial because it is important to know who will not join the organization



## Business_Recommendation
* Firm should focus on 3 important features 'Percent difference CTC', 'Duration to accept the offer'& 'Age'
* Firm should introduce new offering/schemes based on these 3 features combination so that attrition rate can reduce.

## Credit
[dare2Compete](https://https://dare2compete.com/) - This project has been done on this competitive platform.

