import os
import json
import requests
from textwrap import dedent

# ANSI escape codes for colors
class Colors:
    PURPLE = '\033[95m'
    PINK = '\033[94m' # More like a blue, but let's call it pink for theme
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_anime_suggestions(favorite_anime: str, api_key: str) -> list | None:
    """
    Fetches anime suggestions from the Gemini API.

    Args:
        favorite_anime: The name of the user's favorite anime.
        api_key: The Google Gemini API key.

    Returns:
        A list of suggested anime dictionaries or None if an error occurs.
    """
    print(f"\n{Colors.CYAN}Searching for anime similar to '{favorite_anime}'...{Colors.ENDC}")

    # The prompt for the AI model
    prompt = f"Based on the anime \"{favorite_anime}\", suggest 5 similar anime. For each suggestion, provide a one-sentence synopsis and its primary genre."

    # The expected JSON schema for the response
    schema = {
        "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "title": { "type": "STRING" },
                "synopsis": { "type": "STRING" },
                "genre": { "type": "STRING" },
            },
            "required": ["title", "synopsis", "genre"]
        }
    }
    
    # Prepare payload for the Gemini API
    payload = {
        "contents": [{
            "role": "user",
            "parts": [{ "text": prompt }]
        }],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": schema,
        },
    }
    
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    try:
        response = requests.post(api_url, json=payload, headers={'Content-Type': 'application/json'})
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        result = response.json()

        # Process the API response
        if (result.get("candidates") and 
            result["candidates"][0].get("content") and 
            result["candidates"][0]["content"].get("parts")):
            
            suggestions_json_str = result["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(suggestions_json_str)
        else:
            print(f"{Colors.RED}Error: Received an unexpected response format from the API.{Colors.ENDC}")
            print(f"Response: {result}")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"{Colors.RED}HTTP error occurred: {http_err}{Colors.ENDC}")
        print(f"{Colors.YELLOW}Response Body: {response.text}{Colors.ENDC}")
    except requests.exceptions.RequestException as req_err:
        print(f"{Colors.RED}A network error occurred: {req_err}{Colors.ENDC}")
    except json.JSONDecodeError:
        print(f"{Colors.RED}Error: Failed to parse the response from the API.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.RED}An unexpected error occurred: {e}{Colors.ENDC}")

    return None

def display_suggestions(suggestions: list):
    """
    Displays the anime suggestions in a formatted way.
    
    Args:
        suggestions: A list of anime dictionaries to display.
    """
    print(f"\n{Colors.BOLD}{Colors.PURPLE}--- Here are your recommendations ---{Colors.ENDC}\n")
    for i, anime in enumerate(suggestions, 1):
        print(f"  {Colors.BOLD}{Colors.PINK}{i}. {anime.get('title', 'N/A')}{Colors.ENDC}")
        print(f"     {Colors.GREEN}Genre:{Colors.ENDC} {anime.get('genre', 'N/A')}")
        print(f"     {Colors.YELLOW}Synopsis:{Colors.ENDC} {anime.get('synopsis', 'N/A')}\n")
    print(f"{Colors.BOLD}{Colors.PURPLE}------------------------------------{Colors.ENDC}")


def main():
    """
    Main function to run the anime recommender CLI application.
    """
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{Colors.RED}{Colors.BOLD}Error: GEMINI_API_KEY environment variable not found.{Colors.ENDC}")
        print(f"{Colors.YELLOW}Please set your Google Gemini API key as an environment variable.{Colors.ENDC}")
        print("Example: export GEMINI_API_KEY='your_api_key_here'")
        return

    # App header
    header = dedent(f"""
    {Colors.BOLD}{Colors.PURPLE}
    ======================================
    🎬 Welcome to Anime Recommender! 🎬
    ======================================
    {Colors.ENDC}
    """)
    print(header)
    print(f"{Colors.CYAN}Find your next favorite show with the power of AI.{Colors.ENDC}")
    print(f"Type 'quit' or 'exit' to close the application.\n")

    while True:
        favorite_anime = input(f"{Colors.BOLD}Enter your favorite anime: {Colors.ENDC}").strip()
        
        if favorite_anime.lower() in ['quit', 'exit']:
            print(f"\n{Colors.PINK}Happy watching! Goodbye!{Colors.ENDC}")
            break
            
        if not favorite_anime:
            print(f"{Colors.RED}Please enter an anime title.{Colors.ENDC}")
            continue

        suggestions = get_anime_suggestions(favorite_anime, api_key)

        if suggestions:
            display_suggestions(suggestions)
        else:
            print(f"\n{Colors.YELLOW}Could not retrieve suggestions. Please try another anime or check the error messages.{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
