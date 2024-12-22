from soundscapes.feature_logic import generate_soundscape

def main():
    # Prompt the user for an environment
    environment = input("Enter the environment (e.g., forest, cave, mountain): ").strip().lower()

    # Generate the soundscape
    soundscape = generate_soundscape(environment)

    # Print the generated soundscape
    print(f"Generated soundscape for '{environment}': {soundscape}")

if __name__ == "__main__":
    main()
