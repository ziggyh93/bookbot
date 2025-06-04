import sys

from stats import word_count

from stats import char_count

from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    print (sys.argv)

    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    file_contents = get_book_text(filepath)
    num_words = word_count(file_contents)
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    char_count_dict = char_count(file_contents)
    sort_list = sorted_list(char_count_dict)
    print ("-------- Character Count --------")
    for char in sort_list:
        if char["char"].isalpha():
            print (f"{char['char']}: {char['num']}")
    print ("============= END =============")

main()
