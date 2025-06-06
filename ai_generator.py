import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_blog_post(keyword, seo_data):
    prompt = f"""
    Create a 500-word blog post in Markdown format about '{keyword}'.
    SEO Data: Search Volume: {seo_data['search_volume']}, Keyword Difficulty: {seo_data['keyword_difficulty']}, Avg CPC: ${seo_data['avg_cpc']}.
    Structure:
    - A catchy title
    - An engaging intro (100 words)
    - 3-4 sections with subheadings (e.g., benefits, features, recommendations)
    - Include 2 placeholder affiliate links: {{AFF_LINK_1}}, {{AFF_LINK_2}}
    - End with a conclusion and call-to-action
    Optimize for readability and SEO. Use the keyword '{keyword}' naturally 3-5 times.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )

    content = response.text

    # Replace affiliate link placeholders
    content = content.replace("{{AFF_LINK_1}}", "https://example.com/aff1")
    content = content.replace("{{AFF_LINK_2}}", "https://example.com/aff2")
    
    return content