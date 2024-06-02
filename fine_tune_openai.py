import openai

openai.api_key = 'sk-proj-Bn19bfS5o0gVqDKGcDaaT3BlbkFJMfT9vPdZtyWlzIk5MmMg'

# Upload your JSONL file
response = openai.File.create(
  file=open("FineTuneData"),
  purpose='fine-tune'
)

# Start fine-tuning
fine_tune_response = openai.FineTune.create(
  training_file=response['id'],
  model="gpt-4"
)

# Monitor the fine-tuning process
fine_tune_id = fine_tune_response['id']
status = openai.FineTune.retrieve(id=fine_tune_id)
print(status)

# Use the fine-tuned model (after completion)
response = openai.Completion.create(
  model="gpt-4:ft-your-fine-tuned-model",
  prompt="Please assess the following initiation(s): 'Hey, did you see the elephant in the backyard?' The suggestion was 'elephant'.",
  max_tokens=100
)

print(response.choices[0].text.strip())
