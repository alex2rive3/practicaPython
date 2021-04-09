word = "ababa"#input("Introduce una palabra: ")
#realiza un acambio de valor momentaneo para combertira las palabras en una lista y así luego poder compararlos 
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")