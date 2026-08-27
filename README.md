# Text Similarity Checker

## About the Project

This is a small NLP project I built for my **NLTK portfolio**. The goal was to practice some basic Natural Language Processing techniques and see how they can be combined in a simple text comparison program.

The program takes two texts from the user and compares the words they contain. It cleans the text, removes some common words, applies lemmatization, and then calculates a similarity score.

It also shows which words are shared between the two texts and which words appear only in one of them.

## What I Practiced

This project helped me practice:

- **Tokenization** using `wordpunct_tokenize`
- **Text cleaning**
- **Lowercase conversion**
- **Stop-word removal**
- **Lemmatization** using `WordNetLemmatizer`
- **Python sets** for comparing words
- **Jaccard similarity** for calculating the similarity score

## How It Works

The program first asks the user to enter two texts.

The text is converted to lowercase and split into tokens. Punctuation and non-alphabetic tokens are removed, along with a small custom list of common English words.

The remaining words are stored as sets so they can easily be compared.

The program also uses `WordNetLemmatizer` with the verb part of speech. This allows some different forms of verbs to be treated as the same base word.

The similarity score is calculated using **Jaccard similarity**:

```text
Similarity = Number of shared words / Number of unique words
```

The final result is displayed as a percentage.

## Example

For a simple test, I used two sentences that express a very similar idea but have a different sentence structure:

```text
Enter first text: Hi, I was very happy to meet you.
Enter second text: Hi, after meeting you, I became happy.
```

After cleaning and processing the texts, the program compares the words that remain in each sentence.

Example output:

```text
Common words: happy, hi, meet, you
Only in first text: None
Only in second text: become
Similarity score: 80.00%
```

The exact result depends on how the words are processed by the lemmatizer.

This example shows that the program can identify common words even when the **order of the words is different**. However, it does not fully understand that the two sentences have almost the same meaning. It mainly looks at the words themselves.

## Requirements

You need:

- Python 3.x
- NLTK

The required Python package is listed in `requirements.txt`.

Install it with:

```bash
pip install -r requirements.txt
```

The project also uses **WordNet**, which is NLTK data and needs to be downloaded separately.

Run the following in Python:

```python
import nltk
nltk.download("wordnet")
```

If your NLTK setup also requires the Open Multilingual WordNet data, run:

```python
nltk.download("omw-1.4")
```

After installing NLTK and downloading the required data, the project is ready to run.

## How to Run

Clone or download this repository and open a terminal in the project folder.

Install the requirements:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python text_similarity.py
```

Enter the two texts when prompted.

## Project Structure

```text
text-similarity-checker/
│
├── text_similarity.py
├── README.md
└── requirements.txt
```

### `text_similarity.py`

Contains the main Python program that cleans, processes, and compares the two texts.

### `README.md`

Contains information about the project, installation, usage, example, and limitations.

### `requirements.txt`

Contains the external Python package required by the project:

```text
nltk
```

## Limitations

This project is intentionally simple and is mainly meant for learning and portfolio purposes.

The biggest limitation is that it compares **words rather than the actual meaning of the text**. Two sentences can have a very similar meaning but use different words, and the program may still give them a lower similarity score.

Other limitations include:

- The stop-word list is manually created and contains only a limited number of words.
- Lemmatization uses `pos="v"`, so it mainly focuses on verbs.
- Because the program uses sets, repeated words are ignored.
- Synonyms are not recognized. For example, `happy` and `joyful` are treated as different words.
- Word order is not considered when calculating the similarity score.
- The program is not intended to be used as a plagiarism detector.
- It does not perform advanced semantic or contextual analysis.

## What I Learned

This project gave me a practical introduction to some of the basic steps involved in NLP.

I learned how text can be tokenized and cleaned before analysis, how lemmatization can help with different word forms, and how Python sets can be useful when comparing text.

It also helped me understand the difference between **lexical similarity** and **meaning-based similarity**. The current project focuses mainly on the words that appear in the texts, which makes it a useful starting point before moving on to more advanced NLP techniques.

## Future Improvements

Some things I could improve in the future are:

- Use a larger stop-word collection.
- Handle nouns, adjectives, and adverbs during lemmatization.
- Take word frequency into account instead of using only sets.
- Add semantic similarity using word embeddings or another NLP model.
- Create a simple graphical or web interface.
- Add more input validation and error handling.

## Purpose

This project is part of my **NLP/NLTK portfolio** and was created as a hands-on way to practice text preprocessing and basic similarity measurement with Python.
