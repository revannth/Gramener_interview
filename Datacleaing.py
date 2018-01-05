
# coding: utf-8

# In[1]:


#main.py

import pandas as pd

tab = pd.read_csv('data/nas-pupil-marks.csv')
influence = pd.read_csv('data/nas-pupil-marks.csv')
tab.head()


# In[2]:


col = list(tab.head(0).columns)
print col

tab.drop(col[4:-4],axis=1,inplace=True)




# In[3]:



tab.drop(["STUID","District"],axis=1,inplace=True)


# In[4]:


display(tab)


# In[5]:



sorted_tabs = tab.sort_values(['Gender','Maths %','Reading %','Science %','Social %'],ascending=False)
display(sorted_tabs)




# In[6]:


sorted_tabs.shape


# In[7]:


booleans = []
for gender in sorted_tabs.Gender:
    if gender>0:
        booleans.append(True)
    else:
        booleans.append(False)


# In[8]:


boolean_simple = sorted_tabs.Gender>0
        


# In[9]:


boolean_simple.head()


# In[10]:


sorted_tabs[boolean_simple]


# In[11]:


gender_filter = sorted_tabs[sorted_tabs.Gender>0]


# In[12]:


test = gender_filter.dropna(thresh=4)
cleaned_data=test.sort_values(['Gender','State','Maths %','Reading %','Science %','Social %'])

cleaned_data.interpolate(inplace=True)


# In[13]:


cleaned_data.sort_values(['Gender','State','Maths %','Reading %','Science %','Social %'],inplace=True)


# In[14]:


cleaned_data
cleaned_data['Total']=0


# In[15]:


cleaned_data.Total = (cleaned_data["Maths %"] + cleaned_data["Reading %"] + cleaned_data["Science %"] + cleaned_data["Social %"])/4
cleaned_data


# In[16]:


boolean_male = []
boolean_female = []
boolean_male = cleaned_data.Gender<2
boolean_female = cleaned_data.Gender==2


# In[17]:


male_data = cleaned_data[boolean_male]
female_data=cleaned_data[boolean_female]


# In[18]:


State_total_male = male_data.groupby(male_data.State).Total.mean()


# In[19]:



State_total_male.round(1).to_csv('Males.csv')


# In[20]:


State_total_female = female_data.groupby(female_data.State).Total.mean()


# In[21]:


State_total_female.round(1).to_csv('female.csv')


# In[22]:


State_ms = cleaned_data.drop(['Gender','Reading %','Social %','Total'],axis=1)
State_m = State_ms.groupby(State_ms.State)["Maths %"].mean()
State_s = State_ms.groupby(State_ms.State)["Science %"].mean()


# In[23]:


State_m.round(2).to_csv('Mathematics.csv')
State_s.round(2).to_csv('Science.csv')
State_ms.round(2).to_csv('Mathscience.csv')


# In[ ]:





# In[24]:


State_m


# In[25]:


import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('revannth', '0U9AEQ9wp9ZpwfBzbAEp0U9AEQ9wp9ZpwfBzbAEp')
trace1 = {
  "x": ["AN", "AP", "AR", "BR", "CG", "CH", "DD", "DL", "DN", "GA", "GJ", "HP", "HR", "JH", "JK", "KA", "KL", "MG", "MH", "MN", "MP", "MZ", "NG", "OR", "PB", "PY", "RJ", "SK", "TN", "TR", "UK", "UP", "WB"], 
  "y": ["39.6563219895", "32.5579683535", "35.7135180199", "35.8038346553", "34.6753542169", "35.6321366712", "48.5316631799", "33.2623909705", "45.3470596394", "41.9308862498", "37.0032520208", "32.6384144588", "36.3011361988", "39.4681681491", "37.4908081254", "32.788672863", "40.2811154044", "31.7483780992", "35.4283587595", "41.8752659418", "40.3751338754", "38.0013136655", "33.3299062328", "37.9442396505", "37.4218439933", "30.4351278518", "35.0525462234", "40.195", "31.8356602633", "44.5616651959", "33.7502389532", "41.6249525923", "39.2768890788"], 
  "mode": "lines", 
  "name": "Science Marks", 
  "type": "scatter", 
  "uid": "309e09", 
  "xsrc": "revannth:11:e0b8a7", 
  "ysrc": "revannth:11:c67c02"
}
trace2 = {
  "x": ["AN", "AP", "AR", "BR", "CG", "CH", "DD", "DL", "DN", "GA", "GJ", "HP", "HR", "JH", "JK", "KA", "KL", "MG", "MH", "MN", "MP", "MZ", "NG", "OR", "PB", "PY", "RJ", "SK", "TN", "TR", "UK", "UP", "WB"], 
  "y": ["31.3644764398", "36.2194596208", "36.3792460646", "43.6302165955", "38.6232931727", "31.4861840325", "39.2118828452", "37.110625", "40.0573324087", "37.5520609145", "36.2482202656", "33.9512466626", "40.5628436707", "42.4786912325", "42.1561382204", "39.6959766875", "34.8700940237", "34.1202405549", "39.6179723646", "44.4054892742", "44.832403808", "41.6361174506", "36.773838941", "40.1630819638", "42.0195710579", "35.6208696984", "41.0003855232", "36.4392321981", "37.5538527673", "44.2634804095", "36.1953290347", "48.1072523704", "55.5879369271"], 
  "mode": "lines", 
  "name": "Mathematics Marks", 
  "type": "scatter", 
  "uid": "101d3b", 
  "xsrc": "revannth:11:e0b8a7", 
  "ysrc": "revannth:12:fd9134"
}


# In[ ]:


data = Data([trace1, trace2])
layout = {
  "geo": {
    "projection": {
      "rotation": {"lon": 0}, 
      "scale": 0.924022572447, 
      "type": "equirectangular"
    }, 
    "scope": "asia"
  }, 
  "hovermode": "closest", 
  "showlegend": True, 
  "title": "Mathematics vs Science", 
  "xaxis": {
    "autorange": True, 
    "range": [0, 32], 
    "title": "Country Code", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [29.0377495698, 56.9853152091], 
    "title": "Marks", 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)


# In[26]:


import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('revannth', '0U9AEQ9wp9ZpwfBzbAEp')
trace1 = {
  "x": ["Andaman & Nicobar Island", "Andhra Pradesh", "Arunanchal Pradesh", "Bihar", "Chandigarh", "Chhattisgarh", "Dadara & Nagar Havelli", "Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT of Delhi", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Odisha"], 
  "y": ["39", "39.6", "38.3", "39.8", "40.1", "41.5", "44", "49.2", "45.7", "39.2", "40.8", "37.8", "39.2", "41.6", "38.2", "45.5", "45.3", "42.4", "42.3", "35.5", "41.8", "38.4", "40.1", "36", "41.5", "43.4", "39.9", "36.8", "39.6", "45.2", "46.7", "38.8", "53.1", "38.8"], 
  "mode": "markers", 
  "name": "Per Region Female Performance", 
  "type": "scatter", 
  "uid": "1af5b2", 
  "xsrc": "revannth:23:821d5a", 
  "ysrc": "revannth:23:d48366"
}
trace2 = {
  "x": ["Andaman & Nicobar Island", "Andhra Pradesh", "Arunanchal Pradesh", "Bihar", "Chandigarh", "Chhattisgarh", "Dadara & Nagar Havelli", "Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT of Delhi", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Odisha"], 
  "y": ["37.4", "36.8", "38.6", "41.9", "39.3", "41.3", "44.3", "47.9", "41.5", "38.8", "41.3", "37.2", "37.4", "43.7", "37.9", "41", "46.8", "43.1", "43.3", "34.4", "38.6", "37.8", "38.4", "34.4", "40.6", "41.4", "41.2", "36.9", "36.8", "45.5", "49.2", "38.5", "43.1", "39.7"], 
  "mode": "markers", 
  "name": "Per Region Male Performance", 
  "type": "scatter", 
  "uid": "924679", 
  "xsrc": "revannth:23:821d5a", 
  "ysrc": "revannth:28:d470ba"
}
data = Data([trace1, trace2])
layout = {
  "autosize": True, 
  "hovermode": "closest", 
  "showlegend": True, 
  "title": "Male vs Female Performance Plot", 
  "xaxis": {
    "autorange": True, 
    "range": [-2.25, 35.25], 
    "title": "STATES", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [32.9360338243, 54.5639661757], 
    "title": "Marks", 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)


# In[73]:


influence.drop(['STUID','District','State','Gender'],inplace=True,axis=1)



# In[74]:


influence.drop(['Gender'],inplace=True,axis=1)


# In[118]:


influence.drop(['Subjects'],inplace=True,axis=1)


# In[119]:


influence.replace('No',0)


# In[120]:


influence.replace("Yes",1)


# In[121]:


influence2 = pd.melt(influence,id_vars=['Maths %','Science %','Reading %','Social %'],var_name="Factors",value_name="Intensity")


# In[122]:


influence2.replace('No',0)


# In[123]:


cleaned_influence = influence2.dropna(thresh=4)


# In[124]:


cleaned_influence.sort_values(['Factors','Intensity']).interpolate(inplace=True)


# In[125]:


cleaned_influence.replace('No',0,inplace=True)
cleaned_influence.replace('Yes',1,inplace=True)


# In[126]:


cleaned_influence.dropna(how='any',inplace=True)


# In[133]:


cleaned_influence.Intensity.astype(int)
mean_clean = cleaned_influence.groupby(['Factors']).mean()


# In[136]:


mean_clean.to_csv('mean_clean.csv')


# In[50]:





# In[46]:





# In[55]:




