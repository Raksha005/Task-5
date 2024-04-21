from googletrans import Translator

translator=Translator()

word="nevermind"
output=translator.translate(word,dest="hi")
print(output.text)