def read_superheroes(filename):
    superheroes = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip the line of leading/trailing whitespace and split by comma
            name, year = line.strip().split(', ')
            # Append the tuple (name, int(year)) to the superheroes list
            superheroes.append((name, int(year)))
    return superheroes

def sort_superheroes(superheroes):
    # Sort the list of tuples by the second element (year)
    return sorted(superheroes, key=lambda hero: hero[1])

def print_superheroes(superheroes):
    for name, year in superheroes:
        print(f"Superhero: {name}")
        print(f"Year of First Appearance: {year}")
        print()  # Print a blank line for readability

if __name__ == "__main__":
    # Read, sort, and print superheroes
    superheroes = read_superheroes('superheroes.txt')
    sorted_superheroes = sort_superheroes(superheroes)
    print_superheroes(sorted_superheroes)
