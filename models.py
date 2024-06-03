 

import requests
from bs4 import BeautifulSoup
import pinecone

# Initialize Pinecone
pinecone.init(api_key="your-api-key", environment="us-west1-gcp")

# Create a new Pinecone index
index_name = "web-scraping-index"
pinecone.create_index(index_name, dimension=512)
index = pinecone.Index(index_name)

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract relevant information (e.g., paragraphs, titles)
    texts = soup.find_all('p')
    return [text.get_text() for text in texts]

def store_in_vector_db(texts):
    for text in texts:
        vector = embed_text(text)  
        index.upsert([(text, vector)])

def embed_text(text):
    # Use Pinecone's embed function to convert text to vector
    return pinecone.embed(text, model="mpnet-base")

# Example usage
texts = scrape_website("http://example.com")
store_in_vector_db(texts)