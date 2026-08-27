from nltk.tokenize import wordpunct_tokenize
from nltk.stem import WordNetLemmatizer

text1 = input("Enter first text: ").lower().strip()
text2 = input("Enter second text: ").lower().strip()
lemmatizer = WordNetLemmatizer()
stop_words = {
    "i", "am", "is", "are", "was", "were",
    "to", "the", "a", "an", "my", "your",
    "of", "and", "in", "on", "for", "with"
}


def clean_text(text):
    tokens = wordpunct_tokenize(text)
    words = []
    for token in tokens:
        if token.isalpha() and token.lower() not in stop_words:
            words.append(token.lower())
    return words


words1 = set(clean_text(text1))
words2 = set(clean_text(text2))
base1 = {lemmatizer.lemmatize(word, pos="v") for word in words1}
base2 = {lemmatizer.lemmatize(word, pos="v") for word in words2}

base_inter = base1 & base2
base_union = base1 | base2

if base_union:
    similar = len(base_inter) / len(base_union)
else:
    similar = 0
inter = words1 & words2
common_words = list(inter)
remaining1 = words1 - words2
remaining2 = words2 - words1
matched1 = set()
matched2 = set()
for word1 in remaining1:
    for word2 in remaining2:
        base_word1 = lemmatizer.lemmatize(word1, pos="v")
        base_word2 = lemmatizer.lemmatize(word2, pos="v")

        if base_word1 == base_word2:
            common_words.append(f"{word1} / {word2}")
            matched1.add(word1)
            matched2.add(word2)
    remaining1 = remaining1 - matched1
    remaining2 = remaining2 - matched2
print("Common words:", ", ".join(sorted(common_words)))
print("Only in first text:", ", ".join(sorted(remaining1)) or "None")
print("Only in second text:", ", ".join(sorted(remaining2)) or "None")
print("Similarity score: {:.2%}".format(similar))
