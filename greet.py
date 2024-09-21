from main import myGreetings
from translate import Translator

translator = Translator(to_lang='pt')

for greets in myGreetings:
    # print(greets.title())
    print(translator.translate(greets).title())