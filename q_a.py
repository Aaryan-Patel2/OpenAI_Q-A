from openaikey import key #or use the env and os
import openai
from colorama import Fore

openai.api_key = key #grab the key

def inquiry(text, direction):

    #create a function that can answer questions (using DaVinci 003)

    print("> Summarizing.....")

    #process the prompt for the API to read
    prompt = (
        f"{direction}"
        f"{text.strip()}"
    )
    
    #tweak how you want the model to run
    return openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 1,
        max_tokens = 100,
        frequency_penalty = 0,
        presence_penalty = 0
    )

#Test inquiry
x = inquiry("MAIN QUESTION", "ADDITIONAL INFO")
print(x.choices[0].text)