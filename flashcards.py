import json

class Flashcards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    
    def display_info(self):
        return f"{self.question} {self.answer}"
    
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

my_flashcards = Flashcards("apple", "red")
print(Flashcards.display_info())

flashcards_list = [
    Flashcards("apple", "red"),
    Flashcards("banana", "yellow"),
    Flashcards("tangerine", "orange")
]

# Convert objects to dictionaries
flashcards_data = [Flashcards.to_dict() for flashcard in flashcards_list]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)