import openai

def ask_question(processed_text, question, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo" depending on availability
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"The following is a document:\n\n{processed_text}\n\nQuestion: {question}\nAnswer:"}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()
