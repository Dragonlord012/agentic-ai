import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search


load_dotenv()


def print_post_and_sources(response):
    """
    Prints the LinkedIn post followed automatically by the 
    real source links used to generate that response.
    """
   
    print("\n===  LINKEDIN DRAFT ===\n")
    print(response.text)
    
    try:
        candidate = response.candidates[0]
        metadata = candidate.grounding_metadata
        
        if metadata and metadata.grounding_chunks:
            print("\n===  RESOURCES USED (Auto-Generated) ===")
            
         
            unique_links = set()
            
            for chunk in metadata.grounding_chunks:
                if chunk.web:
                    title = chunk.web.title
                    uri = chunk.web.uri
                    
                    if uri not in unique_links:
                        print(f"{title}")
                        print(f"  {uri}")
                        unique_links.add(uri)
        else:
            print("\n(No web search was required for this post.)")
            
    except AttributeError:
        print("\n(Source metadata not available.)")

root_agent = Agent(
    name="linkedin_creator",
    model="gemini-2.0-flash", 
    
    tools=[google_search], 
    instruction="""
    You are a viral LinkedIn Content Creator.
    
    Your Goal: Write high-engagement posts based on real-time data.
    
    Step 1: RESEARCH. Always use the 'google_search' tool to find the latest data on the user's topic.
    Step 2: WRITE. Create a post using this structure:
       - **The Hook:** A punchy, 1-line opener to grab attention.
       - **The Insight:** Use bullet points to list the data/trends found.
       - **The Takeaway:** A professional conclusion.
       - **The Ask:** A question to drive comments.
       - **Hashtags:** 3-5 relevant tags.
    
    CRITICAL CONSTRAINT: 
    Write ONLY the post content. 
    DO NOT manually type a list of sources at the bottom. 
    The system will attach the sources automatically.
    """
)

