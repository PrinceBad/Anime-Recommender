# Anime Recommender: AI-Powered Anime Suggestions (Python CLI)

![Anime Recommender Showcase](https://placehold.co/1200x600/1a202c/9f7aea?text=Python%20Anime%20Recommender)

**Find your next binge-worthy anime with the power of AI! Anime Recommender is a simple yet powerful command-line application that provides personalized anime recommendations based on your favorite shows.**

## 👋 Introduction

Tired of endlessly scrolling, searching for your next favorite anime? You've just finished an incredible series, and now you're left with that all-too-familiar question: "What do I watch next?"

**Let our AI be your guide.** This application uses the Google Gemini API to generate intelligent and relevant anime recommendations right in your terminal.

## 🌟 Features

* **AI-Powered Suggestions:** Leverages the Google Gemini API to provide intelligent and relevant anime recommendations.
* **Personalized Content:** Enter any anime you love and get a curated list of similar shows.
* **Detailed Information:** Each suggestion includes a concise synopsis and the primary genre.
* **Simple CLI Interface:** A clean, colorful, and easy-to-use command-line interface.
* **Structured Data:** Fetches responses from the Gemini API in a structured JSON format for reliability and consistency.

## 🛠️ Tech Stack

* **Language:** [Python 3](https://www.python.org/)
* **API Communication:** [Requests](https://pypi.org/project/requests/)
* **AI & Recommendations:** [Google Gemini API](https://ai.google.dev/)

## ⚡ Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.6+ installed.
* A Google Gemini API key. You can get one from [Google AI Studio](https://ai.google.dev/).

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/anime-recommender-python.git](https://github.com/your-username/anime-recommender-python.git)
    cd anime-recommender-python
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```sh
    # Create a virtual environment
    python -m venv venv

    # Activate it (on macOS/Linux)
    source venv/bin/activate
    # Or on Windows
    # venv\Scripts\activate

    # Install the required packages
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    This application requires your Google Gemini API key to be set as an environment variable.

    **On macOS/Linux:**
    ```sh
    export GEMINI_API_KEY='YOUR_API_KEY_HERE'
    ```
    *To make this permanent, add the line to your `~/.bashrc`, `~/.zshrc`, or other shell configuration file.*

    **On Windows (Command Prompt):**
    ```sh
    setx GEMINI_API_KEY "YOUR_API_KEY_HERE"
    ```
    *You may need to restart your terminal for this to take effect.*

### Running the Application

Once the setup is complete, simply run the script:
```sh
Recommender.py
