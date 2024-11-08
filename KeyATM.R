##############################
## PWH Keyword Assisted Topic Model
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

# Install release version from CRAN (updating keyATM is the same command)
library(quanteda)
library(readtext)
library(devtools)
library(keyATM)

raw_docs <- readtext("ATMTextFiles/*.txt",
                     encoding = "UTF-8")

# Preprocessing with quanteda and create a dfm object
key_corpus <- corpus(raw_docs, text_field = "text")

# You can conduct a variety of types of preprocessing in this step as shown in the next section
key_token <- tokens(key_corpus)

# Create a document-feature matrix (a dfm object) from a token object
key_dfm <- dfm(key_token)

#Tokenize
data_tokens <- tokens(
  key_corpus,
  remove_numbers = TRUE,
  remove_punct = TRUE,
  remove_symbols = TRUE,
  remove_separators = TRUE,
  remove_url = TRUE
) %>%
  tokens_tolower() %>%
  tokens_remove(
    c(stopwords("english"),
      "may", "shall", "can",
      "must", "upon", "with", "without"
    )
  ) %>%
  tokens_select(min_nchar = 3)

data_dfm <- dfm(data_tokens) %>%
  dfm_trim(min_termfreq = 5, min_docfreq = 2)
ncol(data_dfm)  # the number of unique words

keyATM_docs <- keyATM_read(texts = data_dfm)
summary(keyATM_docs)


out <- keyATM(
  docs              = keyATM_docs,    # text input
  no_keyword_topics = 2,              # number of topics without keywords
  keywords          = list("economic"),       # keywords
  model             = "base",         # select the model
  options           = list(seed = 250)
)

plot_topicprop(out, show_topic = 1:3)

top_docs(out)
