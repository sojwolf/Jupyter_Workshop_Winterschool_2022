#!/usr/bin/env python
# coding: utf-8

# # Publish your workflow as Jupyter Book

# Most of this content was taken from the Jupyter Book documentation: https://jupyterbook.org/en/stable/start/overview.html

# ## Install Jupyter Book

# First, install Jupyter Book via pip:

# In[ ]:


get_ipython().system('pip install -U jupyter-book')


# or via conda-forge:

# In[ ]:


get_ipython().system('conda install -c conda-forge jupyter-book')


# ## Create Book

# ### Create first template

# In[7]:


get_ipython().run_cell_magic('bash', '', '\njupyter-book create JupyterTutorial/\n')


# ### Customize the template

# Open the NewJupyterBook/ directory and open the ```_config.yml``` file and the ```_toc.yml``` file.

# Edit your ```_toc.yml``` (table of conents) file by adding the jupyter notebook and markdwon file names. You do not need to add the ```*.ipynb``` endings. Here is an example: 

# <img align="left" src="Figures/toc.png" width="500" >

# For more structure options (sub-sections, chapters etc.), refer to https://jupyterbook.org/en/stable/structure/toc.html

# Next, edit the ```_config.yml``` file.
#     
#  - change the title
# - the author name
# - set excectue to ```'off'```, if you do not want jupyter book to rerun all your code. Otherwise set to ```force```. This will rerun your code as it builds the book. 

# <img align="left" src="Figures/config.png" width="700" >

# ## Build Book

# Check that you are in the directory that contains your book's root folder:

# In[24]:


get_ipython().system('ls')


# In[25]:


get_ipython().system('jupyter-book build JupyterTutorial/')

