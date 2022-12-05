#!/usr/bin/env python
# coding: utf-8

# # Data Analysis in Jupyter Notebook (Part 2)

# We will reproduce parts of a recent publication:
# 
# Wolf, S. and Mahecha, M. D. and Sabatini, F. M. and Wirth, C. and Bruelheide, H. and Kattge, J. and Moreno Martínez, Á. and Mora, K. and Kattenborn, T., **Citizen science plant observations encode global trait patterns**. Nat Ecol Evol (2022). https://doi.org/10.1038/s41559-022-01904-x
# 
# The full documentation can found at: https://github.com/sojwolf/iNaturalist_traits

# ## Research question

# Can we use citizen science plant observations to map plant functional traits on a global scale?

# Plant traits are morphological, anatomical, physiological, biochemical and phenological characteristics of plants. They determine how a plant responds to and shapes its environment. The collective range of all traits of all plants within a plant community defines this community's functional diversity (see Kattge et al. 2020).

# <img align="left" src="Figures/Winterschool_tutorial.jpg" width="900" >

# ## The Data

# - iNaturalist - species observations
# - TRY - plant trait measurements
# - sPlotOpen - vegetaiton community data

# ## iNaturalist citizen science observations

# For this workshop we will use the following download: GBIF.org (4 January 2022) GBIF Occurrence Download https://doi.org/10.15468/dl.34tjre
# 
# For future reference, if you would like to use the most recent data: Follow the above link and click **'Rerun Query'** and proceed to download. For this analysis the 'simple' version is sufficient.

# ### 🤖 Try it!
# 
# **Take a few minutes to explore iNaturalist "research-grade" dataset on www.gbif.org.**
# 
# **1. How is "research-grade" defined in the iNaturalist dataset?**
# 
# **2. Rerun the query - how many vascular plant observations are in the iNaturalist "research-grade" dataset to date?**
# 

# For this tutorial, the following dataframe is already preprocessed a bit. Only the following columns were extracted and we will disregard subspecies level: the species names contain only genus and species.
# 
# - gbifID
# - scientificName
# - decimalLatitude
# - decimalLongitude
# - eventDate
# - dateIdentified

# In[2]:


get_ipython().run_line_magic('ls', '')


# In[ ]:


import pandas as pd # for handling dataframes in python

iNat = pd.read_csv('Data/iNat/observations.csv')


# In[1]:


iNat.head()


# ### 🤖 Try it!
# 
# **1. How many observations does this dataset contain?**
# 
# **2. How many unique species?**
# 
# **3. The number of observations per unique species is highly squewed. Most species are rare and few are common. Plot a histogramm showing this frequency distribution of species.**
# 

# In[4]:


# Number of observations in dataset


# In[5]:


# Number of unique species


# In[6]:


# Histogram of species frequencies


# ---

# ### Plot density of observations

# One version of plotting the density, is by aggregating the iNaturalist observations in hexagonal bins and count the number of observations per hexagon. The function ```hexbin``` provides this functionality.

# In[7]:


import matplotlib.pyplot as plt # main Python plotting library 
import seaborn as sns # pretty plots
import cartopy.crs as ccrs # maps 

def hexmap(long, lat, label):
    
    ax = plt.subplot(projection=ccrs.PlateCarree())
    
    # hexbin aggregates observations in hexagonal bins and plots the density
    hb = ax.hexbin(long,
          lat, 
          mincnt=1, # min. nuber of observations per hexagon 
          gridsize=(100, 30), # bin size
          cmap="cool", 
          transform=ccrs.PlateCarree(), 
          extent=[-180, 180, -90, 90],
          linewidths=0.1)
    
    # add coastline outline and extent of map:
    ax.coastlines(resolution='110m', color='orange', linewidth=1)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    
    cb = fig.colorbar(hb, ax=ax, shrink=0.4)
    cb.set_label(label)


# Apply the ```hexmap``` function to our iNaturalist observations and save output as ```.pdf```:

# In[8]:


#determine figure size
fig = plt.figure(figsize=(10, 10))
hexmap(iNat['decimalLongitude'], iNat['decimalLatitude'], "Number of iNatrualist Observations")

#optional: Save figure
#plt.savefig('iNat_density_hex.pdf', bbox_inches='tight')


# ### 🤖 Try it!
# 
# **The frquency distribution of observations seems to be skewed. Change the color bar to log-scale.**
# 
# Hint: Look up ```matplotlib.axes.Axes.hexbin```.

# ---

# A second plotting option is to grid the data into a latitude/longitude grid. Then we can project our map onto a more realistic representation of the spherical Earth, such as the Robinson projection. The previously used ```hexbin``` function does not have a reprojection functionality implemented.

# In[9]:


from matplotlib.colors import LogNorm, Normalize, BoundaryNorm
import cartopy.feature as cfeature # maps
import numpy as np

def gridmap(long, lat, label, projection, colorbar=True):
    
    plt.rcParams.update({'font.size': 15})

    Z, xedges, yedges = np.histogram2d(np.array(long,dtype=float),
                                   np.array(lat),bins = [181, 91])

    #https://stackoverflow.com/questions/67801227/color-a-2d-histogram-not-by-density-but-by-the-mean-of-a-third-column
    #https://medium.com/analytics-vidhya/custom-strava-heatmap-231267dcd084
    
    #let function know what projection provided data is in:
    data_crs = ccrs.PlateCarree()
    
    #for colorbar
    cmap = plt.get_cmap('cool')
    im_ratio = Z.shape[0]/Z.shape[1]

    #plot map
    #create base plot of a world map
    ax = fig.add_subplot(1, 1, 1, projection=projection) # I used the PlateCarree projection from cartopy
    
    # set figure to map global extent (-180,180,-90,90)
    ax.set_global()

    
    #add grid with values
    im = ax.pcolormesh(xedges, yedges, Z.T, cmap="cool", norm=LogNorm(), transform=data_crs)
    
    #add coastlines
    ax.coastlines(resolution='110m', color='orange', linewidth=1.3)
    
    #add color bar
    if colorbar==True:
        fig.colorbar(im,fraction=0.046*im_ratio, pad=0.04, shrink=0.3, location="left", label=label)



# Apply the ```gridmap``` function to our iNaturalist observations and save output as ```.pdf```. You can also experiment with other projections. See https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html for inspiration:

# In[11]:


fig = plt.figure(figsize=(12, 12))

gridmap(iNat['decimalLongitude'], iNat['decimalLatitude'], "Number of iNatrualist Observations", ccrs.Robinson(0))

#Optional
#plt.savefig('/Figures/iNat_density_Robinson.pdf', bbox_inches='tight')


# ### 🤖 Try it!
# 
# **Take a few minutes to play around with this function:**
# 
# **1. Change the projection of the map.** Hint: Look up "cartopy ccrs projections".
# 
# **2. Change the colors of the map.**
# 
# **Extra credit: Filter the iNaturalist dataset for a species of your interest and plot its global distribution as documented by citizen scientists.** Hint: 
# 
# To subset df: ```df[df['column_name']=="your species name"]```
# 
# Get list of 10 most common species: ```iNat['scientificName'].value_counts()[:10].index.tolist()```

# ---

# ## Make global trait maps

# In[2]:


# enables the %%R magic, needs to be installed and then activated only once per Notebook 
get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# In[ ]:


get_ipython().run_cell_magic('R', '', "\n# Load iNat Data\niNat <- data.table::fread('Data/iNat_TRY_log.csv', data.table=F, showProgress=F)\ngc()\n")


# In[36]:


get_ipython().run_line_magic('R', 'head(iNat)')


# In[37]:


get_ipython().run_cell_magic('R', '', '\nlibrary(raster)\n\n# get coordinates\nxy <- cbind(iNat$decimalLongitude, iNat$decimalLatitude)\n# raster dimensions 2 degree resolution map\nr2 <- raster(ncols = 180, nrows = 90)\n')


# In[38]:


get_ipython().run_cell_magic('R', '', '\nloop.vector <- 7:24 # loop over trait columns in dataframe\nloop.vector\n')


# In[39]:


get_ipython().run_cell_magic('R', '', '\n# export exp(ln()) maps in GeoTiff format\n\nfor (i in loop.vector) { # Loop over loop.vector\n    vals <- iNat[,i]\n    name <- colnames(iNat[i])\n    # create a raster of all data and aggregate all observations as mean\n    raster2 <- rasterize(xy, r2, vals, fun = mean)\n    raster2[is.infinite(raster2)] <- NA\n    crs(raster2) <- "+proj=longlat" #set projection\n    \n    # plot raster to check output\n    plot(raster2, main=name)\n    \n    # write raster to GeoTiff\n    filename = paste(name, "_iNat_2deg_ln.tif", sep="")\n    writeRaster(raster2, filename, overwrite=TRUE)\n\n}\n')


# ## The global spectrum of plant form and function

# 

# **a)** Díaz et al. 2016
# 
# <img align="left" src="Figures/Diaz_2016_spectrum.png" width="600" >
# 

# **b)** Bruelheide et al. 2018
# 
# <img align="left" src="Figures/Bruelheide_2018_spectrum.png" width="600" >
# 

# In[40]:


get_ipython().run_cell_magic('R', '', '\nfiles <- list.files(path=".", pattern="_iNat_2deg_ln.tif", all.files=FALSE, full.names=TRUE, recursive=TRUE)\ns <- stack(files)\n')


# In[41]:


get_ipython().run_cell_magic('R', '', 'files\n')


# In[42]:


get_ipython().run_cell_magic('R', '', 'trait_names <- c(files)\ntrait_names <- gsub("*_iNat_2deg_ln.tif", "", trait_names)\ntrait_names <- gsub(".*./", "", trait_names)\n\nnames(s) <- trait_names\ns\n')


# In[43]:


get_ipython().run_cell_magic('R', '', '\ndf = as.data.frame(s)\nhead(df, 3)\n')


# In[44]:


get_ipython().run_cell_magic('R', '', ' \nsummary(df)\n')


# In[45]:


get_ipython().run_cell_magic('R', '', '\nlibrary(pcaMethods)\n\n# convert back to original dimensions\ndf_exp <- exp(df)\n\n# remove rows where all are NA\ndf_exp <- df_exp[rowSums(is.na(df_exp)) != ncol(df_exp), ]\n\n# scale all variables\ndf_st <- scale(df_exp)\n\n# calculate probobalistic pca\nresult <- pca(df_st, method="ppca", nPcs=2) #includes a mean tranform\nscores <- scores(result)\nloadings <- loadings(result)\n')


# In[46]:


get_ipython().run_cell_magic('R', '', 'result\n')


# In[47]:


get_ipython().run_cell_magic('R', '', '\nbiplot(result,  xlabs = rep(".", nrow(df_st)), xlim=c(-0.07, 0.10), ylim=c(-0.06, 0.065), cex=0.7, col=c(\'grey\', \'red\'))\n')


# ### 🤖 Try it!
# 
# **1. Optimize this biplot to make it more ledgible. Use R or use ```%Rget``` to use the results with Python.**
# 
# **2. Plot the variance explained by each principle component. The code above calculates only the first two, you might want to change this.**
# 
# **3. This PCA represents the so-called spectrum of plant form and function. Compare your biplot visually to the the previously published versions based a) on only TRY trait data and b) sPlotOpen community data (see figures above).**
# 

# In[ ]:




