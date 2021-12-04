# Amazon Product Customer-Review-Classification

The aim of the project is to build classification model  using LSTM after text preprocessing using NLP.

## Table of Content
  * [Business_Context](#Business_Context)
  * [Dataset](#Dataset)
  * [Model_Evaluation](#Model_Evaluation)
  * [Business_Recommendation](#Business_Recommendation)
  * [Documentation](#Documentation)
  * [Credit](#Credit)
  
## Business_Context
Amazon Alexa available in multiple variants. Customer review data has been collected for each variant.In ordee to know about product performance, one of  important aspects is to know about cutsomer reviews regarding the projects. Exactly, we are trying to do using the LSTM model after text preprocessing using NLP



 
 ## Dataset
 The dataset consists of the following attributes:
 Variables - 
 * Productt Name
 * Review
 * Rating
### Dataset shape - Rows - 1409 , Colums = 3


 <img src="/Data.png" width="300">   

 
        


## Model_Evaluation
* LSTM model accuracy is 81%.
* LSTM model F1 socre , Recall ,Precision are 0.87,0.93,0.83 for postive reviews.  
* For our business use case , Fasle postive is more importanc since for a better product performance, customer  negative reviews are more inmportant.So precision is comparatively more important.



 <img src="/model%20evaluation.png" width="300">   




## Business_Recommendation
* Need to analyze further - percentages of postive review and negative reviews for each variant.and Based on the analysis, need to recommend modification in product variant.

  
## Documentation
Please click the below link for documentation
https://drive.google.com/drive/folders/1aX-exE3cD6aOfX1VMlIX9jB4CAswXfsF?usp=sharing

## Credit
 This project has been done as a course project in Deep Learning .

