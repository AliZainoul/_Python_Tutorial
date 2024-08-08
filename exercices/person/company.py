class Company:
    def __init__(self, name: str, industry: str):
        self.name = name
        self.industry = industry

    def __str__(self) -> str:
        return f"Company: {self.name}, Industry: {self.industry}"
