

import pinecone

# Initialize Pinecone
pinecone.init(api_key="your-api-key", environment="us-west1-gcp")

 
index_name = "web-scraping-index"
pinecone.create_index(index_name, dimension=512)
index = pinecone.Index(index_name)

async def process_prompt(prompt):
 
    search_results = query_vector_db(prompt)
 
    new_prompt = f"Search results: {search_results}\nUser query: {prompt}"

    responses = query_llms(new_prompt)
 
    return responses

def query_vector_db(query):
 
    results = index.query(queries=[query], top_k=5)
 
    ids, scores = zip(*results[0])
 
    texts = [index.fetch([id_])[id_][0] for id_ in ids]
  
    return ", ".join(texts)