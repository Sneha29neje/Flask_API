
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("API_KEY")

def get_answer(question):
    headers={
        "Authorization": f"Bearer {apikey}",
        "Accept":"application/json"
    }

    data={
        "messages":[
            {
                "role":"user",
                "content":"Explain the importance of fast language models"
            }
        ],
        "model": "llama-3.3-70b-versatile"
    }

    res=requests.post("https://api.groq.com/openai/v1/chat/completions"
                        ,headers=headers,
                        json=data
                        )

    print("status code",res.status_code)

    print("data",res.json())

    answer=res.json()['choices'][0]['message']['content']


print(get_answer("explain ai"))
print(get_answer("explain flask"))


