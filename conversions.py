#!/usr/bin/env python
# coding: utf-8

# In[4]:


def length_feet(feet):
    return feet * 30.48

def length_inches(inches):
    return inches * 2.54

def mass(pounds):
    return pounds * 0.45359237
    
def temperature(kelvin):
    if kelvin < 0:
        return False
    return kelvin - 273.15
    
def time_hours(hours):
    return hours * 3600

def time_minutes(minutes):
    return minutes * 60


# In[ ]:




