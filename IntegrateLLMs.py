 
import openai
openai.api_key = "your-api-key"

def query_llms(prompt):
    responses = {}
    # GPT-3.5 Turbo
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=prompt, max_tokens=150)
    responses["gpt-3.5-turbo"] = response.choices[0].text.strip()

    # GPT-4
    response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
    responses["gpt-4"] = response.choices[0].text.strip()

    # Add other models (Llama-2-70b-chat, Falcon-40b-instruct)
 

    return responses
