import openai
openai.api_key = "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"

prompt = "Write a poem"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)

generated_text = response.choices[0].text
print(generated_text)
