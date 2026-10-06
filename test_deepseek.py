from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('DEEPSEEK_API_KEYS', '').split(',')[0]
print(f'Using key: {key[:10]}...')

try:
    client = OpenAI(
        api_key=key,
        base_url='https://api.deepseek.com/v1',
        timeout=30.0,
    )
    resp = client.chat.completions.create(
        model='deepseek-chat',
        messages=[{'role': 'user', 'content': '你好'}],
        max_tokens=50,
    )
    print('Response:', resp.choices[0].message.content)
except Exception as e:
    print('Error:', str(e))
