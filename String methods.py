text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier())
print("1234".isidentifier())
print("ananananananananananan".count("ana"))
print("anananananaanannananan".replace("ana", "banana"))
print("ananananananananananan".find("ana", 1))
print("bbbbbbabbbbbbbabbbbbbbabbbbbabb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "hello, kind-sir;, how may! I be of service today?"
punctuation = ".,;!?-"

#sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)
words = sentence.split(" ")
print(words)

text = "sohrab caw caw"
print(text.upper())

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}")

