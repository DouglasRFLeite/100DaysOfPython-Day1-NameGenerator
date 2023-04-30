from include import gpt

def generate_name():
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name  of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print(f'Your band name could be {city_name} {pet_name}')

def generate_name_gpt():
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name  of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")

    prompt = f"""
    Use the city and pet names given bellow to create a
    creative name for a band.

    City name: {city_name}.
    Pet name: {pet_name}.

    Generate a very creative name. Your answer should be just the
    name and no other commentary.
    """

    print(f'Your band name could be {gpt.get_completion(prompt)}')
    

if __name__ == "__main__":
    generate_name_gpt()