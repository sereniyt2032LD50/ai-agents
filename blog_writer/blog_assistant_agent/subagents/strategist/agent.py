""" 
An agent that handles research and content planning.
"""
from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

#constant
MODEL = "gemini-2.5-flash"
strategist_agent = Agent(
    name="StrategistAgent",
    model= MODEL,
    description="An agent that handles a post outline and content planning.",
    instruction="""
    You are a blog strategist agent. Your job is to create a blog post outline and content plan based on a specific topic.
    
    The blog post outline and content plan should contain the structured attributes that contain the same core idea 
    on a specific topic provided by the user that could be adapted into multiple formats such as long from blog posts and
    more conversational linkedIN posts. 
    This agent acts as the “thinking and planning” layer of the blogging system, ensuring the content is relevant, 
    strategic, and aligned with the overall goals of the platform or organization.

    Your final output should be a structured blog outline and content plan in Markdown format """,
    tools=[google_search],
    output_key="blogOutline_contentPlan"
    "",
)

robust_strategist_agent = LoopAgent(
    name="RobustStrategistAgent",
    description="A robust blog strategist agent that retries if it fails.",
    sub_agents=[strategist_agent],
    max_iterations=3,
    )

