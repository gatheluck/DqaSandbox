from llama_index import StorageContext, load_index_from_storage

if __name__ == "__main__":
    # https://github.com/jerryjliu/llama_index/blob/main/llama_index/storage/storage_context.py#L24
    storage_context = StorageContext.from_defaults(persist_dir="./data/storage")
    index = load_index_from_storage(storage_context)