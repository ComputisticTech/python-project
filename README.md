# Random Joke Generator 🎭

A Python application that generates random jokes using the [JokeAPI](https://jokeapi.dev/) external service.

## Features

- 🎲 Fetch random jokes from multiple categories
- 📚 Support for 6 different joke categories (Any, Misc, Programming, Knock-Knock, Spooky, Christmas)
- 🎯 Handle both single-line and two-part jokes
- ⚠️ Error handling for API failures
- 🧹 Clean, object-oriented design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ComputisticTech/python-project.git
cd python-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Demo
```bash
python joke_generator.py
```

### Use as a Module

```python
from joke_generator import JokeGenerator

# Create an instance
generator = JokeGenerator()

# Get a random joke from any category
generator.get_and_display_joke()

# Get a joke from a specific category
generator.get_and_display_joke("Programming")

# Get raw joke data
joke_data = generator.get_random_joke("Knock-Knock")
print(joke_data)
```

## Available Categories

- **Any** - Random joke from any category
- **Misc** - Miscellaneous jokes
- **Programming** - Programming-related jokes
- **Knock-Knock** - Knock-knock jokes
- **Spooky** - Scary/spooky jokes
- **Christmas** - Christmas-themed jokes

## API Reference

### JokeGenerator Class

#### Methods

- `get_random_joke(category: str = "Any") -> Optional[Dict]`
  - Fetches a random joke from the specified category
  - Returns a dictionary with joke data or None on failure

- `display_joke(joke_data: Dict) -> None`
  - Displays a joke in formatted output
  - Handles both single and two-part joke formats

- `get_and_display_joke(category: str = "Any") -> None`
  - Convenience method to fetch and display a joke in one call

## Example Output

```
🎭 Random Joke Generator
========================================

Category: Programming
😂 Why do Java developers wear glasses?
   Because they don't C#

----------------------------------------
```

## Error Handling

The generator gracefully handles:
- Network connection failures
- API errors
- Invalid category requests
- Malformed API responses

## Requirements

- Python 3.6+
- requests library (see requirements.txt)

## License

MIT License

## API Attribution

Jokes provided by [JokeAPI](https://jokeapi.dev/)
