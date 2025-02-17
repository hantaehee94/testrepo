from collections import Counter

class TextAnalyzer(object):
    def __init__(self, text):
        # Remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # Convert text to lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText

    # Method to calculate frequency of all words
    def freqAll(self):
        wordList = self.fmtText.split(' ')
        freqMap = Counter(wordList)  # More efficient than manually counting
        return freqMap

    # Method to get frequency of a specific word
    def freqOf(self, word):
        freqDict = self.freqAll()
        return freqDict.get(word, 0)  # Returns 0 if word is not found


# Given string
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Create an instance of TextAnalyzer
analyzer = TextAnalyzer(givenstring)

# Print word frequency for all words
all_frequencies = analyzer.freqAll()
print("Word frequencies:", all_frequencies)

# Print frequency of specific words
print("Frequency of 'diam':", analyzer.freqOf('diam'))
print("Frequency of 'amet':", analyzer.freqOf('amet'))
print("Frequency of 'lorem':", analyzer.freqOf('lorem'))