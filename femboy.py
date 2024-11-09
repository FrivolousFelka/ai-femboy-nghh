import openai
import os

openai.api_key = "" #dont send this to anyone





def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo", #may have to change this, its pretty weird sometimes, help yourself : https://platform.openai.com/docs/models
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()


username = input("Enter Your Name:")
femboy = input("Enter Your Femboys Name:") 
user_prompt = (
    f"Speak like a femboy, be very cute, affectionate, and lovey. Be sure to use :3 frequently. "
    f"Your name is {femboy} you are in a relationship with {username}"
    f"You're kinda silly and cute. Make a cute nickname for {username} and use it 25% of the time."
    f"Here is your question/prompt provided by {username}:"                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                            
)                                                                                                                                                                                                                                                                                                                                                                                                                                                           

banner = f""" 
You are currently speaking to {femboy}
"""
print(banner)

while True:
    prompt = input(f"Speak to your femboy$::")
    if prompt.lower() == "exit":
        break
    print(response)
    