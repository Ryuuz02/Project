# Imports
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity

# Parse HTML Files
html_files = os.listdir('html_docs/')
text_data = []

for file in html_files:
    with open("html_docs/" + file, 'r', encoding='utf-8') as f:  # Specify the encoding explicitly
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text()
        text_data.append(text)

# Construct TF-IDF Matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_data)
terms = vectorizer.get_feature_names_out()

# Save TF-IDF Matrix and Terms
with open('tfidf_matrix.pickle', 'wb') as f:
    pickle.dump(X, f)

with open('terms.pickle', 'wb') as f:
    pickle.dump(terms, f)

with open('vectorizer.pickle', 'wb') as f:
    pickle.dump(vectorizer, f)

# Example Query
# print(vectorizer.vocabulary_["sweetspot"]) <- This will give you the index of the term "sweetspot" in the TF-IDF matrix
# print(terms[20278]) <- This will give you the term at index 20278 (which happens to be sweetspot in our example)
# print(X[0, 20278]) <- This will give you the TF-IDF value of the term "sweetspot" in the first document

term1 = "tibbers" # Change these terms to the ones you want to compare
term2 = "stun" # Change these terms to the ones you want to compare

# Can also use the inputs below to ask the user for the terms
# term1 = input("Enter the first term: ")
# term2 = input("Enter the second term: ")

# Get the indices of the terms in the TF-IDF matrix
term1_index = vectorizer.vocabulary_[term1]
term2_index = vectorizer.vocabulary_[term2]

# Retrieve the TF-IDF vectors for the two terms
tfidf_vector_term1 = X[:, term1_index].reshape(1, -1)  # Reshape to row vector
tfidf_vector_term2 = X[:, term2_index].reshape(1, -1)  # Reshape to row vector

# Compute cosine similarity between the TF-IDF vectors
cosine_sim = cosine_similarity(tfidf_vector_term1, tfidf_vector_term2)

# Print the cosine similarity
print("The cosine similarity between " + term1 + " and " + term2 + " is: " + str(cosine_sim[0][0]))
