# AI News & Video Script Generator

A Streamlit-based application that fetches real-time news on any topic using EURI AI and generates engaging video scripts for YouTube Shorts or Instagram Reels. Ideal for content creators, journalists, or AI enthusiasts looking for automated news insights and script generation.

---

## 🔹 Features

- Fetch the latest news for any keyword or topic.
- Generate a short, engaging video script based on the news.
- Downloadable scripts as .txt files for easy reuse.
- Built with Streamlit for quick and interactive usage.
- Powered by EURI AI’s Gemini and GPT models.

---

## 🛠️ Tech Stack & Libraries

- Frontend / App: Streamlit
- AI / NLP: EURI AI (gemini-2.0-flash-001 for news, gpt-4.1-mini for scripts)
- Data Handling: pandas, numpy
- Visualization (optional): matplotlib, seaborn, plotly
- Image & ML Extras: scikit-image, scikit-learn, scikit-learn-extra
- Environment Management: python-dotenv
- MCP Integration: fastmcp

---

## ⚡ Installation

# Clone the repository
git clone <your-repo-url>
cd <repo-folder>

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
# Create a .env file in the project root:
EURI_API_KEY=your_api_key_here

---

## 🚀 Usage

## Run Streamlit App
streamlit run app.py

 Instructions:
1. Enter a topic or keyword in the input box.
2. View the latest news fetched by the AI.
3. Optionally, select “Yes” to generate a video script.
. Download the script via the download button.

# Run MCP Tools (Optional)
python mcp_tools.py

# Tools exposed:
# fetch_news_tool – fetch the latest news.
# generate_video_transcription_tool – generate a video script from news.

---

## 📄 Example

# Input: Artificial Intelligence

# News Output:
# “Recent breakthroughs in AI include … [summary of latest news]”

# Video Script Output:
# “Hook: Did you know AI is transforming industries faster than ever? Today’s news: … CTA: Don’t forget to like and subscribe for more updates!”

---

## ⚙️ Project Structure

├── app.py                     # Streamlit application
├── mcp_tools.py               # FastMCP integration
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables (API key)

---

## 💡 Notes & Tips

# Ensure your EURI API key is valid and has access to the models.
# Adjust max_tokens or temperature in app.py for shorter/longer outputs or more creative responses.
# You can integrate additional features like news history, caching, or multiple languages.

---

## ❤️ Made With

Streamlit
EURI AI
Python
