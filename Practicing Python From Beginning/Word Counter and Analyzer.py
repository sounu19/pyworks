def word_analyzer():
    text = input("Enter a sentence or a paragraph: ")

    words = text.lower().split()
    words = [word.strip(".,!?") for word in words]


    total_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = max(word_count.values())
    most_frequent_words = [word for word, count in word_count.items() if count == max_count]


    print(f"\nTotal words: {total_words}")
    print(f"Unique words: {num_unique_words}")
    print(f"Most frequent word(s): {', '.join(most_frequent_words)} ({max_count} occurrences)")

word_analyzer()