import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """A random joke generator using the JokeAPI external service."""
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    def __init__(self):
        """Initialize the JokeGenerator."""
        self.session = requests.Session()
    
    def get_random_joke(self, category: str = "Any") -> Optional[Dict]:
        """
        Fetch a random joke from the JokeAPI.
        
        Args:
            category: The joke category (Any, Misc, Programming, Knock-Knock, 
                     Spooky, Christmas). Default is 'Any'.
        
        Returns:
            A dictionary containing the joke data, or None if the request fails.
        """
        try:
            url = f"{self.BASE_URL}/{category}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("error"):
                print(f"Error: {data.get('message', 'Unknown error')}")
                return None
            
            return data
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def display_joke(self, joke_data: Dict) -> None:
        """
        Display a joke in a formatted way.
        
        Args:
            joke_data: The joke data dictionary from the API.
        """
        if not joke_data:
            print("No joke data to display.")
            return
        
        if joke_data.get("type") == "single":
            print(f"\n😂 {joke_data.get('joke', 'Joke not found')}\n")
        
        elif joke_data.get("type") == "twopart":
            setup = joke_data.get('setup', 'Setup not found')
            delivery = joke_data.get('delivery', 'Delivery not found')
            print(f"\n😂 {setup}")
            print(f"   {delivery}\n")
        
        else:
            print("\n📝 Unknown joke format.\n")
    
    def get_and_display_joke(self, category: str = "Any") -> None:
        """
        Convenience method to fetch and display a joke in one call.
        
        Args:
            category: The joke category.
        """
        joke_data = self.get_random_joke(category)
        self.display_joke(joke_data)


def main():
    """Main function to demonstrate the joke generator."""
    print("🎭 Random Joke Generator")
    print("=" * 40)
    
    generator = JokeGenerator()
    
    # Available categories
    categories = ["Any", "Misc", "Programming", "Knock-Knock", "Spooky", "Christmas"]
    
    print("\nAvailable categories:")
    for i, category in enumerate(categories, 1):
        print(f"  {i}. {category}")
    
    print("\nGenerating random jokes...\n")
    
    # Get jokes from different categories
    for category in ["Programming", "Misc", "Knock-Knock"]:
        print(f"Category: {category}")
        generator.get_and_display_joke(category)
        print("-" * 40)


if __name__ == "__main__":
    main()
