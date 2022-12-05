#!/usr/bin/env python
# coding: utf-8

# # Reuse of winter school practical course material
# 
# - Get material and data
# - Reuse options
#     - BinderHub
#     - Other options
#         - Home institution JupyterLab
#         - Local computer
# - Find and install missing requirements
#     - Installing an R kernel
#     - Install python packages
# - Repositories of all tutorials
# 
# 
# There are different ways of reusing and continuing with the material that you get in touch with in the winter school. This document serves as a rough guide to help you get rolling after the workshop. We show how you can get the scripts and the data and how you can place it into an environment in which you can continue to play with the material. We start with the easiest solution first but also want to highlight some options which require more time and knowledge from your side.
# 

# ## Get material and data
# 
# First of all we need to talk about getting the material. Each tutor prepared a Git repository with all the files that are relevant for their workshop part. In there you find e.g. the scripts and folders with files including data and documentation. You can simply click on the download button in a repository to download a Git repository as a zip file to get all the content. 
# 
# While that provides you with most of the things you need to get going there is one caveat. GitHub does not allow us to store large files. That means that we had to put large datasets somewhere else. So that also means you need to get them from somewhere else. This is indicated during the tutorial and one example of this is the dataset of Sophie Wolf.
# 
# https://syncandshare.desy.de/index.php/s/tTLLCnzbtCCpHot
# 
# 
# That is already nice you might say. However all above gets you only the original workshop files without your modifications. So let's see how you can preserve and work on with your own files. 
# 
# 
# You can export your work (e.g. .ipynb file) from a JupyterHub by clicking on File and selecting Download.
# 
# <img align="left" src="Figures/download.png" width="900" >
# 
# 
# 

# 
# **Interesting to know:** There is not only raw file based exports available. Other processed formats include e.g. html or PDF as shown below which can be handy in some cases giving you a nicely readable representation of your research.
#  
# 
# <img align="left" src="Figures/pdf.png" width="900" >
# 
# 
# 

# ## Reuse options
# 

# ### BinderHub
# 
# The easiest solution to continue with the material is to use the same system as we have been using. During the winter school we used a tool called BinderHub in order to enable you to work in your own JupyterLab environment including all requirements that it needed to execute the scripts properly. So what is BinderHub actually?
# 
# “Have a repository full of Jupyter notebooks? With Binder, open those notebooks in an executable environment, making your code immediately reproducible by anyone, anywhere.” *cited from their website*
# 
# So that means the tool takes a GitHub repository and turns it into a complete JupyterLab instance to work with. All that happens in a reliable and reproducible way. On https://mybinder.org you can also run the things that we have shown to you during the winter school. To get going:
# 
# 1. Get the original Github-Repository URL of your tutor (see at below)
# 2. Paste it into the form on BinderHub as we did in the winter school
# 3. Wait for the build process and starting of the environment (takes a while)
# 4. Get the modifies files (see above) upload it into the new environment
# 
# Just in case you are into GitHub. You can also create a copy of the original repository and use that one for further experimentation or to base your own work on the examples. For that:
# 
# 1. Get the original Github-Repository URL of your tutor (see below)
# 2. Copy the repository by creating a fork
# 3. Modify your copy to your liking (e.g. add your files from the winter school)
# 4. Then you copy the URL of your repository and go to step one above
# 
# 

# ### Other options
# 
# As said above there are some more options to work on with the material. However, not all might be the best way for a beginner to start with as they require some more work or a bit of technical background to set up and run.
# 

# #### Home institution JupyterLab
# 
# Sometimes you might be lucky and your home institution already runs a JupyterLab instance as a service for their employees. In that case you can simply ask how to get access and upload all the workshop data and the scripts to your account and you can start working with it. One thing you need to do to make the scripts work is to install additional python packages which are referenced in the scripts or special Jupyter packages which allow to run e.g. R-Code if you wish to do so. You can read the section further down or ask your IT for support. 
# 
# 
# 

# #### Local computer
# 
# If you want to use the workshop material on your local machine, you need to install a JupyterLab environment yourself. There are plenty of tutorials out there to do a basic setup. One would be:
# 
# https://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html
# 
# After installation of the environment you can open the workshop materials in your JupyterLab. For this navigate to the respective folder in your terminal and then launch Jupyter Lab like so:
# 

# In[ ]:


jupyter lab


# 
# That will make the current directory the working directory in JupyterLab and open a browser window that should look familiar to what you have seen at the winter school lessons:
# 
# <img align="left" src="Figures/launch.png"  >
# 
# 
# One thing you need to do in order to make the scripts work is to install additional python packages which are referenced in the scripts or also install special Jupyter packages which allow to run e.g. R-Code if you wish to do so. You can read the section further down or ask your IT for support. 

# ## Find and install missing requirements
# 
# 
# If you go with an institutional installation of JupyterLab or with a local one you will notice that you have to install all dependencies on your own. That includes python and R packages used in the scripts as well as additional kernels which enable it to run specific code like R. Don't worry you do not need to go through the script step by step and guess the requirements. In each of the repositories of your tutors you find a requirements file listing out what you need. You find the information either in a file in the folder named “binder”. The file itself then is called “environment.yml”. Or you find it in a file in the base folder of the repository where it is called “requirements.txt”
# 
# 
# In this example of an “environment.yml” file you can see the R and python dependencies. The R dependencies you can install via your R console followed by the python packages which you install via your preferred way of installing python packages (e.g. pip). 
# 
# ```
# # binder/environment.yml
# channels:
#   - conda-forge
#   - bioconda
# dependencies:
#   #R
#   - r-base=3.6
#   - r-tidyverse
#   - r-raster
#   - bioconductor-pcamethods
#   #Python
#   - numpy
#   - matplotlib
#   - pandas
#   - rpy2
#   - session-info
#   - seaborn
#   - cartopy
#   - rapidfuz`
# ```
# 
# 
# 

# ### Installing an R kernel
# 
# If you want to use an R kernel or R magic within a Python kernel, this has to be installed separately. You can install the IRkernel packages by running to the following command in an R console:
# 
# install.packages('IRkernel')
# 

# ### Installing R magic
# 
# You can install e.g. the R magic python package by running to the following command in the terminal:
# 

# In[ ]:


pip install rpy2


# Don’t forget to initialise R magic inside your python kernel notebook for it to work:

# In[ ]:


get_ipython().run_line_magic('load_ext', 'rpy2')


# ## Repositories of all tutorials
# 
# - Sophie Wolf, Data analysis in Jupyter Notebooks: https://github.com/sojwolf/Jupyter_Workshop_Winterschool_2022
# - Hanieh Saeedi https://git.ufz.de/winterschool/hs
# - Michael Öllermann https://github.com/pangaea-data-publisher/community-workshop-material
# 
# 
# 
# 
# 
