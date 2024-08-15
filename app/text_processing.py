import nltk
import spacy

# Ensure necessary resources are downloaded
nltk.download('punkt')

# Load spaCy's small English language model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Tokenization using NLTK
    sentences = nltk.sent_tokenize(text)
    
    # Process text using spaCy for more advanced NLP tasks
    doc = nlp(" ".join(sentences))

    # Optionally, perform more sophisticated processing here
    # For example, extracting named entities, filtering tokens, etc.
    
    # Return processed text (or any other relevant information)
    return doc
