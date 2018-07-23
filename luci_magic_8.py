#luci_magic_8
import random
print("~~Welcome to Magic 8 Ball~~")

question = input("Ask the Magic 8 Ball a question: ")
ans_list = ["For sure!", "Unclear", "Unlikely", "More than likely.", "Maybe", "In your dreams.", "When pigs fly.", "Never gonna happen.", "Piss off, jerkwad.", "Can you repeat that?", "Be careful what you wish for."]

while True:
    print(random.choice(ans_list))
    break

another = input("Would you like to ask something else? ")
while another.lower() != "no":
    input("Ask the Magic 8 Ball a question: ")
    while True:
        print(random.choice(ans_list))
        another = input("Would you like to ask something else? ")
        break
