def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    make_report(text, book_path)

def sort_on(dict):
      return dict["count"]

def get_book_text(book_path):
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    
def count_words(text):
        words = text.split()
        print(f"The number of words in this text was...{len(words)}!")

def count_letters(text):
      lowered_text = text.lower()
      character_counts = {}
      for letter in lowered_text:
            if letter not in character_counts:
                  character_counts[letter] = 1
            else:
                  character_counts[letter] = character_counts[letter] + 1
      print(f"the number of times each character was used was as follows...")
      print(character_counts)

def make_report(text, book_path):
      lowered_text = text.lower()
      character_counts = {}
      for letter in lowered_text:
            if letter not in character_counts:
                  character_counts[letter] = 1
            else:
                  character_counts[letter] = character_counts[letter] + 1
      ordered_list = [{"char": letter, "count": value} for letter, value in character_counts.items()]
      ordered_list.sort(reverse=True, key=sort_on)
      print(f"-- Begin report of {book_path} --")
      count_words(text)
      for char in ordered_list:
            print(f"the character {char['char']} was found {char['count']} times.")
      print("-- end of report --")




    
                  

main()