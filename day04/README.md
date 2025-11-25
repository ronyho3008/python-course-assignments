# ☑️ UniProt It has never been easier
---
## A brief introduction
First and foremost In order to remove the __pycache__ folders, I deleted all the folders already installed on the computer and added a file.
Now we can start 😮‍💨

At first, I tried to perform the task on sites that I know and use often, such as AliExpress 🛍️ and recipes 🍳 sites. 
Unfortunately, scraping these sites did not yield results because they do not allow downloading data and do not have an open public API.
Therefore, I moved on to more biological sites 🧫 and chose the UniProt site

## UniProt
[UniProt](https://www.uniprot.org/) is a large free database of protein sequences and functional information about them. 
in the website you can find:
- Detailed information on proteins from across the living world, including names, sequences, structures, and functions
- Extensive biological annotations collected from research and other data sources
- Searches and displays of differences between various isoforms of the same protein
- Tools for searching and comparing proteins from different sources

I use the site to get more information about proteins that I work with in the lab, compare sequences, and more.
And most importantly, the input it receives is simple, you can download the information from it in JSON and it has an open and clear API!

## Writing the program using ChatGPT
Then I turned to ChatGPT with instructions for writing the codes divided into files:
1. logic.py - Contains all the business logic of the program, downloading the data from the site and saving it locally in a Json file.
2. main.py - The UI where you can type in the name or ID number of a protein and get information about it in a new Json file.

I felt that the UI file was not convenient enough for me, so I also added a gui file

3. gui.py - Opens a new window that allows for a convenient search by protein name or serial number and provides the name of the protein, the relevant organism, its length, and also allows you to download the sequence and save the information in an Excel file

And that's it for this week 🎊
![pic](https://ace-lifestyle.com/wp-content/uploads/2020/10/Proteins-meme-1.jpg)
