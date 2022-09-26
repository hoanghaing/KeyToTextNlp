from transformers import pipeline
generator = pipeline('text-generation', model='./gpt-neo-125M')
x = generator("Korean idol singer", do_sample=True, max_new_tokens=60)
print(x)