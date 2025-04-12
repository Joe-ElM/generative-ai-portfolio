---
sdk: gradio
app_file: main.py
---

# HomeMatch: AI-Powered Real Estate Personalization App

**HomeMatch** is an AI-powered real estate assistant that transforms standard property listings into personalized narratives based on individual buyer preferences.

Using large language models (LLMs) and vector search, HomeMatch helps users discover properties that match their lifestyle, budget, and dreams — and presents listings in a way that feels like they were written just for them.

---

## Features

- Personalized property descriptions
- Semantic search using vector databases (ChromaDB)
- Natural language user input (e.g., "I want a quiet neighborhood with a garden and easy public transport")
- Dynamic listing generation (50 custom listings auto-generated at startup)
- Interactive web app built with Gradio
- Modular Python architecture (clean for scale and future features)
- Ready for deployment on Hugging Face Spaces

---

## Tech Stack

- Python 3.10
- LangChain
- OpenAI API (LLM)
- ChromaDB for vector search
- Gradio for user-friendly web interface
- Pandas for data handling
- FastAPI for future extensibility

---

## How it works

1. Generate Listings:  
   At startup, HomeMatch generates 50 diverse real estate listings using an LLM and stores them in a vector database.

2. Collect User Preferences:  
   Users describe their ideal home and lifestyle in natural language.

3. Semantic Search:  
   The app performs a semantic search in the vector database to find the top 3 matching listings.

4. Personalized Rewrite:  
   For each match, HomeMatch uses the LLM to personalize the listing description based on the user's preferences.

5. Interactive Results:  
   Users receive rich, personalized property descriptions via the Gradio web interface.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/HomeMatch.git
cd HomeMatch
pip install -r requirements.txt
