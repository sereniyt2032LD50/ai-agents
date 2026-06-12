from google.adk.agents import Agent

#constant
MODEL = "gemini-2.5-flash"

editor_agent = Agent (
    name="EditorAgent",
    model = MODEL,
    description="Edits an article based on user feedback",
    instruction= """
    Role: You are an editor agent. 
    You will be given a blog post and user feedback. 
    Your task is to edit and format the blog article based on the user's feedback while optimizing metadata, tags, and links.
    
    The final output should be a well-formatted article ready for publication to various platforms
    """,
    output_key="published_blog_post",
)