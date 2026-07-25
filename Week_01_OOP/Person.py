class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name :{self.name} Age:{self.age}")
p1=Human("Aman", 21)
p2=Human("Khurshed",22)
p1.display();
p2.display();