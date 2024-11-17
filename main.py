import os


def read_banner(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


def parse_banner(file_content):
    lower_bound = 32
    upper_bound = 126
    char_arts = file_content.split("\n\n")
    ascii_dict = {}

    for i, art in enumerate(char_arts):
        if i + lower_bound > upper_bound:
            break
        char_key = chr(i + lower_bound)
        ascii_dict[char_key] = art

    return ascii_dict


def generate_ascii_art(string_to_convert, ascii_dict):
    lines = string_to_convert.split("\n")
    ascii_art_lines = []
    character_width = max(len(line) for art in ascii_dict.values() for line in art.split("\n"))

    for line in lines:
        words = line.split() 
        ascii_art_for_line = ['' for _ in range(8)]

        for word in words:
            for char in word:
                if char in ascii_dict:
                    char_art = ascii_dict[char].split("\n")
                    for i in range(8):
                        ascii_art_for_line[i] += char_art[i]
                else:
                    for i in range(8):
                        ascii_art_for_line[i] += " " * character_width

            for i in range(8):
                ascii_art_for_line[i] += " " * 4

        ascii_art_lines.append("\n".join(ascii_art_for_line).rstrip())

    return "\n\n".join(ascii_art_lines)


if __name__ == "__main__":
    BANNER_TYPE = ('shadow', 'standard', 'thinkertoy')
    print("Welcome to the ASCII Art Generator!")
    string_to_convert = input("Enter the text to convert into ASCII art: ")
    string_to_convert = string_to_convert.replace("\\n", "\n")
    banner_type = input("Enter the banner type (standard, shadow, thinkertoy): ").strip().lower()

    if banner_type not in BANNER_TYPE:
        print(f"Invalid banner type! Choose from {BANNER_TYPE}.")
        exit(1)

    banner_path = os.path.join("./", f"{banner_type}.txt")
    if not os.path.exists(banner_path):
        print(f"Error: Banner file '{banner_path}' not found.")
        exit(1)

    banner_content = read_banner(banner_path)
    ascii_dict = parse_banner(banner_content)
    ascii_art = generate_ascii_art(string_to_convert, ascii_dict)
    print("Generated ASCII Art:")
    print(ascii_art)
