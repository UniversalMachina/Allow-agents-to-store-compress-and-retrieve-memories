import openai
openai.api_key ="api-key"

def generate_text(prompt):
    import time

    max_attempts = 5

    for attempt in range(max_attempts):
        try:
            # Your code block here
            # Replace the following line with the code you want to execute
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                ]
            )
            message = completion["choices"][0]["message"]["content"]
            return message
            # If the code runs without any errors, break out of the loop

        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
            time.sleep(1)  # Optional: add a time delay between attempts
    else:
        print(f"Failed after {max_attempts} attempts.")




