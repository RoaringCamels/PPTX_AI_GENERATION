import openai

contentText = "Create a 5 slide presentation about solar energy."

response = openai.ChatCompletion.create(
    model="gpt-4",
    message=[
        {"role":"user", "content":contentText}
    ]
)

slideText = response['choices'][0]['message']['content']