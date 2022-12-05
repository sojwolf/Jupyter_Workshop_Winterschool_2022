#!/usr/bin/env python
# coding: utf-8

# # Publish your workflow as a Jupyter Book

# The Jupyter Book is a great way to combine multiple analyses and document an entire workflow in html.
# 
# Here are some nice examples: https://executablebooks.org/en/latest/gallery.html
# 
# Most of the following content was taken from the Jupyter Book documentation: https://jupyterbook.org/en/stable/start/overview.html

# ## Install Jupyter Book

# First, install Jupyter Book via pip:

# In[ ]:


get_ipython().system('pip install -U jupyter-book')


# or via conda-forge:

# In[ ]:


get_ipython().system('conda install -c conda-forge jupyter-book')


# ## Create Book

# ### Create first template

# In[ ]:


get_ipython().run_cell_magic('bash', '', '\njupyter-book create JupyterTutorial/\n')


# ### Customize the template

# Open the NewJupyterBook/ directory and open the ```_config.yml``` file and the ```_toc.yml``` file.

# Edit your ```_toc.yml``` (table of conents) file by:
# 1. adding the jupyter notebook and markdwon file names. You do not need to add the ```*.ipynb``` endings. 
# 2. copy paste the notebook files to your book directory
# 3. keep intro file and customize it to your liking
# 4. delete all tem
# 
# Here is an example: 

# ![toc](Figures/toc.png)

# For more structure options (sub-sections, chapters etc.), refer to https://jupyterbook.org/en/stable/structure/toc.html

# Next, edit the ```_config.yml``` file.
#     
#  - change the title
# - the author name
# - set excectue to ```'off'```, if you do not want jupyter book to rerun all your code. Otherwise set to ```force```. This will rerun your code as it builds the book. 

# ![config](Figures/config.png)

# ## Build Book

# Check that you are in the directory that contains your book's directory:

# In[24]:


get_ipython().system('ls')


# Build your book

# In[51]:


get_ipython().system('jupyter-book build JupyterTutorial/')


# Navigate to ```JupyterTutorial/_build/html``` and open ```index.html``` to look at your book. It should look something like this:
# 
# ![jupyterbook](Figures/jupyterbook.png)

# ## Publish your book online

# There are many options to now incorporate the html code you have built into existing websites.
# 

# ### Publish inside your GitHub repository

# One easy and accessible and free way to publish your book is using GitHub pages:
# 
# 1. Create a new repository or navigate to an exisitng one
# 2. Create a directory ```docs``` in your repository's main directory
# 3. Copy paste the content ```BookName/_build/html``` to ```docs/```
# 4. Execute the following command inside the repository's main directory:

# In[ ]:


get_ipython().system('touch .nojekyll')
get_ipython().system('git add .nojekyll')


# Push all changes to GitHub.

# Now open your repository in a browser and make the following configurations:
# 
# 1. Click on Settings
# 2. Click on "Pages in the side bar"
# 3. Under "Source", choose "Deploy from branch"
# 
# ![settings1](Figures/settings1.png)

# 
# 4. Choose main branch and ```docs/```
# 
# ![settings2](Figures/settings2.png)

# 5. Click ```Save```
# 
# ![settings4](Figures/settings4.png)
# 

# Your site link will now be available at the top of the page. Sometimes it takes some time until the site is avialable:
# 
# ![settings3](Figures/settings3.png)
# 

# Click on the link to check out the result!
