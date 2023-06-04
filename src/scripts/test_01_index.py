import tiktoken
from llama_index.node_parser import SimpleNodeParser
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
from llama_index.langchain_helpers.text_splitter import TokenTextSplitter
from llama_index import ServiceContext

if __name__ == "__main__":
    # https://github.com/jerryjliu/llama_index/blob/main/llama_index/readers/file/base.py#L37
    documents = SimpleDirectoryReader(input_dir="./data/cvpr2023/Takashima_Visual_Atoms_Pre-Training_Vision_Transformers_With_Sinusoidal_Waves").load_data()

    print(documents)
    print(len(documents))

    # # Customize text spilitter's parameters
    # text_splitter = TokenTextSplitter(
    #     separator=". ",  # default: " "
    #     chunk_size=300,  # default: 1024 ~= 750 english words
    #     chunk_overlap=20,  # default: 20
    #     tokenizer=tiktoken.get_encoding("cl100k_base").encode  # cl100k_base is also used at gpt-4
    # )

    # node_parser = SimpleNodeParser(text_splitter=text_splitter)

    # # https://gpt-index.readthedocs.io/en/latest/reference/service_context.html
    # service_context = ServiceContext.from_defaults(
    #     node_parser=node_parser
    # )

    # # https://gpt-index.readthedocs.io/en/v0.6.8/guides/primer/index_guide.html
    # index = GPTVectorStoreIndex.from_documents(
    #     documents,
    #     service_context=service_context,
    # )
    # # https://gpt-index.readthedocs.io/en/latest/guides/primer/usage_pattern.html#optional-save-the-index-for-future-use
    # index.storage_context.persist(persist_dir="./data/storage/Takashima_Visual_Atoms_Pre-Training_Vision_Transformers_With_Sinusoidal_Waves")