from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
from typing import List

class LegalEmbeddings:
    def __init__(self):
        self._model = SentenceTransformer("nlpaueb/legal-bert-base-uncased")
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._model.encode(t).tolist() for t in texts]
    def embed_query(self, query: str) -> List[int]:
        return self._model.encode(query)
