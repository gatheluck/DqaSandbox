import pathlib
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from typing import List

input_path = pathlib.Path("./data/cvpr2023/Takashima_Visual_Atoms_Pre-Training_Vision_Transformers_With_Sinusoidal_Waves/mathpix")
# latex_text = input_path.read_text()

# https://python.langchain.com/en/latest/modules/indexes/text_splitters/examples/code_splitter.html#latex
# latex_splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.LATEX,  # this arg decides separators
#     # encoding_name="cl100k_base",  # cl100k_base is also used at gpt-4
#     chunk_size=1000,
#     chunk_overlap=0,
#     keep_separator=True,
# )

# latex_docs = latex_splitter.create_documents([latex_text])
# print(latex_docs)

loader = TextLoader(str(input_path))
documents = loader.load()

# print(documents)

text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",  # cl100k_base is also used at gpt-4
    chunk_size=300,
    chunk_overlap=20,
    keep_separator=True,
)
docs: List[str] = text_splitter.split_documents(documents)

# print(docs)
# print(len(docs)) # 53

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",  # https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
)
db = FAISS.from_documents(docs, embeddings)
output_path = input_path = pathlib.Path("./data/cvpr2023/Takashima_Visual_Atoms_Pre-Training_Vision_Transformers_With_Sinusoidal_Waves/index/")
db.save_local(str(output_path))