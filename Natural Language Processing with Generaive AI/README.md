# Natural Language Processing with Generative AI

This folder moves from classical text representations (Bag-of-Words, Word2Vec/GloVe) to transformer-based embeddings, then to prompting large language models (OpenAI GPT-4o-mini and a local LLM via `llama-cpp-python`), then to Retrieval-Augmented Generation (RAG) fundamentals, and finishes with a capstone RAG system built on a local LLM.

---

## Core concepts

### From text to numbers
- **Bag-of-Words / `CountVectorizer`** — text preprocessing (lowercasing, stopword removal, stemming with `PorterStemmer`) followed by sparse word-count vectors fed into classical classifiers.
- **Word2Vec / GloVe** — dense, pretrained or self-trained word embeddings (via `gensim`) that capture semantic similarity between words, aggregated (e.g. averaged) into a single vector per document.
- **Sentence-transformers** — transformer models that embed entire sentences/documents directly into dense vectors, used for clustering, similarity, and as classifier features.

### Generative / LLM approaches
- **T5 (`T5Tokenizer` / `T5ForConditionalGeneration`)** — a text-to-text transformer used here for generative sentiment classification and summarization-style tasks, contrasted against classic feature + `RandomForestClassifier` pipelines.
- **Prompt engineering** — structuring system/user prompts, response parameters (`max_tokens`, `temperature`, `top_p`), and structured (JSON) outputs for both a hosted LLM (OpenAI `gpt-4o-mini`) and a local LLM (`llama-cpp-python`), iterating on prompt design across successively richer classification/summarization tasks.
- **Retrieval-Augmented Generation (RAG)** — combining a vector database (`Chroma`) of document chunks with a local LLM (`llama-cpp-python`) so answers are grounded in retrieved source text instead of the model's parametric memory alone. Byte-Pair Encoding tokenization (`tiktoken`) and sentence-embedding pooling are covered as the RAG building blocks before the full pipeline is assembled.

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

### LLMs and Prompt Engineering (`LLMs and Prompt Engineering/`)

| Folder / file | Notebook | Approach | Data |
|---|---|---|---|
| — | [LLM_Hands_on_Prompt_Engineering_Notebook.ipynb](LLMs%20and%20Prompt%20Engineering/LLM_Hands_on_Prompt_Engineering_Notebook.ipynb) | Introductory hands-on with the OpenAI client: response parameters (`max_tokens`, `temperature`, `top_p`), zero-shot/few-shot prompting, and structured-output prompting | — |
| `Case Study - Restaurant Review Analysis/` | [MLS_Restaurant_Review_Analysis_Notebook.ipynb](LLMs%20and%20Prompt%20Engineering/Case%20Study%20-%20Restaurant%20Review%20Analysis/MLS_Restaurant_Review_Analysis_Notebook.ipynb) | Iterative prompt engineering with `gpt-4o-mini`: plain sentiment → structured JSON output → aspect-based sentiment → liked/disliked feature extraction → auto-generated customer response, ending in business insights/recommendations | `restaurant_reviews.csv`, `config.json` (OpenAI key placeholder) |
| `Case Study - News Article Categorization and Summarization/` | [Case_Study_News_Article_Categorization_and_Summarization-1.ipynb](LLMs%20and%20Prompt%20Engineering/Case%20Study%20-%20News%20Article%20Categorization%20and%20Summarization/Case_Study_News_Article_Categorization_and_Summarization-1.ipynb) | Prompt engineering with a locally-run LLM (`llama-cpp-python`, Hugging Face model download): article classification → structured output → headline generation → summarization, all via prompt design rather than fine-tuning | `Dataset - articles.csv` |

**Note:** the Restaurant Review notebook expects real OpenAI credentials in `config.json` (`OPENAI_API_KEY`, `OPENAI_API_BASE`) — the committed file only holds placeholder values.

### Retrieval Augmented Generation (`Retrieval Augmented Generation/`)

Builds the RAG pipeline up in stages before the full capstone: tokenization/embeddings fundamentals, a guided RAG walkthrough, and an applied document-Q&A case study.

| Folder | Notebook | Approach | Data |
|---|---|---|---|
| `Additional Learning Material - Understanding_Embeddings/` | [Understanding_Embeddings.ipynb](<Retrieval%20Augmented%20Generation/Additional%20Learning%20Material%20-%20Understanding_Embeddings/Understanding_Embeddings.ipynb>) | Byte-Pair Encoding tokenization (`tiktoken`), computing sentence embeddings with `sentence-transformers`, then applying them to legal-domain use cases: finding similar legal cases and clustering legal documents (`KMeans`, `t-SNE`) | `legal_cases.csv`, `legal_documents.csv` |
| `Hands-On Notebook/` | [RAG_Colab.ipynb](<Retrieval%20Augmented%20Generation/Hands-On%20Notebook/RAG_Colab.ipynb>) | Guided end-to-end RAG walkthrough: load & chunk a document, embed chunks, load a local LLM (`llama-cpp-python`), build a `langchain` retrieval chain, run and evaluate a query | `AAPL-MDA.txt` (Apple 10-K Management's Discussion & Analysis excerpt) |
| `Case Study - Apple HBR Report Document Q&A/` | [MLS_Apple_HBR_Notebook_V2.ipynb](<Retrieval%20Augmented%20Generation/Case%20Study%20-%20Apple%20HBR%20Report%20Document%20Q%26A/MLS_Apple_HBR_Notebook_V2.ipynb>) | Full RAG case study over a business report: PDF loading, chunking, embedding, vector store + retriever, local-LLM response generation, prompt/parameter tuning across 3 queries, and LLM-based output evaluation | `HBR_How_Apple_Is_Organized_For_Innovation-4.pdf` |

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
7. `LLMs and Prompt Engineering/` — prompt a hosted LLM (OpenAI) and a local LLM (`llama-cpp-python`) directly, iterating on prompt design for classification, structured output, and summarization
8. `Retrieval Augmented Generation/Additional Learning Material - Understanding_Embeddings/` — tokenization and embedding fundamentals that underpin RAG
9. `Retrieval Augmented Generation/Hands-On Notebook/` and `Case Study - Apple HBR Report Document Q&A/` — guided RAG walkthrough, then an applied document-Q&A case study
10. `Medical Assistant/` — capstone: LLM prompting → RAG → evaluation

---

## Key takeaway

Text representation quality drives everything downstream: moving from sparse Bag-of-Words → dense Word2Vec/GloVe → contextual transformer embeddings steadily improves how much semantic meaning a classifier has to work with. From there, prompting an LLM directly (hosted or local) trades feature engineering for prompt design, and RAG grounds that LLM in retrieved, embedded document chunks so its answers can be scored for groundedness and relevance instead of trusted blindly. The capstone folds all of this together into an auditable, RAG-based question-answering system.

## Notes

- Word embedding notebooks use `nltk` (stopwords, tokenization) and `gensim` (`Word2Vec`, `KeyedVectors`, `glove2word2vec`); the first run of `nltk` may need `nltk.download(...)` for stopword corpora.
- Transformer notebooks use `sentence-transformers` and Hugging Face `transformers` (T5); a GPU speeds these up significantly but is not strictly required except for the Medical Assistant capstone.
- `glove.6B.100d.zip` / `glove.6B.100d.txt` are pretrained GloVe vectors (100-dimensional, 6B-token corpus) used by the Word2Vec/GloVe notebooks.
- The Restaurant Review Analysis notebook needs the `openai` package and a real key in its `config.json`; the News Article Categorization and Summarization, RAG Colab, and Apple HBR notebooks instead download and run a local LLM via `llama-cpp-python` + `huggingface_hub` (no API key needed, but slower without a GPU).
- The Understanding_Embeddings notebook additionally needs `tiktoken` (BPE tokenization) and `sentence-transformers`.
- The Medical Assistant capstone additionally needs `langchain`, `langchain-community`, `chromadb`, `pymupdf`, `llama-cpp-python`, and `huggingface_hub`, and **requires a T4 GPU runtime**.
- Run notebooks from within their own folder so relative CSV/PDF/TXT paths resolve correctly.
