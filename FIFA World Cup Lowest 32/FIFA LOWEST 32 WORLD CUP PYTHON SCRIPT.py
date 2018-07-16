
# coding: utf-8

# In[41]:


import pandas
import random


# In[42]:


df1=pandas.read_excel("grouping lowest.xlsx")


# In[3]:


df1


# In[4]:


from pandas import DataFrame


# In[5]:


grouping=DataFrame(df1)


# In[6]:


grouping


# In[8]:


grouping.drop([0])


# In[9]:


df2=pandas.read_excel("details lowest32.xlsx")


# In[10]:


df2


# In[13]:


details=DataFrame(df2)


# In[15]:


details


# In[34]:


redetails=details.rename(index={0:"GU",1:"MA",2:"TL",3:"USVI",4:"MOL",5:"STEP",6:"DJI",7:"CAY",8:"CU",9:"ARU",10:"SAM",11:"SOM",12:"LIE",13:"GUA",14:"AS",15:"TO",16:"LA",17:"BHU",18:"BAN",19:"SRI",20:"CHA",21:"MAC",22:"GIB",23:"PAK",24:"BER",25:"SEY",26:"BD",27:"BAH",28:"DOM",29:"MON",30:"CI",31:"SM"})


# In[40]:


redetails


# In[216]:


def winner(teamA,teamB):
    totolA=0
    totalB=0
    countA=0
    countB=0
    
    
    for x in range(5):
        
        totalA=0.01*redetails["WIN PER"].loc[teamA]+0.01*redetails["NET GOALS"].loc[teamA]+random.randint(0,120)
        totalB=0.01*redetails["WIN PER"].loc[teamB]+0.01*redetails["NET GOALS"].loc[teamB]+random.randint(0,120)
        print(totalA,totalB)
        if(totalA>totalB):
            print("winner is"+teamA)
            
        else:
            print("winner is"+ teamB)
            
        
    


# In[200]:


#qualification of group
winner("GU","MA")
winner("GU","TL")
winner("GU","USVI")
winner("MA","TL")
winner("MA","USVI")
winner("TL","USVI")
winner("MOL","STEP")
winner("MOL","DJI")
winner("MOL","CAY")
winner("STEP","DJI")
winner("STEP","CAY")
winner("DJI","CAY")
winner("CU","ARU")
winner("CU","SAM")
winner("CU","SOM")
winner("ARU","SAM")
winner("ARU","SOM")
winner("SOM","SAM")
winner("LIE","GUA")
winner("LIE","AS")
winner("LIE","TO")
winner("GUA","AS")
winner("GUA","TO")
winner("AS","TO")
winner("LA","BHU")
winner("LA","BAN")
winner("LA","SRI")
winner("BHU","BAN")
winner("BHU","SRI")
winner("BAN","SRI")
winner("CHA","MAC")
winner("CHA","GIB")
winner("CHA","PAK")
winner("MAC","GIB")
winner("MAC","PAK")
winner("GIB","PAK")
winner("BER","SEY")
winner("BER","BD")
winner("BER","BAH")
winner("SEY","BD")
winner("SEY","BAH")
winner("BD","BAH")
winner("DOM","MON")
winner("DOM","CI")
winner("DOM","SM")
winner("MON","CI")
winner("MON","SM")
winner("CI","SM")

# In[202]:


def knockout(teamA,teamB):
    totolA=0
    totalB=0
    countA=0
    countB=0
    
    
    for x in range(5):
        
        totalA=0.4*redetails["WIN PER"].loc[teamA]+0.4*redetails["NET GOALS"].loc[teamA]+random.randint(0,10)
        totalB=0.4*redetails["WIN PER"].loc[teamB]+0.4*redetails["NET GOALS"].loc[teamB]+random.randint(0,10)
        print(totalA,totalB)
        if(totalA>totalB):
            print("winner is"+teamA)
            
        else:
            print("winner is"+ teamB)


# In[204]:


knockout("GU","CAY")
knockout("TL","MOL")
knockout("CU","TO")
knockout("ARU","LIE")
knockout("BHU","MAC")
knockout("SRI","PAK")
knockout("SEY","CI")
knockout("BER","SM")


# In[207]:


def knockquarters(teamA,teamB):
    totolA=0
    totalB=0
    countA=0
    countB=0
    
    
    for x in range(5):
        
        totalA=0.6*redetails["WIN PER"].loc[teamA]+0.6*redetails["NET GOALS"].loc[teamA]+random.randint(0,120)
        totalB=0.6*redetails["WIN PER"].loc[teamB]+0.6*redetails["NET GOALS"].loc[teamB]+random.randint(0,120)
        print(totalA,totalB)
        if(totalA>totalB):
            print("winner is"+teamA)
            
        else:
            print("winner is"+ teamB)


# In[208]:


knockquarters("GU","TL")
knockquarters("CU","ARU")
knockquarters("BHU","PAK")
knockquarters("CI","BER")


# In[209]:


def semiknock(teamA,teamB):
    totolA=0
    totalB=0
    countA=0
    countB=0
    
    
    for x in range(5):
        
        totalA=0.8*redetails["WIN PER"].loc[teamA]+0.8*redetails["NET GOALS"].loc[teamA]+random.randint(0,120)
        totalB=0.8*redetails["WIN PER"].loc[teamB]+0.8*redetails["NET GOALS"].loc[teamB]+random.randint(0,120)
        print(totalA,totalB)
        if(totalA>totalB):
            print("winner is"+teamA)
            
        else:
            print("winner is"+ teamB)


# In[210]:


semiknock("GU","ARU")
semiknock("PAK","BER")


# In[212]:


def final(teamA,teamB):
    totolA=0
    totalB=0
    countA=0
    countB=0
    
    
    for x in range(5):
        
        totalA=1*redetails["WIN PER"].loc[teamA]+1*redetails["NET GOALS"].loc[teamA]+random.randint(0,120)
        totalB=1*redetails["WIN PER"].loc[teamB]+1*redetails["NET GOALS"].loc[teamB]+random.randint(0,120)
        print(totalA,totalB)
        if(totalA>totalB):
            print("winner is"+teamA)
            
        else:
            print("winner is"+ teamB)


# In[214]:


final("ARU","BER")

