from google.adk.agents import Agent
from google.genai import types 
from google.genai.models import Litellm

AGENT_MODEL = Litellm(model="openai/gpt-4o-mini")


safety_settings = types.SafetySetting (
    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
)

def lookup_faq():
    """ You are a tool that will be used by the customer support agent to answer questions related to the faq """
    faq_text = "\n".join(f" {k} : {v} for k, v in ")

    return 

root_agent = Agent (
    name="CustomerSupportAgent",
    model = "gemini-2.0-flash",
    description = 
    """
        You are a customer support agent that answers the user queries from an available faq database. 
        If the user ask questions outside of the faq database, you implement the guardrail strategy
    """,

    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250
    )
)