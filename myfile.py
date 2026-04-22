# A sample Python file with some linting errors for ruff to find
class Octocat:
    def __init__(self, name, breeds):
        self.name = name
        self.breeds = breeds

    def display(self):
        breed = "-".join(self.breeds)
        print(f"I am of {breed} breed, and my name is {self.name}.")

m = Octocat("Mona", ["cat", "octopus"])
m.display()
