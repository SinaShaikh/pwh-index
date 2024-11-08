##############################
## PWH Belize
## Sina Shaikh
##############################

# Setting Working Directory
setwd("~/Desktop/PWH")

# Requires some standard libraries
library(rio)
library(tidyverse)
library(dplyr)
library(ggplot2)
library(MASS)
library(ppcor)
library(textstem)



# Load in data
master <- read.csv("Master.csv")

table

for (i in 1:nrow(master)){
  master[i] = strsplit(master[i,],split = '/')
  print(master[i])
}


