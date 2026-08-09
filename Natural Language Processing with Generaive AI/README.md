# Natural Language Processing with Generative AI

This folder moves from classical text representations (Bag-of-Words, Word2Vec/GloVe) to transformer-based embeddings and generative models (T5, sentence-transformers), and finishes with a capstone Retrieval-Augmented Generation (RAG) system built on a local LLM.

---

## Core concepts

### From text to numbers
- **Bag-of-Words / `CountVectorizer`** — text preprocessing (lowercasing, stopword removal, stemming with `PorterStemmer`) followed by sparse word-count vectors fed into classical classifiers.
- **Word2Vec / GloVe** — dense, pretrained or self-trained word embeddings (via `gensim`) that capture semantic similarity between words, aggregated (e.g. averaged) into a single vector per document.
- **Sentence-transformers** — transformer models that embed entire sentences/documents directly into dense vectors, used for clustering, similarity, and as classifier features.

### Generative / LLM approaches
- **T5 (`T5Tokenizer` / `T5ForConditionalGeneration`)** — a text-to-text transformer used here for generative sentiment classification and summarization-style tasks, contrasted against classic feature + `RandomForestClassifier` pipelines.
- **Retrieval-Augmented Generation (RAG)** — combining a vector database (`Chroma`) of document chunks with a local LLM (`llama-cpp-python`) so answers are grounded in retrieved source text instead of the model's parametric memory alone.

### Evaluation
- Classic pipelines: `accuracy_score`, `confusion_matrix`, `classification_report`, `GridSearchCV` for hyperparameter tuning.
- RAG pipeline: LLM-as-judge prompts for **groundedness** (is the answer supported by retrieved context?) and **relevance** (does the answer address the question?).

---

## Notebooks

### Word Embeddings (`Word Embeddings/`)

| Folder | Notebook | Approach | Dataset |
|---|---|---|---|
| `Hands_on_Word2Vec_GloVe/` | [Hands_on_Word2Vec_GloVe_Notebook.ipynb](Word%20Embeddings/Hands_on_Word2Vec_GloVe/Hands_on_Word2Vec_GloVe_Notebook.ipynb) | Movie review sentiment: text cleaning (`nltk`, `spacy`, `unidecode`), `CountVectorizer`/`TfidfVectorizer` baselines vs. self-trained `Word2Vec` and pretrained GloVe vectors, `RandomForestClassifier` | `movie_reviews.csv` |
| `Case Study - Word Embeddings/` | [MLS_Articles_Categorization_Notebook.ipynb](Word%20Embeddings/Case%20Study%20-%20Word%20Embeddings/MLS_Articles_Categorization_Notebook.ipynb) | News article categorization using `Word2Vec` and GloVe (`glove2word2vec`, `KeyedVectors`) document embeddings + `RandomForestClassifier` with `GridSearchCV` | `Articles.csv`, `glove.6B.100d.zip` |
| `Case Study - Product Reviews Sentiment Analysis/` | [Case_Study_Product_Review_Sentiment_Analysis.ipynb](Word%20Embeddings/Case%20Study%20-%20Product%20Reviews%20Sentiment%20Analysis/Case_Study_Product_Review_Sentiment_Analysis.ipynb) | Baseline sentiment pipeline: `nltk` cleaning + stemming, `CountVectorizer` (Bag-of-Words), `RandomForestClassifier` + `GridSearchCV` | `Product_Reviews.csv` |
| `Additonal Case Study - Word Embeddings/` | [Case_Study_Product_Review_Sentiment_Analysis_Word_Embeddings-1.ipynb](Word%20Embeddings/Additonal%20Case%20Study%20-%20Word%20Embeddings/Case_Study_Product_Review_Sentiment_Analysis_Word_Embeddings-1.ipynb) | Same product review problem re-solved with `Word2Vec`/`KeyedVectors` embeddings instead of Bag-of-Words, for direct comparison against the BoW notebook above | `Product_Reviews.csv` |
| `Case Study - Airline Customer Reviews Sentiment Analysis/` | [Session Notebook - Airline Customer Review Sentiment Analysis.ipynb](Word%20Embeddings/Case%20Study%20-%20Airline%20Customer%20Reviews%20Sentiment%20Analysis/Session%20Notebook%20-%20Airline%20Customer%20Review%20Sentiment%20Analysis.ipynb) | Airline tweet sentiment: `nltk` cleaning, `CountVectorizer`, `LabelEncoder`, `RandomForestClassifier` + `GridSearchCV`, precision/recall/F1 evaluation | `Dataset - US_Airways.csv` |

### Transformers (`Transformers/`)

| Folder | Notebook | Approach | Dataset |
|---|---|---|---|
| `Hands_on_Transformers/` | [Hands_on_Transformers_Notebook.ipynb](Transformers/Hands_on_Transformers/Hands_on_Transformers_Notebook.ipynb) | Introductory hands-on: `sentence-transformers` embeddings + `RandomForestClassifier`, and generative sentiment classification with `T5ForConditionalGeneration` | `movie_reviews.csv` |
| `Case Study - Airline Customer Review Sentiment Analysis/` | [MLS1_Customer_Sentiment_Analysis-1.ipynb](Transformers/Case%20Study%20-%20Airline%20Customer%20Review%20Sentiment%20Analysis/MLS1_Customer_Sentiment_Analysis-1.ipynb) | Generative sentiment classification with `T5Tokenizer`/`T5ForConditionalGeneration`, word clouds, `nltk` | `US_Airways.csv` |
| `Case Study - Product Reviews Sentiment Analysis/` | [Case_Study_Product_Review_Sentiment_Analysis_Transformers-1.ipynb](Transformers/Case%20Study%20-%20Product%20Reviews%20Sentiment%20Analysis/Case_Study_Product_Review_Sentiment_Analysis_Transformers-1.ipynb) | `sentence-transformers` document embeddings + `RandomForestClassifier`, compared against `T5` generative classification | `Product_Reviews.csv` |
| `Case Study - News Article Categorization/` | [MLS_News_Article_Categorization_Notebook_V3.ipynb](Transformers/Case%20Study%20-%20News%20Article%20Categorization/MLS_News_Article_Categorization_Notebook_V3.ipynb) | `sentence-transformers` article embeddings, `KMeans` clustering, cosine similarity, and supervised categorization with `classification_report` | `news_articles.csv`, `news_article_labels.csv` |

### Medical Assistant — RAG capstone (`Medical Assistant/`)

Full-code RAG project: build a question-answering assistant over the *Merck Manuals* (a 4,000+ page medical reference) that first answers with a raw LLM, then with prompt-engineered LLM calls, then with a full retrieval-augmented pipeline, and finally evaluates groundedness/relevance of the generated answers.

| File | Description |
|---|---|
| [Full_Code_NLP_RAG_Project_Notebook_.ipynb](Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb) | End-to-end RAG pipeline: `PyMuPDFLoader` to parse the PDF, `RecursiveCharacterTextSplitter` for chunking, `SentenceTransformerEmbeddings` for embeddings, `Chroma` as the vector store, a locally-run LLM via `llama-cpp-python`/`huggingface_hub`, prompt engineering (5+ parameter combinations), and LLM-based groundedness/relevance evaluation |
| `medical_diagnosis_manual.pdf` | Source corpus — the Merck Manuals medical reference (~20 MB, 4,000+ pages) |
| `problem_statement.md` | Business context, objective, and the 5 target medical questions the assistant must answer |
| `rubrics.md` | Grading rubric (LLM QA, prompt engineering, RAG data prep, RAG QA, output evaluation, business recommendations) |
| `faq.md` | Setup notes, including a fix for the `llama-cpp-python` dependency conflict during install |

**Note:** requires a GPU runtime (Google Colab: **Runtime → Change runtime type → T4 GPU**).

---

## Suggested order

1. `Word Embeddings/Case Study - Product Reviews Sentiment Analysis/` — classic Bag-of-Words baseline
2. `Word Embeddings/Additonal Case Study - Word Embeddings/` — same problem re-solved with Word2Vec, to see the difference embeddings make
3. `Word Embeddings/Hands_on_Word2Vec_GloVe/` — Word2Vec vs. pretrained GloVe, side by side
4. `Word Embeddings/Case Study - Word Embeddings/` and `Case Study - Airline Customer Reviews Sentiment Analysis/` — apply embeddings to new domains
5. `Transformers/Hands_on_Transformers/` — move from static embeddings to transformer sentence embeddings + generative (T5) classification
6. `Transformers/Case Study - *` — apply transformers to airline reviews, product reviews, and news categorization
7. `Medical Assistant/` — capstone: LLM prompting → RAG → evaluation

---

## Key takeaway

Text representation quality drives everything downstream: moving from sparse Bag-of-Words → dense Word2Vec/GloVe → contextual transformer embeddings steadily improves how much semantic meaning a classifier has to work with. The capstone folds all of this into a generative-AI capstone: an LLM alone can hallucinate, but grounding it in retrieved, embedded document chunks (RAG) — and then scoring its answers for groundedness and relevance — turns it into an auditable question-answering system.

## Notes

- Word embedding notebooks use `nltk` (stopwords, tokenization) and `gensim` (`Word2Vec`, `KeyedVectors`, `glove2word2vec`); the first run of `nltk` may need `nltk.download(...)` for stopword corpora.
- Transformer notebooks use `sentence-transformers` and Hugging Face `transformers` (T5); a GPU speeds these up significantly but is not strictly required except for the Medical Assistant capstone.
- `glove.6B.100d.zip` / `glove.6B.100d.txt` are pretrained GloVe vectors (100-dimensional, 6B-token corpus) used by the Word2Vec/GloVe notebooks.
- The Medical Assistant capstone additionally needs `langchain`, `langchain-community`, `chromadb`, `pymupdf`, `llama-cpp-python`, and `huggingface_hub`, and **requires a T4 GPU runtime**.
- Run notebooks from within their own folder so relative CSV/PDF paths resolve correctly.
