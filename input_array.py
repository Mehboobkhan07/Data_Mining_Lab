# Step 1: Define stop words
stop_words = {"is", "the", "an", "a", "in", "of", "and"}

# Step 2: Take 5 sentences as input
sentences = []
for i in range(5):
    line = input(f"Enter sentence {i+1}: ")
    sentences.append(line.split())

# Step 3: Remove stop words and convert to lowercase
clean_sentences = []
for sent in sentences:
    new_sent = []
    for w in sent:
        word = w.lower()
        if word not in stop_words:
            new_sent.append(word)
    clean_sentences.append(new_sent)

# Step 4: Collect all words together
all_words = []
for sent in clean_sentences:
    for w in sent:
        all_words.append(w)

# Step 5: Find unique words
unique_words = []
for w in all_words:
    if w not in unique_words:
        unique_words.append(w)

# Step 6: Count frequency of each word
freq = {}
for w in unique_words:
    count = 0
    for x in all_words:
        if w == x:
            count += 1
    freq[w] = count

# Step 7: Print word frequencies and where they appear
print("\nWord Frequency:")
for word in unique_words:
    appears_in = []
    for i in range(len(clean_sentences)):
        if word in clean_sentences[i]:
            appears_in.append(i+1)
    print(f"{word}: {freq[word]}, appears in sentences {appears_in}")

# Step 8: Find word with highest frequency
if len(freq) > 0:
    max_word = None
    max_count = 0
    for word in freq:
        if freq[word] > max_count:
            max_word = word
            max_count = freq[word]
    print(f"\nMost frequent word: '{max_word}' -> {max_count} times")
else:
    print("\nNo valid words after removing stop words")

# Step 9: Compare sentences for similarity
print("\nSentence Similarity (common words):")
max_common = 0
similar_pair = (0, 0)

for i in range(5):
    for j in range(i+1, 5):
        common = 0
        for w in clean_sentences[i]:
            if w in clean_sentences[j]:
                common += 1
        print(f"Sentence {i+1} and {j+1} -> {common} common words")
        if common > max_common:
            max_common = common
            similar_pair = (i+1, j+1)

# Step 10: Print most similar pair
if max_common > 0:
    print(f"\nMost similar sentences: {similar_pair[0]} and {similar_pair[1]} -> {max_common} common words")
else:
    print("\nNo similarity found between sentences")
