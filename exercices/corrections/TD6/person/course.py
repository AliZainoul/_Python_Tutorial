class Course:
    def __init__(self, courseName: str, credits: int):
        self.courseName = courseName
        self.credits = credits

    def __str__(self) -> str:
        return f"Course: {self.courseName}, Credits: {self.credits}"
