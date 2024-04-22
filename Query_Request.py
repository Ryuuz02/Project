# imports
import requests

# URL of your Flask app's query endpoint
url = 'http://localhost:5000/query'

# Get user input for query and number of documents to retrieve
input_query = input("Enter your query: ")
input_k = input("Enter the number of documents to retrieve: ")
query_data = {
    "query": input_query, # Input query
    "k": input_k # Number of documents to retrieve
}

# Send POST request with JSON data
response = requests.post(url, json=query_data)

# Check if request was successful
if response.status_code == 200:
    # Print the processed result
    print("Result:", response.json())
else:
    # Print the error message
    print("Error:", response.text)
