from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex

if __name__ == "__main__":
    # https://github.com/jerryjliu/llama_index/blob/main/llama_index/readers/file/base.py#L37
    documents = SimpleDirectoryReader(input_dir="./data/cvpr2023").load_data()

    print(documents)
    print(len(documents))

    # https://gpt-index.readthedocs.io/en/v0.6.8/guides/primer/index_guide.html
    index = GPTVectorStoreIndex.from_documents(documents)
    index.save_to_disk("outputs/index.json")