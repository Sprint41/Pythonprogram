# Replace a specific word in a sentence with another word.
user_input=input("Enter a sentence:")
word_to_replace=input("Enter a word to be replaced:")
replaced_word=input("Enter the replacement word:")
new_sentence=user_input.replace(word_to_replace,replaced_word)
print("New sentence is:",new_sentence)