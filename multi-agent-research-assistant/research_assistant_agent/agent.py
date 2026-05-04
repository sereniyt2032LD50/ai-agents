from google.adk.agents import  SequentialAgent

from .subagents.researcher import research_agent
from .subagents.compiler import compiler_agent


root_agent = SequentialAgent(
    name="ResearchAssistantAgent",
    description="An agent that conducts research on a given subject on the internet",
    sub_agents=[research_agent, compiler_agent],
)