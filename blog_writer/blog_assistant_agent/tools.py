from fileinput import filename

from google.genai import types
from google.adk.tools.tool_context import ToolContext

def save_blog_post(blog_post: str, filename: str ):
    """ Saves the blog post to a file """
    with open(filename, "w") as f:
        f.write(blog_post)
    return f"Blog post saved to {filename}"


async def save_output_as_artifact(blog_post: str, tool_context: ToolContext, filename: str):
    """ Saves the blog post as an artifact """
    
    #Encode the string content into bytes
    data_bytes = blog_post.encode('utf-8')
    
    #create the artifact with the encoded data
    artifact_part = types.Part(
        inline_data = types.Blob(mime_type="text/plain", data=data_bytes),
    )
    
    await tool_context.save_artifact(filename, artifact_part)

    return f"Successfully processed and save file {filename} as a blog post artifact."


