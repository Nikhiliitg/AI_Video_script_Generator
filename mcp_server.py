from fastmcp import FastMCP
from app import fetch_news, generate_video_transcription

mcp=FastMCP("This is for real time news")

@mcp.tool()
def fetch_news_tool(query: str = "latest news") -> str:
    """
    Fetch the latest news articles.
    """
    return fetch_news(query=query)

@mcp.tool()
def generate_video_transcription_tool(query) -> str:
    """
    Generate a transcription for a given video URL.
    """
    news=fetch_news(query=query)
    return generate_video_transcription(news)

if __name__ == "__main__":
    mcp.run()