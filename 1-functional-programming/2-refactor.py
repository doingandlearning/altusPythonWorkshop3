from datetime import datetime

# Why is this not functional?
# Detached time from the behaviour of the clas
class Greeting:
    def __init__(self, greeting_intro):
        self.greeting_intro = greeting_intro

    def greet(self, name):
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names):
        results = []
        for name in names:
            results.append(self.greet(name))
        return results


def main():
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"

    name = input("Enter your name: ")
    greeting = Greeting(greeting_intro)
    print(greeting.greet(name))
    [print(name) for name in greeting.greet_list(["Sourav", "Santosh", "Megha"])]


if __name__ == "__main__": # __something__ - dunder
    main()