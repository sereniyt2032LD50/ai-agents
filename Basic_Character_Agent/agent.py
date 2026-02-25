from google.adk.agents import Agent
from google.genai import types 

#Defining the root agent
root_agent = Agent(
    name = "CharacterAgent", # Name of our AI Agent 
    model = "gemini-2.0-flash", # Underlying Model we will be using
    description = "Greeting Agent", # A brief description of the agent 
    instruction = 
            """You are a lazy but still helpful assistant that greets the user. 
               Talk to me in a shakespearean manner.
            """, # Detailed things the Agent has to do

    generate_content_config=types.GenerateContentConfig(
        temperature=0.2, #More deterministic output, closer to 0 more deterministic
        max_output_tokens=250
    )
)
