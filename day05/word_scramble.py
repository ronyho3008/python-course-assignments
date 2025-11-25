import random

# List of science-related words
WORDS = [
    "proteasome", "ubiquitin", "ribosome", "chromatin", "nucleotide",
"polymerase", "transcription", "translation", "mitochondria",
"phosphorylation", "signal", "cytoskeleton", "kinase",
"chaperone", "replication", "helicase", "exon", "intronic",
"epigenetics", "autophagy"
]

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def play_game():
    print("\n🔬 Welcome to the Science Word Scramble Game! 🔬")
    print("Unscramble the science word. Type 'quit' to exit.\n")

    score = 0

    while True:
        word = random.choice(WORDS)
        scrambled = scramble_word(word)

        print(f"Scrambled word: {scrambled}")
        guess = input("Your guess: ").strip().lower()

        if guess == "quit":
            print(f"\nGame over! Your final score is: {score}")
            break

        if guess == word:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Nope! The correct word was: {word}")
        
        print(f"Current score: {score}\n")


if __name__ == "__main__":
    play_game()