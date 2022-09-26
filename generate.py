from transformers import pipeline
import re
generator = pipeline('text-generation', model='./gpt-neo-125M')
# x = generator("Korean idol singer", do_sample=True, max_new_tokens=60)
x = generator("Tommy shaw was", do_sample=True, max_new_tokens=60)
z = re.sub(r"[\n\t]*", "", x[0]['generated_text'])
# print(x[0]['generated_text'])
print(z)

# Tommy shaw was with me that day as I got on my stomach. I wanted to make a stop before the tour bus began to pull up to the front steps,
# which was the last stop I had before the train left. The car doors opened. My eyes snapped up, and a familiar name came to mind