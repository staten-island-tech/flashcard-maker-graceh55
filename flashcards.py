class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    

    class Student(User):
        def __init__(self, name, email, student_id):
            super().__init__(name, email)  # Call the parent class constructor
            self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    

    class Teacher(User):
        def __init__(self, name, email, subject):
            super().__init__(name, email)
            self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"