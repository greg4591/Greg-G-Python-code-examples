oranges = {
    "Navel": "A sweet, seedless orange with a thick skin.",
    "Valencia": "A juicy orange often used for juice.",
    "Mandarin": "A small, easy-to-peel orange with a sweet flavor.",
    "Blood": "An orange with deep red flesh and a unique flavor.",
    "Cara Cara": "A type of navel orange with pinkish-red flesh.",
    "Tangerine": "A small citrus fruit with a loose skin and sweet flavor.",
    "Clementine": "A seedless, easy-to-peel orange with a sweet taste.",
    "Satsuma": "A seedless orange with a loose skin and sweet flavor.",
}

def ask_orange_fruit():
    fruit = input("Enter the name of an orange fruit type: ")
    description = oranges.get(fruit)
    if description:
        print(f"{fruit}: {description}")
    else:
        print("Sorry, that orange type is not in the list.")

ask_orange_fruit()
