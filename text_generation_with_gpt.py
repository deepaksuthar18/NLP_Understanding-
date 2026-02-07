from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
generated_text = generator("Once upon a time, in a land far, far away, there lived a", max_length=50, num_return_sequences=1)
print(generated_text)