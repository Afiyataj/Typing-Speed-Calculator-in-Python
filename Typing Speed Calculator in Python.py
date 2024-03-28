import random
import time

def calculate_word_per_minute(time_taken, total_words):
    minutes = time_taken / 60
    word_per_minute = total_words / minutes
    return word_per_minute

def generate_text():
    sentence = [
        "Test your typing speed" 
    ]
    return random.choice(sentence)

def main():
    print("Welcome!")
    print("Type the following sentence: ")

    text_to_type = generate_text()
    print(text_to_type)

    input("Press Enter when you are ready")
    
    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    accuracy = sum(1 for x, y in zip(user_input, text_to_type)
                   if x == y) / max(len(text_to_type),len(user_input)) * 100
    word_per_minute = calculate_word_per_minute(time_taken, words_typed)

    print(f"\nTime taken to type the sentence: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Your typing speed is: {word_per_minute:.2f} WPM(Word_Per_Minute)")

if __name__ == "__main__":
    main()
