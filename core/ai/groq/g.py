GROQ_KEY = "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"
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.chains.retrieval import create_retrieval_chain
import pdfplumber
from langchain_core.documents import Document
from .legal_embeddings import LegalEmbeddings
from django.contrib.staticfiles import finders

def _read_file(fp):
        docs = []
        with pdfplumber.open(fp) as f:
            for page_number, page in enumerate(f.pages, start=1):
                lines = page.extract_text().split("\n")
                docstr = "\n".join(lines)
                document = Document(docstr, metadata={'source': fp, 'page': page_number-1})
                docs.append(document)
        return docs

def _format_docs(docs):
    s = ""
    for doc in docs:
        s += doc.page_content + "\n\n"
    return s

class Chatbot:
    def __init__(self):
        self._chat = ChatGroq(temperature=0, groq_api_key=GROQ_KEY, model_name="llama-3.3-70b-versatile")
        self._init_file = finders.find('laws.pdf')
        self._init_docs = _read_file(self._init_file)
        self._text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self._splits = self._text_splitter.split_documents(self._init_docs)
        self._embedding_custom = LegalEmbeddings()
        self._vectorstore = Chroma.from_documents(documents=self._splits, embedding=self._embedding_custom)
        self._retriever = self._vectorstore.as_retriever(search_kwargs={"k": len(self._init_docs)})
        self._system_prompt = (
            "You are an assistant for question-answering tasks related to traffic laws for specific states."
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise. Don't provide irrelevant info to the prompt, "
            "nor states that aren't directly mentioned in the prompt."
            "\n\n"
            "{context}"
        )
        self._prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self._system_prompt),
                ("human", "{input}"),
            ]
        )
        self._question_answer_chain = create_stuff_documents_chain(self._chat, self._prompt)
        self._rag_chain = create_retrieval_chain(self._retriever, self._question_answer_chain)

    def respond(self, query: str):
        return self._rag_chain.invoke({"input": query})
