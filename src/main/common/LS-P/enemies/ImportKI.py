import openai
openai.api_key = "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"

prompt = "What time is now in Berlin"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)

generated_text = response.choices[0].text
print(generated_text)
