sentence = input("please enter a sentence: ")

letter_count = {letter:sentence.count(letter)for letter in sentence}
print(letter_count)