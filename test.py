from openai import OpenAI

# ایجاد یک نمونه از کلاینت با کلید API خود
client = OpenAI(base_url='https://api.gapgpt.app/v1', api_key='sk-sEbZLuw7Gzr91CLF8XfylaTogqQsn3wUvcvFSRDYQ62xCH52')

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "سلام! نظرت در مورد ایران چیه؟"}
    ]
)

print(response.choices[0].message.content)
