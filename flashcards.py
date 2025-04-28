import json

class Flashcards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    
    def display_info(self):
        return f"{self.question} {self.answer}"
    
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

""" my_flashcards = Flashcards("apple", "red")
print(my_flashcards.display_info()) """

flashcards_list = [
    Flashcards("apple", "red"),
    Flashcards("banana", "yellow"),
    Flashcards("tangerine", "orange")
]


# Convert objects to dictionaries
flashcards_data = [flashcard.to_dict() for flashcard in flashcards_list]

# Save to a JSON file
with open("flashcard.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)

streak = 0
total_flashcards = 3

while streak < total_flashcards:
    for flashcard in flashcards_list:
        user_input = input(f"What color is a {flashcard.question}? ")
        
        if user_input == flashcard.answer:
            streak += 1
            print("Streak", streak, "🔥")
        
        else:
            streak = 0
            print("Streak lost :(")
            break

    if streak == total_flashcards:
        print("Congratulations!!")
        break
        

          