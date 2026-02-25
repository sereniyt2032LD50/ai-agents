from google.adk.agents import Agent
from google.genai import types 
from google.genai.models.lite_llm import Litellm
from google.adk.tools import FunctionTool
import litellm
from faq import Faq_text

AGENT_MODEL = Litellm(model="openai/gpt-4o-mini") #To use a model other tha gemini


#Initializing the safety settings for the agent to stay within topic 
safety_settings = types.SafetySetting (
    category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
)

def lookup_faq(question: str) -> str:
    """ You are a tool that will be used by the customer support agent to answer questions related to the faq """
    faq_text = "\n".join(f" - {k} : {v} " for k, v in {Faq_text.items()})

    prompt = (
        f"You are helpful assistant. This is an faq database: \n\n{faq_text}\n\n"
        f"User's question: \"{question}\". "
        f"Reply with the best match from the faq. If it is not available, say you don't know."
    )

    response = litellm.completion(
        model="gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0][message][content].strip()


faq_tool = FunctionTool(func=lookup_faq)

root_agent = Agent(
    name="CustomerSupportAgent",
    model = "gemini-2.0-flash",
    description = "An agent that answers from a set of faq's",
    Instructions =
    """
        You are a customer support agent that answers the user queries from an available faq database. 
        If the user ask questions outside of the faq database, you implement the guardrail strategy
    """,

    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250,
        safety_settings=safety_settings
    ),
    tools = [faq_tool]
)