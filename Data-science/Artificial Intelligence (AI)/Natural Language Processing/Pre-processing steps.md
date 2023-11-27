***Pre preprocessing steps in NLP***
1. Remove HTML tags
2. Remove Extra whitespaces
3. Convert character into ASCII code
    - accented charactor (Non-accented letters are letters without accents. In many languages, accents alter the meaning or pronunciation of certain words. These have mostly fallen away from English, but they are still used in some circumstances, especially when English has absorbed words from other languages that have accents.)
4. Expand contractions and short-forms
5. Remove special characters
---
***Important Pre-processing steps in all files***
Before applying more sophisticated natural language processing (NLP) techniques, it's common to perform pre-processing steps to clean and prepare the raw text data. These steps help standardize the data, remove noise, and create a more manageable and consistent input for further analysis. Here are some pre-processing steps commonly applied in NLP:

1. **Text Lowercasing:**
   - Convert all text to lowercase to ensure consistency and avoid treating the same word with different cases as different entities.

2. **Tokenization:**
     - Break the text into individual words or tokens. Tokenization is a fundamental step in NLP and is often the first step in text processing.
     - ***N-gram***
       - In natural language processing (NLP), an n-gram is a contiguous sequence of n items (or words) from a given sample of text or speech. N-grams are used in various NLP tasks, and they play a crucial role in tokenization. The term "n-gram" refers to the number of items in the sequence. Common choices for n include 1 (unigram), 2 (bigram), 3 (trigram), and so on.

       - Different types of n-grams:
    
       1. **Unigram (1-gram):**
          - A single word is treated as a separate unit. For example, in the sentence "I love natural language processing," the unigrams are ["I", "love", "natural", "language", "processing"].
    
       2. **Bigram (2-gram):**
          - It Consists of two adjacent words. Using the same example sentence, the bigrams are ["I love", "love natural", "natural language", "language processing"].
    
       3. **Trigram (3-gram):**
          - Comprises three adjacent words. In the example sentence, the trigrams are ["I love natural", "love natural language", "natural language processing"].
    
       4. **4-gram, 5-gram, ... (n-gram):**
          - N-grams with larger values of n include more words in each sequence. For instance, 4-grams have four adjacent words, and so on.
    
       - N-grams are widely used in language modeling, text analysis, and feature extraction in NLP. They provide a way to capture local patterns and dependencies between words in a sequence. Here are some applications of n-grams:

       - **Language Modeling:** N-grams are used to model the probability of a word given the previous words in a sequence. This is the basis for various language models.

       - **Text Generation:** N-grams can be used to generate new text based on the patterns observed in a training corpus.

       - **Spell Checking and Correction:** By analyzing common n-grams in a language, it's possible to identify and correct misspellings.

       - **Information Retrieval:** N-grams can be used in search engines to find documents or passages that contain specific sequences of words.

       - **Machine Translation:** N-grams are used to model and predict sequences of words during the translation process.

       - **Sentiment Analysis:** Analyzing n-grams helps in understanding the sentiment expressed in longer phrases or sentences.

3. **Removing Punctuation:**
   - Eliminate punctuation marks from the text as they may not contribute significantly to the meaning in certain contexts.

4. **Removing Special Characters and Numbers:**
   - Remove non-alphabetic characters, numbers, and other symbols that may not carry meaningful information or could introduce noise.

5. **Removing Stopwords:**
   - Remove common words (stopwords) such as "the," "and," "is," which occur frequently in the language but may not contribute much to the overall meaning.

6. **Stemming and Lemmatization:**
   - Reduce words to their base or root form to handle variations of words. Stemming involves removing prefixes or suffixes, while lemmatization considers the context and transforms words to their dictionary form.
   - Example for Lemmatization:
     - To find root word
       - walking -> walk
       - Running -> run
       - bought -> buy
7. **Handling Contractions:**
   - Expand contractions (e.g., "can't" to "cannot") to standardize the representation of words.

8. **Spell Checking and Correction:**
   - Identify and correct spelling errors to improve the accuracy of subsequent analyses.

9. **Removing HTML Tags and URLs:**
   - In text extracted from web pages, remove HTML tags and URLs that may not be relevant for analysis.

10. **Handling Abbreviations:**
    - Expand abbreviations to their full forms for better interpretation.

11. **Whitespace Removal:**
    - Remove extra whitespaces and trim leading or trailing spaces.

12. **Text Normalization:**
    - Standardize and normalize text, such as converting accented characters to their ASCII equivalents.

13. **Handling Emoticons and Special Characters:**
    - Depending on the context, decide whether to keep, remove, or replace emoticons and special characters.
14. **Vectorization:**
    - Word convert into binary.
    - Methods:
      - `**TF-IDF**`
        - TF-IDF, which stands for `Term Frequency-Inverse Document Frequency`, is a numerical statistic used in information retrieval and text mining to evaluate the importance of a word in a document relative to a collection of documents (corpus). TF-IDF is often used in vectorization, where it is employed to represent text data in a format suitable for machine learning algorithms. Let's break down the key components:
These pre-processing steps create a cleaner and more uniform text dataset for subsequent NLP tasks such as tokenization, feature extraction, and model training. The choice of pre-processing steps may vary based on the specific requirements of the task and the characteristics of the text data being analyzed. It's essential to strike a balance between preserving meaningful information and removing irrelevant noise during pre-processing.