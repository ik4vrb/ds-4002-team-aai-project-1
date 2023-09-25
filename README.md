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
All code used for this project can be found in the [SRC](https://github.com/ik4vrb/ds-4002-team-aai/tree/main/SRC) folder.

### Code Installing/Building 
This project was created using Python. Here are the steps:
  1. Do a git clone or download the zip file to install everything.
  2. Open the EDA_project1.py file in an IDE that runs Python.
  3. Proceed by running the code, which will execute the code and output results for the syntax analysis.
  4. Open the Data_Analysis.ipynb file in an IDE that runs Python, preferably Jupyter Notebook or something similar to that.
  5. Run every chunk of the Data_Analysis.ipynb to output results for various sentimental analyses.
  6. NOTE: If the pd.read_csv does not work, append "Data/" to the beginning of the string in the input. (EX: "Data/Top25_Books_Data - Sheet1.csv" in the second chunk)
  7. An alternative to step 6 would be to move the files from Data into the same directory as the Data_Analysis.ipynb file.

### Code Usage
There are two files in the SRC folder:
  1. The first one is called EDA project 1 and contains the intial EDA conducted on our data.
  2.  The second file is called Data Analysis that consists of the sentiment and syntax analysis conducted on the book intructions.

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
|      2          | Sentiment Score per Book Title | This graph contains the individual sentiment score for each of the books used in the analysis. The graph demonstrates how all of the 25 intruductions that were anlyzed are close to 0 meaning that most of them were neutral in sentiment. |
|      3          | The Average Parts of Speech Across 25 Introductions|               |
|      4          | Sentiment Score per Genre| This graph contains the sentiment scores for each of the genres that were present for the 25 books. The graph demonstrates that most of the scroes were close to 0 meaning that the introductions were netural in sentiment; however, we can also see that most descriptions are above 0 meaning that they scored a little bit more positive in sentiment. |


## Reference
[1] “Vote For the Best Book,” The New York Times, November 24, 2024. [Online], Available: https://www.nytimes.com/interactive/2021/11/24/books/best-book-vote.html. [Accessed Sept. 18, 2023].

[2] Project Goal: [M1 Project 1](https://docs.google.com/document/d/1i4sS1NQyEUDuwy_ixIY1v-LkcXKPx7PHKQ6wzbPDzV4/edit?usp=sharing)

[3] Establish Data & Analysis Plan: [M2 Project 1](https://docs.google.com/document/d/1cel0WBVufGpupIIiwYumxygtfpUAnK3bwc2n_Wfrvc8/edit?usp=sharing)
