# imports
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Function to extract text from HTML files
def extract_text_from_html(html_files):
    #Extract text content from HTML files in a directory.
    html_texts = []
    for file in html_files:
        # have to use utf-8 encoding to avoid UnicodeDecodeError
        with open('html_docs/' + file, 'r', encoding="utf-8") as file:
            html_text = file.read()
            html_texts.append(html_text)
    return html_texts

def preprocess_text(html_texts):
    # {rocess text data using CountVectorizer.
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(html_texts)
    terms = vectorizer.get_feature_names_out()
    return X, terms

def create_inverted_index(X, terms):
    # Create the inverted index.
    inverted_index = {}
    for i, term in enumerate(terms):
        doc_indices = X[:, i].nonzero()[0]
        inverted_index[term] = list(doc_indices)
    # example of how to access the inverted index for coding purposes
    # sweet_spot = inverted_index["sweetspot"]
    # for i in sweet_spot:
    #     print(html_files[i])
    return inverted_index

def save_inverted_index(inverted_index, output_file):
    #Serialize and save the inverted index to a pickle file.
    with open(output_file, 'wb') as file:
        pickle.dump(inverted_index, file)

# Main function
def main(html_dir, output_file):
    # Step 1: Extract text from HTML files
    html_texts = extract_text_from_html(html_dir)
    
    # Step 2: Preprocess text
    X, terms = preprocess_text(html_texts)
    
    # Step 3: Create the inverted index
    inverted_index = create_inverted_index(X, terms)
    
    # Step 4: Save the inverted index to a pickle file
    save_inverted_index(inverted_index, output_file)

# Call the main function
html_files = os.listdir('html_docs/')
output_file = 'inverted_index.pkl'
main(html_files, output_file)
