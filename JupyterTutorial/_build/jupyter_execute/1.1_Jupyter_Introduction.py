#!/usr/bin/env python
# coding: utf-8

# # Introduction to Jupyter Notebook (Part 1)
# 

# *gfbio Winterschool 2022, Sophie Wolf*

# Jupyter refers to **Ju**lia, **Py**thon and **R**
# 
# Jupyter Notebook (formerly IPython Notebooks) is a web-based open-source interactive computational environment.
# 
# --- 
# 
# A notbook contains a list of input and output cells, which can contain:

# In[1]:


# code
1+1


# Text formatted with **Markdown**

# In[2]:


import matplotlib.pyplot as plt

plt.plot(range(10))
plt.title('Display plot in notebook')
plt.show()


# ## Creating a new notebook
# 
#    - Kernels
#   
# We will be using Python 3 and R kernels.

# ## First orientation
# 
#    - user interface tour
#    - command mode and edit mode
#    - keyboard shortcuts
#    

# In[3]:


print("Winterschool 2022")


# In[4]:


title = "Winterschool 2022"


# In[5]:


title


# In[6]:


"Winterschool 2022"


# Supress output using ```;```

# In[7]:


"Winterschool 2023";


# ### 🤖 Try it!
# 
# **Take a few minutes to explore the keyboard shortcuts.**

# ---

# ## Ordering of executions
# 
# Be mindful: You can execute Jupyter cells in any order.
# The execution order is displayed as numbers to the left of each code cell.

# In[8]:


species = "Nepeta cataria"


# In[11]:


species


# In[10]:


species = "Theobroma cacao"


# ## A few remarks on Markdown
# 
# Markdown is a simple markup language for creating formatted text using a plain-text editor.
# 
# ---
# 
# ### Some functions
# 
# - *italics*
# - **bold**
# - ```code block here```
# 
# You can create things like this nice table:
# 
# | Some traits in TRY database   | ID     | Unit    |
# | :------------- | :----------: | -----------: |
# | Leaf area (in case of compound leaves: leaflet, undefined if petiole is in- or excluded) | 3113 | mm<sup>2 |
# | Leaf area per leaf dry mass (specific leaf area, SLA or 1/LMA): undefined if petiole is in- or excluded) | 3117 |m<sup>2</sup>/kg|
# | Stem specific density (SSD) or wood density (stem dry mass per stem fresh volume) | 4 | g/cm<sup>3 |
# | Leaf carbon (C) content per leaf dry mass | 13 | mg/g |
# | Leaf nitrogen (N) content per leaf dry mass| 14 | mg/g |
# | Leaf phosphorus (P) content per leaf dry mass| 15| mg/g |
# | Plant height vegetative | 3106 | m |

# Or insert an image from your local machine or url.
# 
# ![iNaturalist observation: Fouquieria splendens](https://inaturalist-open-data.s3.amazonaws.com/photos/513109/original.jpg?1444266311)
# 
# This image is a citizen science observation from the project iNaturalist.

# ## Line magic and cell magic

# Jupyter has a whole library of so-called line or cell magic. These allow you to switch to other programming languages within on single Jupyter notebook.

# ### bash command 
# 
# To access the terminal simply use an ```!``` before your bash command.

# In[12]:


get_ipython().system('pwd')


# For example, you could use it to install a new package:

# In[ ]:


get_ipython().system('pip install tqdm')


# There are many in-built options for line and cell magics. They always start with:
# 
#   - ```%``` for line magic
#   - ```%%``` for cell magic
#   
# To list all the built-in available magic commands type the following:

# In[13]:


get_ipython().run_line_magic('lsmagic', '')


# **Line magic** refers only to the one line. So all code before and after this line within the same cell will be interpreted as the kernel language, in our case Python 3. There are many bash line magic commands, such as ```%ls``` or ```%pwd```.

# In[14]:


get_ipython().run_line_magic('ls', '')

print("Hi! I'm Python code.")
get_ipython().system('echo "And I\'m bash script."')


# **Cell magic** applies to the whole cell, so all code will be interpreted in reference to the magic command. As a result, the following command will generate an error. Cell magic must always be placed at the top of the cell.

# In[15]:


get_ipython().run_cell_magic('bash', '', '\nls\necho "Hi! I\'m bash script."\nprint("And I\'m Python code.")\n')


# Since Jupyter cells can be executed in any order, you might need to check your notebooks variables. The following commands can be very useful:

# In[16]:


# current variable names

get_ipython().run_line_magic('who', '')


# In[17]:


# current variables, incl. type and data

get_ipython().run_line_magic('whos', '')


# Remove a specific variable from environment:

# In[18]:


get_ipython().run_line_magic('reset_selective', 'species')


# Remove all variables from environment:

# In[19]:


get_ipython().run_line_magic('reset', '')


# How to embed a video:

# In[20]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="700" height="500" \n    src="https://www.youtube.com/embed/HW29067qVWk"\n    frameborder="0"\n    allowfullscreen></iframe>\n')


# ### 🤖 Try it!
# 
# **Take a few minutes to play around with the line and cell magic commands. Create some variables and remove them again.**

# ---

# ## Visualize plots

# In[21]:


# Example from matplotlib documentation

import numpy as np # arrays and such
import matplotlib.pyplot as plt # plotting

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


# ## Execution time 

# If you want to test the speed of your code, the ```%%time``` magic can be very useful.

# In[22]:


get_ipython().run_cell_magic('time', '', 'plt.scatter(x, y, s=area, c=colors, alpha=0.5)\nplt.show()\n')


# ## Look up documentation

# If you want to check the documentation of the function you want to use, simply click inside the function and press ```Shift+Tab```. Or, if that doesn't help, look it up using your favorite search engine!

# In[23]:


plt.scatter(x, y);


# ## Dataframes

# In[24]:


import pandas as pd #handles dataframes in Python
import numpy as np #arrays and such in Python

# create sample dataframe

df = pd.DataFrame(np.random.randn(100,5), columns=["A","B","C","D","E"])
df


# In[25]:


# display only the first 5 rows
df.head(5)


# ### 🤖 Try it!
# 
# **Use the scatter plot function above together with data from the sample dataframe ```df```. Look up the ```plt.scatter()``` documentation to add features to your plot.**

# In[ ]:


# play around with scatter plot function


# ---

# ## Using R within a Python Juypter notebook

# ### R Magic

# To use R within a Python Juypter notebook, which was intitiated using a Python kernel, we need so-called R magic. 

# In[26]:


# enables the %%R magic, needs to be installed and then activated only once per Notebook 
get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# As we've seen before, ```%``` denotes line magic, while ```%%``` denotes cell magic. R magic uses the same syntax.

# In[27]:


get_ipython().run_line_magic('R', 'x <- c(1, 2, 3)')

x


# R variables can also be used across different cells, as long as you call R magic every time.

# In[28]:


get_ipython().run_line_magic('R', 'x')


# In[29]:


get_ipython().run_cell_magic('R', '', '\nx <- append(x, c(5,6,7))\nplot(x)\n')


# ### Move variables from Python environment to R, and vice versa

# In[30]:


get_ipython().run_line_magic('whos', '')


# In[31]:


get_ipython().run_line_magic('Rpush', 'df')


# In[32]:


get_ipython().run_line_magic('R', 'df')


# In[33]:


get_ipython().run_cell_magic('R', '', '\ncorrelation <- cor(df$A, df$B)\ncorrelation\n')


# In[34]:


correlation = get_ipython().run_line_magic('Rget', 'correlation')
correlation


# ### Create a new notebook using an R kernel

# See file ```Winterschool_2022_R_Kernel.ipynb```

# ## Practical example with vegetation data

# In[35]:


# import required packages

import pandas as pd #for data frames
import numpy as np #
from matplotlib import pyplot as plt #for plotting


# ### sPlotOpen

# sPlotOpen (Sabatini et al, 2021) is an open-access and environmentally and spatially balanced subset of the global sPlot vegetation plots data set v2.1 (Bruelheide et al, 2019).
# 
# For future reference, sPlotOpen Data is available at the iDiv Data Repository. For this study we used version 52, which you can download using the following link: https://idata.idiv.de/ddm/Data/ShowData/3474
# 
# The data is stored in various tab-separated files:
# 
# - **sPlotOpen_header(2).txt** : contains information on each plot, such as coordinates, date, biome, country, etc.
# - **sPlotOpen_DT(1).txt** : contains information per plot and species with abundance and relative cover
# - **sPlotOpen_CWM_CWV(1).txt** : contains information on trait community weighted means and variances for each plot and 18 traits (ln-transformed)

# For this example, we will look at the trait community weighted means.

# In[36]:


cwm = pd.read_csv("Data/sPlotOpen_CWM_CWV(1).txt", sep= "\t")


# View the first 5 rows of data frame. **Note: All values are in natural logarithm.**

# In[37]:


cwm.head()


# View information on the dataframe.

# In[38]:


cwm.info()


# ### 🤖 Try it!
# 
# 1. **Plot histograms of two trait cwm's you are interested in. *Extra credit: Plot both histograms inside one graph.***
# 2. **Save figure(s) as PDF.**
# 3. **Check via your Jupyter notebook if the figure was gererated properly.**
# 4. **Plot a scatter plot using one trait x values and another trait on as y values.**
# 5. **Calculate Pearson's correlation coefficient to quantify the linear relationship of trait x and trait y.**
# 
# *Extra credit:* Try and use the keyboard shortcuts to move around the notebook.
# *Note:* There are, of course, many different ways to answer these questions.

# In[ ]:


# plot trait cwm histogramm and export as PDF (give it a unique name!)


# Check if image was generated properly.

# In[ ]:


# plot scatterplot of two traits in relation


# In[ ]:


# calculate Pearson's correlation coefficient r
# Hint 1: Use the pandas function DataFrame.corr() 
# Hint 2: Subsetting a pandas dataframe works like this: df[["variable_1", "variable_2"]]
# Or switch over to R using line or cell magic


# ---

# ## Export your notebook

# Go to ```File > Download as``` at the top left in your Jupyter notebook window. You can download your notebook as:
#     
#    - ```html```, which you could incorporate into your web-documentation, for example
#    - as a ```PDF```
#    - in Jupyter notebook format ```.ipynb```
#    - as Python code ```.py```
#    
# and many more.

# ### 🤖 Try it!
# 
# **Export this notebook as an html file and view it in your browser.**

# ---

# ## Requirements / Packages used in session

# In[39]:


import session_info
session_info.show()

