class Reverse:
    def __init__(self):
        self.s = ""

    def get_input(self):
        self.s = input("Enter sentence: ")

    def reverse_words(self):
        words = self.s.split()
        words = words[::-1]
        return " ".join(words)


r = Reverse()
r.get_input()
print(r.reverse_words())