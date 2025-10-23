def analysewords(words):
    total_words = 0
    characters = 0
    for wordlist in words:
         total_words += len(wordlist)
         characters += sum(len(words) for  words in wordlist)
    avarage = round(characters / total_words, 2) if total_words > 0 else 0
    print(f"- {total_words} Words")
    print(f"- {characters} Characters")
    print(f"- {avarage:.2f} Average word length")
    return None
         
         
     

def collectwords():
     words = []
     while True:
          feed = input("Insert word(empty stops): ")
          if feed == "":
               break
          else: 
               words.append(feed)
     return words

def main():
    print("Program starting.")
    words = []
    words.append(collectwords())
    analysewords(words)
    print("Program ending.")

main()