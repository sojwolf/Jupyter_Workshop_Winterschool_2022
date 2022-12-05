#!/usr/bin/env python
# coding: utf-8

# # Additional Materials

# ## Plant traits - TRY database

# The TRY database contains trait measurements from individual plants and, typically, multiple individual measurements per trait and species. We want to extract a mean for each trait value per species.

# We have prepared data for this course, however, for future reference, to download data from the TRY database, create an account at https://www.try-db.org/de.
# 
# We choose the option of open access data only, but the curators of this database still require you to add a short project description to your download request. You will then be sent a download link via e-mail.
# 
# For this study we will use continuous (con) traits used in the sPlot analysis from Buehlheide et al. 2018:
# 
# 
# | Trait     | ID     | Unit    |
# | :------------- | :----------: | -----------: |
# | Leaf area (in case of compound leaves: leaflet, undefined if petiole is in- or excluded) | 3113 | mm^2 |
# | Leaf area per leaf dry mass (specific leaf area, SLA or 1/LMA): undefined if petiole is in- or excluded) | 3117 |m^2/kg|
# | Stem specific density (SSD) or wood density (stem dry mass per stem fresh volume) | 4 | g/cm^3 |
# | Leaf carbon (C) content per leaf dry mass | 13 | mg/g |
# | Leaf nitrogen (N) content per leaf dry mass| 14 | mg/g |
# | Leaf phosphorus (P) content per leaf dry mass| 15| mg/g |
# | Plant height vegetative | 3106 | m |
# | Seed dry mass | 26 | mg |
# | Seed length | 27 | mm |
# | Leaf dry mass per leaf fresh mass (leaf dry matter content, LDMC) | 47 | g/g |
# | Leaf nitrogen (N) content per leaf area | 50   | g/m^2 |
# | Leaf nitrogen/phosphorus (N/P) ratio | 56 | g/g |
# | Leaf nitrogen (N) isotope signature (delta 15N) | 78 | ppm |
# | Seed number per reproducton unit | 138 |  |
# | Leaf fresh mass | 163 | g
# | Stem conduit density (vessels and tracheids) | 169 | mm-2 |
# | Dispersal unit length | 237 | mm |
# | Wood vessel element length; stem conduit (vessel and tracheids) element length | 282 | μm |
# 
# 
# 
# 
# When asked which traits you would like to download, type in the following list. This filters TRY data for our traits of interest, listed in the table above.
# 
# ```3113, 3117, 4, 13, 14, 15, 3106, 26, 27, 47, 50, 56, 78, 138, 163, 169, 237, 282```

# ### Load Data

# First, load the TRY data as a data frame, selecting only the following columns:
# - **AccSpeciesName** - Consolidated species name
# - **SpeciesName** - Species name
# - **TraitID** - Unique identifier for traits (only if the record is a trait)
# - **TraitName** - Name of trait (only if the record is a trait)
# - **StdValue** - Standardized value: available for standardized traits

# In[12]:


TRYdata = pd.read_csv("Data/iNaturalist/Data/TRY/19287.txt", sep = "\t", encoding="iso-8859-1", 
                      usecols = ["AccSpeciesName", "SpeciesName", "TraitID", "TraitName", "StdValue"],
                     dtype={'TraitID': float})


# In[13]:


TRYdata.head()


# In[14]:


# drops rows with missing values
TRYdata = TRYdata.dropna(subset=["TraitID"])


# In[15]:


# check number of unique trait names
TRYdata["TraitID"].nunique()


# In[16]:


# number of unique species
TRYdata["AccSpeciesName"].nunique()


# We remove author annotation and subspecies information from species names.

# In[17]:


# make all letters lower case
TRYdata['AccSpeciesName'] = TRYdata['AccSpeciesName'].str.lower()
# capitalize first letter in string
TRYdata['AccSpeciesName'] = TRYdata['AccSpeciesName'].str.capitalize()
# get only two first words (split at space)
TRYdata['AccSpeciesName']  = TRYdata['AccSpeciesName'].apply(lambda x: ' '.join(x.split()[0:2]))
# change type to string
TRYdata['AccSpeciesName'] = TRYdata['AccSpeciesName'].astype(str)

# same for species name
TRYdata['SpeciesName'] = TRYdata['SpeciesName'].str.lower()
TRYdata['SpeciesName'] = TRYdata['SpeciesName'].str.capitalize()
TRYdata['SpeciesName'] = TRYdata['SpeciesName'].astype(str)
TRYdata['SpeciesName']  = TRYdata['SpeciesName'].apply(lambda x: ' '.join(x.split()[0:2]))


# In[18]:


TRYdata['AccSpeciesName'].nunique()


# In[19]:


TRYdata['SpeciesName'].nunique()


# ### Check for duplicate names

# In[ ]:


TRY_sp = TRYdata["AccSpeciesName"].apply(str)
TRY_sp = TRY_sp.unique()
len(TRY_sp)


# In[ ]:


from rapidfuzz import process, fuzz

def fuzzy_match(choices, queries, cutoff):
    
    score_sort = [(x,) + i
             for x in queries
             for i in process.extract(x, choices, score_cutoff=cutoff, scorer=fuzz.token_sort_ratio) ]
    
    similarity_sort = pd.DataFrame(score_sort)
    similarity_sort = similarity_sort[similarity_sort[2] != 100.0]
    return similarity_sort


# In[ ]:


TRY_matches = fuzzy_match(TRY_sp, TRY_sp, 95)


# In[ ]:


TRY_matches.head()


# In[ ]:


TRY_matches[0].nunique()


# In[ ]:


(len(TRY_matches)/2)/len(TRY_sp)


# Only 0.5% of unique species in TRY have potential duplicates (similar names). Since we are looking at vast scales and, we can diregard this slight uncertainty and accept that these species might not be matched to the iNaturalist observations.
# 
# We devide the number for matches by 2, since every pair is listed twice (positions switched).

# ### Create summary stats with consolidated species name

# Use ```groupby``` function to group data by consolidated species name and trait; grouping variables: ```AccSpeciesName, TraitName, TraitID```.
# 
# More information: https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm

# In[20]:


# group data by species name and trait

grouped = TRYdata.groupby(['AccSpeciesName', 'TraitID', 'TraitName'])
TRY = grouped['StdValue'].agg([np.mean]).reset_index()

#check output
TRY.head()


# In[21]:


def shorten_names(df):

    df.rename(columns = {'Stem specific density (SSD) or wood density (stem dry mass per stem fresh volume)':'SSD'}, inplace = True)
    df.rename(columns = {'Leaf carbon (C) content per leaf dry mass':'Leaf C'}, inplace = True)
    df.rename(columns = {'Leaf nitrogen (N) content per leaf dry mass':'Leaf N per mass'}, inplace = True)
    df.rename(columns = {'Leaf phosphorus (P) content per leaf dry mass':'Leaf P'}, inplace = True)
    df.rename(columns = {'Leaf dry mass per leaf fresh mass (leaf dry matter content, LDMC)':'LDMC'}, inplace = True)
    df.rename(columns = {'Seed dry mass':'Seed mass'}, inplace = True)
    df.rename(columns = {'Seed length':'Seed length'}, inplace = True)
    df.rename(columns = {'Leaf nitrogen (N) content per leaf area':'Leaf N per area'}, inplace = True)
    df.rename(columns = {'Leaf nitrogen/phosphorus (N/P) ratio':'Leaf N P ratio'}, inplace = True)
    df.rename(columns = {'Leaf nitrogen (N) isotope signature (delta 15N)':'Leaf delta15N'}, inplace = True)
    df.rename(columns = {'Leaf fresh mass':'Leaf fresh mass'}, inplace = True)
    df.rename(columns = {'Seed number per reproducton unit':'Seeds per rep. unit'}, inplace = True)
    df.rename(columns = {'Stem conduit density (vessels and tracheids)':'Stem conduit density'}, inplace = True)
    df.rename(columns = {'Dispersal unit length':'Dispersal unit length'}, inplace = True)
    df.rename(columns = {'Wood vessel element length; stem conduit (vessel and tracheids) element length':'Conduit element length'}, inplace = True)
    df.rename(columns = {'Plant height vegetative':'Plant Height'}, inplace = True)
    df.rename(columns = {'Leaf area (in case of compound leaves: leaflet, undefined if petiole is in- or excluded)':'Leaf Area'}, inplace = True)
    df.rename(columns = {'Leaf area per leaf dry mass (specific leaf area, SLA or 1/LMA): undefined if petiole is in- or excluded':'SLA'}, inplace = True)


# Change data frame from long to wide using ```pandas.DataFrame.pivot```. And shorten trait names.

# In[22]:


TRY = TRY.pivot(index=["AccSpeciesName"], columns="TraitName", values="mean")

# reset indeces (species name) as columns in data frame
TRY.reset_index(inplace=True)

# rename trait variables to shorter names
shorten_names(TRY)

TRY.head(3)


# In[23]:


# Optional: Save file
#TRY.to_csv("TRY/TRY_summary_stats.csv", index=False)


# ### Create summary stats with original name

# In[24]:


# group data by species name and trait, same analysis as above
grouped_syn = TRYdata.groupby(['SpeciesName', 'TraitID', 'TraitName'])

TRY_syn = grouped_syn['StdValue'].agg([np.mean]).reset_index()

# change df shape
TRY_syn = TRY_syn.pivot(index=["SpeciesName"], columns="TraitName", values="mean")

# reset indeces (species name) as columns in data frame
TRY_syn.reset_index(inplace=True)

# shorten column names
shorten_names(TRY_syn)

#optional
#TRY_syn.to_csv("TRY/TRY_summary_stats_syn.csv", index=False)

TRY_syn.head(3)


# ## Link iNaturalist to TRY

# Non-fuzzy merge with TRY summary stats on **consolidated TRY species name**:
# 

# In[ ]:


import pandas as pd # for handling dataframes in python

iNat = pd.read_csv('iNat_observations.csv')


# In[25]:


iNat_TRY = pd.merge(iNat, TRY, 
                    left_on= ['scientificName'],
                    right_on= ['AccSpeciesName'], 
                    how='inner')
iNat_TRY.head(3)


# Extract from TRY those observations that have not been matched:

# In[26]:


# filter for observations not in merged dataframe:
iNat_rest = iNat[~iNat.gbifID.isin(iNat_TRY['gbifID'])]
iNat_rest.shape


# We repeat the same with the **'original' species name** in TRY:

# In[27]:


# non-fuzzy merge with TRY summary stats on original TRY species name:

iNat_TRY_syn = pd.merge(iNat_rest, TRY_syn, 
                    left_on= ['scientificName'],
                    right_on= ['SpeciesName'], 
                    how='inner')
iNat_TRY_syn.head(3)


# In[28]:


subsets = [iNat_TRY, iNat_TRY_syn]

iNat_TRY_all = pd.concat(subsets)
iNat_TRY_all = iNat_TRY_all.drop(['AccSpeciesName', 'SpeciesName'], axis = 1)


# In[29]:


# replace infinite values as NaN

iNat_TRY_all = iNat_TRY_all.replace(-np.inf, np.nan)
iNat_TRY_all = iNat_TRY_all.replace(np.inf, np.nan)


# In[30]:


iNat_TRY_all.head()


# In[31]:


trait = iNat_TRY_all.columns[6:24]

iNat_TRY_all.loc[:, trait] = np.log(iNat_TRY_all[trait])


# In[32]:


iNat_TRY_all.to_csv("iNat_TRY_log.csv", index=False)

iNat_TRY_all.head()


# After matching with consolidated and original name, we were able to match about 84% of the iNaturalist observations with trait information. Many rare species seem to be absent in either one of the two databases.
# 

# In[33]:


print('percentage of iNat observations linked with at least one TRY trait:')
print(len(iNat_TRY_all)/len(iNat))

print('percentage of species in iNaturalist matched with TRY:')
print(iNat_TRY_all["scientificName"].nunique()/iNat["scientificName"].nunique())

