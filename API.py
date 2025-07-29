# hw7.py

import requests

API_BASE = "http://example.com/api"  # Replace this with the actual API URL

# Start a new game session by calling the API
def start_new_game():
    try:
        response = requests.post(f"{API_BASE}/start")
        response.raise_for_status()
        data = response.json()
        print("New Mastermind game started.")
        return data["game_id"], data["colors"], data["code_length"], data["max_attempts"]
    except Exception as e:
        print("Error starting game:", e)
        exit(1)

# Validate the user's guess
def is_valid_guess(guess, allowed_colors, code_length):
    if len(guess) != code_length:
        print(f"Guess must be exactly {code_length} characters long.")
        return False
    for char in guess:
        if char not in allowed_colors:
            print(f"Invalid color '{char}'. Allowed colors: {', '.join(allowed_colors)}")
            return False
    return True

# Send the guess to the API and receive feedback
def submit_guess(game_id, guess):
    try:
        response = requests.post(f"{API_BASE}/guess", json={
            "game_id": game_id,
            "guess": guess
        })
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error submitting guess:", e)
        return None

# The main game loop
def play_game():
    game_id, allowed_colors, code_length, max_attempts = start_new_game()

    print(f"\nWelcome to Mastermind!")
    print(f"Guess the secret code consisting of {code_length} colors.")
    print("Available colors:", ', '.join(allowed_colors))
    print(f"You have {max_attempts} attempts.\n")

    attempts = 0
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: ").strip().upper()

        if not is_valid_guess(guess, allowed_colors, code_length):
            continue

        result = submit_guess(game_id, guess)
        if result is None:
            continue

        attempts += 1
        print(f"Correct position: {result['correct_position']}, correct color only: {result['correct_color']}")

        if result.get("status") == "won":
            print("\nCongratulations! You cracked the code!")
            break
        elif result.get("status") == "lost":
            print("\nGame over. You've used all your attempts.")
            print(f"The correct code was: {result.get('answer', 'Unknown')}")
            break
        else:
            print(f"Attempts left: {result['attempts_left']}\n")

    print("\nGame session ended.")

# Entry point of the program
if __name__ == "__main__":
    play_game()
