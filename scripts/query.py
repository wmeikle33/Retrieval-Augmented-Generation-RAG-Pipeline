import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. Load your local data
loader = TextLoader("your_data.txt")
documents = loader.load()

# 2. Split text into manageable chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# 3. Create vector embeddings and store them in ChromaDB
embeddings = OpenAIEmbeddings()
vector_store = Chroma.from_documents(texts, embeddings)

# 4. Initialize the LLM (e.g., GPT-4)
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# 5. Create the RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

# 6. Ask a question
query = "What is the main topic of the document?"
response = qa_chain.invoke(query)
print(response["result"])
