### BLOG ASSISTANT AGENT

A multi-agent blog assistant that writes an seo optimized article with the possibility to add visuals and formats it for two platforms:
- A Blog article
- A LinkedIn piece

#### Installation
Create and activate a virtual environment using uv or other 

`                                         `
#### Project Setup

`  pip install requirements.txt                              `

#### Running the Agents 
Run the agent in an interactive manner or using the the CLI

```
adk web 
adk run blog_assistant_agent

```
#### Project Structure

blog_assistant_agent/: The main python package for the agent 
    agent.py : Defines the main agents and orchestrates the subagents
    subagents/ : Contains the subagents responsible for specific tasks
        strategist/ : Generates the blog outline and content plan
        author/ : Writes the article
        editor/ : Edits the article based on user feedback
        publisher/ : Generates the LinkedIn and Blog versions
    tools.py : Defines the custom tools used by the different agents

#### Agent Architecture 

#### Workflow 
The Workflow is as follows:
- The user should provide the agent with a topic for a blog article if not the agent will request one. 
- The agent asks the user to chooses how to include visuals in the article 
- The agent then presents the user with an article outline and a content plan
- If the user validates, the agent writes the article and presents it to the user for feedback
- Once the user provides feedback, the agent edit the article to inlude the feedback and present the new article to the user
- If the user agrees, the agent then presents two versions of the article to the user; a linkedin text and a blog article 
- The agent will then ask the user to provide names t save the articles as artefacts