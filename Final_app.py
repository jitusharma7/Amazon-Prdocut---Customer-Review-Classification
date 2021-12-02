#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:



import streamlit as st
from Multipgae_app import MultiApp
import Review_Prediction,Business_Problem # import your app modules here

Final = MultiApp()

# Add all your application here
#Final.add_app("Project_Information", Project_Information.app)
#Final.add_app("Overview", Overview.app)
#Final.add_app("Dashboard", Dashboard.app)
Final.add_app("Business_Problem", Business_Problem.app)
Final.add_app("Review_Prediction", Review_Prediction.main)

# The main app
Final.run()


# In[ ]:


# In[ ]:





# In[ ]:





# In[ ]:




