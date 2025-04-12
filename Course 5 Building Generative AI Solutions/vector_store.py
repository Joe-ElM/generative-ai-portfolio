# import os
# import shutil
# from   langchain.vectorstores      import Chroma
# from   langchain.embeddings.openai import OpenAIEmbeddings
# from   langchain.docstore.document import Document


# def prepare_vector_store(df):
#     chroma_db_path = "./chroma_db"
#     if os.path.exists(chroma_db_path):
#         shutil.rmtree(chroma_db_path)

#     documents = [
#         Document(
#             page_content=(
#                 f"Neighborhood            : {row['neighborhood']}\n"
#                 f"Price                   : {row['price']}\n"
#                 f"Bedrooms                : {row['bedrooms']}\n"
#                 f"Bathrooms               : {row['bathrooms']}\n"
#                 f"House Size              : {row['house_size']}\n"
#                 f"Property Type           : {row['property_type']}\n"
#                 f"Description             : {row['description']}\n"
#                 f"Neighborhood Description: {row['neighborhood_description']}"
#             ),
#             metadata={"id": str(idx)}
#         )
#         for idx, row in df.iterrows()
#     ]

#     embedding   = OpenAIEmbeddings()
#     vectorstore = Chroma.from_documents(documents, embedding, persist_directory=chroma_db_path)
#     vectorstore.persist()
    
#     return vectorstore
import os
from langchain.vectorstores      import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document


def prepare_vector_store(df):
    documents = [
        Document(
            page_content=(
                f"Neighborhood            : {row['neighborhood']}\n"
                f"Price                   : {row['price']}\n"
                f"Bedrooms                : {row['bedrooms']}\n"
                f"Bathrooms               : {row['bathrooms']}\n"
                f"House Size              : {row['house_size']}\n"
                f"Property Type           : {row['property_type']}\n"
                f"Description             : {row['description']}\n"
                f"Neighborhood Description: {row['neighborhood_description']}"
            ),
            metadata={"id": str(idx)}
        )
        for idx, row in df.iterrows()
    ]

    embedding = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embedding)
    
    return vectorstore