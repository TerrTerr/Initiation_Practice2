import openai

openai.api_key = 'your-api-key'

# Upload your JSONL file
response = openai.File.create(
  file=open("fine_tuning_data.jsonl"),
  purpose='fine-tune'
)

# Start fine-tuning
fine_tune_response = openai.FineTune.create(
  training_file=response['id'],
  model="davinci"
)

# Monitor the fine-tuning process
fine_tune_id = fine_tune_response['id']
status = openai.FineTune.retrieve(id=fine_tune_id)
print(status)

# Use the fine-tuned model (after completion)
response = openai.Completion.create(
  model="davinci:ft-your-fine-tuned-model",
  prompt="Please assess the following initiation(s): 'Hey, did you see the elephant in the backyard?' The suggestion was 'elephant'.",
  max_tokens=100
)

print(response.choices[0].text.strip())
