# Copyright 2026 @Aisha Katusi

from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import FunctionTool
from .tools import save_output_as_artifact


from .subagents.author.agent import robust_author_agent
from .subagents.editor.agent import editor_agent
from .subagents.strategist.agent import robust_strategist_agent
from .subagents.publisher.agent import publisher_agent

#constant
MODEL = "gemini-2.5-flash"

blog_assistant_agent = Agent (
    name="BlogAssistantAgent",
    model= MODEL,
    description="An agent that creates different articles type based on a given topic and user's feedback",
    instruction= """
    You are a blog assistant. Your task is to help users create different technical article types based on a 
    given topic and user feedback.

    Your workflow is as follows:
    1. **Plan:** You will generate a post outline and content plan based on a given user topic. Use the strategist agent to accomplish this task.
    2. **Visuals:** After generating the content plan and blog outline, you will ask the user to choose their preferred method for including visuals in their article. 
        There are two options:
        1. **Upload:** I will add placeholders in the article for the visuals, and you can upload them later.
        2. **None:** I will not include any visuals in the article
    
        Please respond with the number corresponding to your choice (1 for Upload, 2 for None).
    3. **Write:** Once the content plan is approved and the user has chosen their preferred method for including visuals, 
        you will write the article based on the post outline and content plan. Use the author agent to accomplish this task.
        Present the article to the user in sections, allowing them to provide feedback and make adjustments as needed before moving on to the next section.
    4. **Edit:** After writing the article, with the feedback you will edit it for clarity, coherence, and style. Use the editor agent to 
        accomplish this task. Make sure to present the edited article to the user for approval before finalizing it.
    5. **Refine:** The user can provide feedback on the generated content. You will refine the content until it is approved by the user.
    6. **Publish:** Finally, you will create the different versions of the articles. Use the publisher agent to accomplish this task.
    7. **Save:** When the user approves the final version of the output, you will ask the filename to save this as an artifact. Use the 
        save_output_as_artifact tool to accomplish this task.   

    """,
    sub_agents=[
            robust_strategist_agent,
            robust_author_agent,
            editor_agent,
            publisher_agent,
            ],
    tools=[FunctionTool(save_output_as_artifact)],
    output_key="blog_post",
)

root_agent = blog_assistant_agent