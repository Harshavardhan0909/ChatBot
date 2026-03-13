from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from models.embeddings import get_embedding_model
from config.config import DOCUMENT_PATH


def load_documents():
    try:
        with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
            text = f.read()

        splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        docs = splitter.split_text(text)

        return docs

    except Exception as e:
        raise RuntimeError(f"Document loading failed: {str(e)}")


def create_vector_store():

    docs = load_documents()
    embeddings = get_embedding_model()

    vectorstore = FAISS.from_texts(docs, embeddings)

    return vectorstore


def retrieve_context(query):

    vectorstore = create_vector_store()

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    return context