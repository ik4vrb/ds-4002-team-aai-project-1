# Sentiment and Syntatic Analysis across Introductions to Popular Books

### Project Information
  - DS 4002
  - Project 1
  - Team: AAI
  - This repository is a collaboration between Ishan Koroth, Ashley Huang, and Ana Cristina Cordova for DS 4002 Project 1

## Context

A journey of a thousand pages begins with a single sentence. This single sentence is part of a hook. The purpose of the hook is to entice the reader to continue on their journey i.e. read the book. The hook leaves the first impression of the novel on the reader. Like how first impressions matter, so does the hook. There are many, many ways to write a hook. However, because there’s many ways to write a hook, it makes writing a good hook particularly difficult. Therefore, with all the ways to write a hook, are there hidden elements that differentiate between a hook and a great hook? What do the hooks of the most acclaimed novels have in common?

In order to be able to conduct this analysis, we gathered the hooks from the best 25 novels over the course of the past 125 years. The list of the top 25 books was published by the New York Times. This are the 25 novels that we will be analyzing:
  - Nineteen Eighty-Four by George Orwell
  - All the Light We Cannot See	by Anthony Doerr
  - Beloved	by Toni Morrison
  - Catch-22 by Joseph Heller
  - The Chatcher in the Rye	by J.D. Salinger
  - Charlottes's Web	E.B. White
  - A Confederacy of Dunces	 by John Kennedy Toole
  - The Fellowship of the Ring	by J.R.R. Tolkein
  - A Fine Balance	by Rohinton Mistry
  - A Gentleman in Moscow	by Amor Towles
  - A Fine Balance	by Rohinton Mistry
  - Gone With the Wind	by Margaret Mitchell
  - The Grapes of Wrath by	John Steinbeck
  - The Great Gatsby	by F. Scott Fitzgerald
  - The Handmaid’s Tale	by Margaret Atwood
  - Harry Potter and the Sorcerer’s Stone	by J.K. Rowling
  - Infinite by Jest	David Foster Wallace
  - To Kill a Mockingbird	by Harper Lee
  - A Little Life by Hanya Yanagihara
  - Lolita	by Vladimir Nabokov
  - Lonesome Dove	by Larry Mcmurtry
  - One Hundred Years of Solitude by Gabriel Garcia Marquez
  - The Overstory by	Richard Powers
  - A Prayer for Owen Meany	 by John Irving
  - A Tree Grows in Brooklyn	by Betty Smith
  - Ulysses	by James Joyce


## Repository Contents 
 - Make an H2 (##) section explaining the contents of the repository
 - SRC section
 - Make an H3 section for Installing/Building your code
 - Make an H3 section for Usage of your code
 - 
All code used for this project can be found in the [SRC](https://github.com/ik4vrb/ds-4002-team-aai/tree/main/SRC) folder.
### Code Building 

### Code Usage
There are two files in the SRC folder:
  1. The first one is called EDA project 1 and contains the intial EDA conducted on our data.
  2.  The second file is called Data Anlysis that consists of the sentiment and syntax analysis conducted on the book intructions.

## Data
All the data for this project can be found in the [Data](https://github.com/ik4vrb/ds-4002-team-aai/tree/main/Data) folder.

### Main Data Set
For this project there was one main data set containg information about the top 25 books over the last 125 years. The data dictionary for this data set is the following:

|    Column     |  Description  |
| ------------- | ------------- |
| Response_id    | Book ID for each individual book |
| Story_name     | The novel title |
| Author         | The name of the author for each book |
| Year_published | The year the book was published |
| Genre          | A general genre the book belong to |
| Response       | Around the first 250 word of each book |
| num_words      | The exact number of words that the hook has |

### List of Words
For the inital EDA, a list of around 1000 positive and negative words is needed. The data dictionary for this data set is the following:

|    Column     |  Description  |
| ------------- | ------------- |
| word          | A single word |
| category      | Whether the word is positive or negative |


## Visualizations 
All data visulaizations are found in the [Visualizations](https://github.com/ik4vrb/ds-4002-team-aai/tree/main/Visualizations) folder. 

|    Figue ID     |  Figure Name  |  Description  |
| ----------------| ------------- | ------------- |
|      1          | Sentiment Score vs Subjectivity Score |               |
|      2          | Sentiment Score per Book Title |               |
|      3          | The Average Parts of Speech Across 25 Introductions|               |
|      4          | Sentiment Score per Genre|               |


## Reference
[1] “Vote For the Best Book,” The New York Times, November 24, 2024. [Online], Available: https://www.nytimes.com/interactive/2021/11/24/books/best-book-vote.html. [Accessed Sept. 18, 2023].

[2] Project Goal: [M1 Project 1](https://docs.google.com/document/d/1i4sS1NQyEUDuwy_ixIY1v-LkcXKPx7PHKQ6wzbPDzV4/edit?usp=sharing)

[3] Establish Data & Analysis Plan: [M2 Project 1](https://docs.google.com/document/d/1cel0WBVufGpupIIiwYumxygtfpUAnK3bwc2n_Wfrvc8/edit?usp=sharing)
