
from openai import OpenAI

# Your API key (please use environment variable in production)
API_KEY = "YOUR_OPENAI_API_KEY"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)



while (1):
    inpt = input("User: ")
   
    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {"role": "user", "content": "hii"},
            {"role": "system", "content": "Hi there! How can I help you today?"},
            {"role": "user","content":inpt}
        ],
    )
    print(response.choices[0].message.content)