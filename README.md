# Amazon-Prdocut---Customer-Review-Classification

The aim of the project is to build classification model  using LSTM post text preprocessing uasing NLP.

## Table of Content
  * [Business_Context](#Business_Context)
  * [Data_Context](#Data_Context)
  * [Dataset](#Dataset)
  * [Model_Evaluation](#Model_Evaluation)
  * [Business_Recommendation](#Business_Recommendation)
  * [Credit](#Credit)
  
## Business_Context
rate is a metric used to measure employees or customers lost over a period who are not replaced. The rate is shown as a percentage compared to the total workforce or customer base. Human resources employees often use an attrition rate to determine the number of vacant or eliminated positions

**Impact of attrition on Business**
The costs of employee attrition range from quantifiable numbers to hidden costs. When employees resign from companies, costs are incurred in recruiting new employees and training them. Productivity will be lower until new hires learn the business. If it is a customer-based business, customers could be dissatisfied if the new hire is not proficient.
 According to Deloitte, the average cost per hire is $4,000. This cost can be varied by country, region, industry,
 
 So attrition is vital metric and needs to build suitable model and identify what are the key factor which drives individual to leave the organization.
 
 ## Data_Context
 One talent acquisition agency is facing challenges about default rate where candidates not joining the company after accepting the offer. Acquiring new talent is always a challenging and time-consuming task, especially in the IT industry since the recruit has to handle numerous changes in an ever-changing landscape. In many instances, it is even difficult to find the exact matching candidates for the specified job role. In such a scenario, if an offer is denied, then the human resource (HR) department has to repeat the entire recruitment process resulting in additional effort from the top management.
 
 The talent acquisition agency  is trying to address this problem by identifying patterns in their existing candidate records using a Machine learning algorithm
 
 
 ## Dataset
 The dataset consists of the following attributes:

* SLNO
* Candidate Ref - unique candidate reference number
* DOJ Extended
* Duration to accept the offer 
* Notice period
* Offered band 
* Percent hike expected in CTC
* Percent difference CTC
* Joining Bonus (1: yes, 0: No)
* Candidate relocate actual (1: yes, 0: No)
* Gender ( 1: Male, 0: Female )
* Candidate Source
* Location
* Age
* Target Variable - Status ( 1: Joined Organization, 0: Not Joined Organization ) 

 
        


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

