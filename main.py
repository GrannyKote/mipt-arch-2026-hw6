import requests

def get_text(url):
    response = requests.get(url)
    return response.text

def count_word_frequencies(frequencies, text):
    text_words = text.split()
    for text_word in text_words:
        if text_word in frequencies:
            frequencies[text_word] += 1
    return 

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    text = get_text(url)

    frequencies = {}
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                frequencies[word] = 0

    
    count_word_frequencies(frequencies, text)
    
    print(frequencies)

if __name__ == "__main__":
    main()