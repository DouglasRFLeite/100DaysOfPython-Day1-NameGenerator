import openai

def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = "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"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]