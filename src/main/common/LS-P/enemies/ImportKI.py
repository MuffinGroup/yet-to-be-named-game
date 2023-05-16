try:
    import openai
except ImportError:
    import subprocess as sp
    # FIXME: create requirements.txt with openai dependency to make the following code redundant
    try:
        sp.run(['python', '-m', 'pip', 'install', 'openai'])
    finally:
        import openai
    except Exception:
        import sys
        sys.exit(0)

openai.api_key = "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"

prompt = "Write a poem"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)

generated_text = response.choices[0].text
print(generated_text)
