from googletrans import Translator

translator = Translator()
malayalam_text = "ಟೈಟಾನಿಕ್ ಏನಾಯ್ತು"
translated_text = translator.translate(malayalam_text, src='kn', dest='en').text
print(translated_text)
