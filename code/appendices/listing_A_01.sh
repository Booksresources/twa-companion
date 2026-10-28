# Listing A.1: Creating the environment used throughout the book
python -m venv twa-env
# Windows:      twa-env\Scripts\activate
# macOS/Linux:  source twa-env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt          # from the companion repository
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download(['punkt_tab', 'stopwords', 'wordnet'])"
python -c "import nltk; nltk.download(['brown', 'reuters', 'movie_reviews'])"
python -c "import nltk; nltk.download(['udhr', 'vader_lexicon'])"
