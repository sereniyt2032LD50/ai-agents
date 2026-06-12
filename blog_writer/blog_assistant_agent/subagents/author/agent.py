""" 
An agent that handles research, topic discovery, SEO, and content planning.
"""

from google.adk.agents import Agent, LoopAgent 
from google.adk.tools import google_search

#constants
MODEL = "gemini-2.5-flash"

author_agent = Agent(
    name="AuthorAgent",
    model= MODEL,
    description="An agent that writes a concise blog article.",
    instruction="""
    You are an expert technical blog writer that writes articles with a clear and engaging tone.

    The user will provide you with a topic for a blog article. Your task is to create a well-researched 
    and SEO-optimized blog article on that topic based on the provided post outline and content plan.
    The article should be concise, engaging, and informative, providing value to the reader while adhering to SEO best practices.
    - Deep dive into the topic, ensuring that the content is accurate and comprehensive
    - Use google search to find relevant information and sources on the topic.
    - Write in a clear and engaging tone, making the content accessible to a wide audience.
    - Ensure that the article is SEO-optimized, incorporating relevant keywords and following best practices for on-page SEO.
    
    The final output should be a well-structured blog article in markdown format that effectively communicates the topic to the audience

    """,
    tools=[google_search],
    output_key="blog_post"
)

robust_author_agent = LoopAgent(
    name="RobustAuthorAgent",
    description="A robust author agent that retries if it fails.",
    sub_agents=[author_agent],
    max_iterations=3,
)
