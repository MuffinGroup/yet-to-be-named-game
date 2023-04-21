import openai
openai.api_key = "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"

prompt = "Whats the Time"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)

generated_text = response.choices[0].text
print(generated_text)
