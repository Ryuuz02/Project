Abstract 
Development Summary: An application designed to be able to crawl web pages, index them according to their contents, and use inputs to return relevant web pages to a user’s query.

Objectives: 
First component: Have a functional spider using Scrapy, that is able to crawl a user inputted web domain/page, and store the information for later use. Also allow the user to choose the maximum depth and pages that the crawler will look at. 
Second component: Make an indexer using sk-learn in order to take the crawled web pages in html form and create an inverted index using them. Additionally, use tfidf scores and cosine similarities scores in order to compute most relevant results.
Third Component: Take the scores and content from steps 1 and 2 to make a query processor using flask. The processor will then prompt the user for a query for it to act on, and return relevant web pages using their scores to the user. Additionally, checks for input errors in the query, and allows the user to ask for the k-highest ranking results.

Next Steps: Limit the content that is crawled to just the main page. Currently it crawls and copies the entire page, including things like ads, or links to other sites, or other unrelated pages that can throw off the relevant results (Though generally not too much). Additionally generalize for it to be used more modularly.
Overview 
Solution Outline: In the crawler, take in user input from the command line using os, and design the crawler to be able to use adaptable values for variable values. For the indexer, make two separate files for easier understanding. One file creates the inverted index, while the other one makes the tfidf matrix and calculates cosine similarity scores. The processor will use a host program running on flask in order to take requests to a local host for the query and the value k. A second partner program will be ran to request information from the local host using queries.

Relevant Literature: Read through the Operation section for learning how to use the program. Additionally, skim through the web page that you are inputting to ensure that it is what you are looking for, and how to modify the content searching values to fit the webpage.

Proposed System: A 3 component system that progresses from one step to the next using the files created from the previous steps. Effectively following the solution outline given above.
Design
System Capabilities: By default, The crawler crawls the webpage and will look for any <div class=floatleft> links to secondary sites. The secondary sites will then be crawled and stored in a folder for the html_docs. The inverted index will then look at those saved pages and create an inverted index dictionary and store it as a .pkl file. The tfidf indexer will do the same, but creating a tfidf matrix .pkl instead, for use in the processor. The processor will take in queries and return k relevant web pages that were passed in the crawler. The documents are listed by number, but they are in order for the folder (so document #3 is the third document in the folder the crawler created)

Interactions: Uses a feed-forward system where the outputs of step 1 (crawler) is used for step 2 (indexer), and both outputs for steps 1 and 2 are used in step 3 (processor). 

Integration: No direct integration of any files outside of itself or used outside of itself. Only exception would technically be the processor, since it works off a localhost server, so a different program that also sent requests to http://localhost:5000/query would also be able to interact with the processor.
Architecture
Software Components: 5 total python files, consisting of the crawler, inverted index, tfidf indexer, flask processor, and query request. They output multiple .pkl files that are later used as inputs as well along with a folder of .html files from the crawler based on the web pages crawled.
Interfaces: Uses the command line, or terminal equivalent per the user’s machine. No built-in interfaces for any elements.
Implementation: Similar to integration, does not directly implement or is implemented by any application, aside from python and its packages listed below.
Operation
Software Commands:
Crawler: Open a command line/terminal on the spider folder “Tutorial”. Then use the command as given. scrapy crawl Ryuzu -a url=(insert webpage here) -a max_depth=(insert max_depth here) -a max_pages=(insert max_pages here), replacing the parenthesized parts with the values you wish to replace them with. The max_depth and max_pages will default to extending infinitely.
Inverted Indexer: Call the python file from either an IDE or from a command line. From the command line use “python inverted_indexer.py” while in the directory the file is stored in. 
Tfidf indexer: Call the python file from either an IDE or from a command line. From the command line use “python tfidf_indexer.py” while in the directory the file is stored in. This can also be used to find the cosine similarity from two terms in the vocabulary, by replacing the marked variables in the file. Alternatively, you can comment those variables out and uncomment the input lines below to do the same, but asking for the user to input their own values for it to find cosine similarity instead. With a little expertise, you can also separate the cosine similarity from the tfidf indexer.
Flask Processor: Call the python file from either an IDE or from a command line. From the command line use “python Flask_Processor.py” while in the directory the file is stored in. This is used in tandem with the “Query_Request.py” file, so you will need to keep this running while using the 2nd file.
Query Request: Call the python file from either an IDE or from a command line. From the command line use “python Query_Request.py” while in the directory the file is stored in while the flask processor is running. This will then prompt the user for their input query and k value, can be repeated for multiple queries.

Inputs: Covered above in the software commands

Installation: Need the folder from the github, which comes with pre-indexed values and default test values for variables. You also need python 3.10+. For dependencies, you need flask, sklearn, pickle, os, bs4, Scrapy, path, and requests. Multiple of which are included by default in python.
Conclusion 
Success/Failure Results: 
Crawler: On success, the crawler will make a folder with new .html files included for each of the webpages crawled. Failure will return an error message.
Inverted Indexer: On success will create the inverted_index.pkl file, failure will return an error
Tfidf Indexer: Will output the cosine similarity of the given terms on success and create tfidf matrix, failure will return an error message
Flask Processor: On success, will await the query from query_request.py, leaving it running. Failure will return an error and stop running
Query Request: Success will return the web pages that match your query up to k, failure will return an error and status code.

Outputs: As above

Caveats/Cautions: The structure used for the crawler is built for https://leagueoflegends.fandom.com/wiki/List_of_champions, but will work for anything that uses <div class=floatleft> links, although the naming conventions might be a bit off. In order to make it work for other webpages, just adjust the html element (<div class=floatleft>) to the location of the links on the webpage.
Data Sources 
Links: https://leagueoflegends.fandom.com/wiki/List_of_champions for the webpages used. 

Downloads: https://github.com/Ryuuz02/Project/tree/main, https://www.python.org/downloads/ downloads for packages are from pip

Access Information: 
https://flask.palletsprojects.com/en/3.0.x/ 
https://scrapy.org 
https://scikit-learn.org/stable/
https://docs.python.org/3/library/pickle.html 
https://pypi.org/project/beautifulsoup4/ 
Test Cases
For test cases, test different values of max_pages and max_depth and different webpages. Do note, that you will likely need to adjust the crawler to look for the new elements of the webpage.
Source Code 
Documentation: See access information above.
Dependencies: Flask, sklearn, pickle, os, bs4, Scrapy, path, and requests. Multiple of which are included by default in python.

Bibliography
“A Fast and Powerful Scraping and Web Crawling Framework.” Scrapy, scrapy.org/. Accessed 22 Apr. 2024.
“Learn.” Scikit, scikit-learn.org/stable/. Accessed 22 Apr. 2024.
“Welcome to Flask¶.” Welcome to Flask - Flask Documentation (3.0.x), flask.palletsprojects.com/en/3.0.x/. Accessed 22 Apr. 2024. 

