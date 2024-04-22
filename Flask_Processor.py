# Imports
from flask import Flask, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle

# Create a Flask app
app = Flask(__name__)

# Load the TF-IDF matrix and terms from pickle files. Also load the vectorizer for the term vocabulary
with open('tfidf_matrix.pickle', 'rb') as f:
    X = pickle.load(f)

with open('terms.pickle', 'rb') as f:
    terms = pickle.load(f)

with open('vectorizer.pickle', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a route for the query endpoint
@app.route('/query', methods=['POST'])

# Process query function
def process_query():
    # Parse JSON data from the request
    query_data = request.json

    # Parse the input query into individual words
    query_words = query_data['query'].split()

    # Error checking
    if len(query_words) == 0:
        return " Query must contain at least one word", 400
    k = query_data['k']
    try :
        k = int(k)
    except:
        return " K must be an integer", 400
    if k < 1:
        return " K must be equal to or greater than 1", 400
    
    

    # Compute TF-IDF scores for each word in the query
    similarity_scores = []
    for doc_index in range(X.shape[0]):
        query_tfidf_scores = []
        for word in query_words:
            # Check if the word is in the term vocabulary
            if word in terms:
                word_index = vectorizer.vocabulary_[word]
                query_tfidf_scores.append(1 + X[doc_index, word_index])
            # If word not found, assign TF-IDF score of 1
            else:
                query_tfidf_scores.append(1) 

        # Compute the similarity score for the document
        similarity_score = 1
        for score in query_tfidf_scores:
            similarity_score *= score

        # Append the similarity score to the list
        similarity_scores.append(similarity_score)

    # Identify the document with the highest similarity score
    best_match_index = similarity_scores.index(max(similarity_scores))
    best_match_score = similarity_scores[best_match_index]

    # Return the best matching document and its similarity score and do it k times
    result = "\n"
    for i in range(k):
        best_match_index = similarity_scores.index(max(similarity_scores))
        best_match_score = similarity_scores[best_match_index]
        result += "#" + str(i + 1) + " Document is document " + str(best_match_index + 1) + " with a similarity score of " + str(best_match_score) + "\n"
        # Set the similarity score to -1 for the best match to avoid selecting it again
        similarity_scores[best_match_index] = -1

    # Return the result in JSON format
    return jsonify(result)

# Run the Flask app
app.run()