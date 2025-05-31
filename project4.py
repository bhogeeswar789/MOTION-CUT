import random

def make_nicknames(first, last, style):
    names = []
    names.append(first[:3] + last[-3:])
    names.append(last[:3] + first[-3:])
    names.append(first + last)
    names.append(last + first)
    names.append(first[:2] + last[:2] + str(random.randint(10, 99)))

    if style == "fun":
        names.append(first + "_fun")
        names.append(last + "_cool")
    elif style == "short":
        names.append((first + last)[:5])
    elif style == "formal":
        names.append(first.capitalize() + "." + last.capitalize())

    return names

def main():
    first = input("First name: ")
    last = input("Last name: ")
    style = input("Style (fun/short/formal): ").lower()

    result = make_nicknames(first, last, style)
    print("\nNicknames:")
    for name in result:
        print("-", name)

    save = input("Save to file? (yes/no): ").lower()
    if save == "yes":
        with open("nicknames.txt", "w") as f:
            for name in result:
                f.write(name + "\n")
        print("Saved to nicknames.txt")

if __name__ == "__main__":
    main()