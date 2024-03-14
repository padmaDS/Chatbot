# import
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
import os
import chromadb
from langchain_community.vectorstores import Chroma
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

openai_client = OpenAI()

embeddings = OpenAIEmbeddings()

file = r'data\Grievances data1.csv'
loader = CSVLoader(file_path= file, encoding = "latin1")
data = loader.load()

## split it into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(data)
# print(docs)

## save to disk
# db2 = Chroma.from_documents(docs, embeddings, persist_directory="./chroma1_db")
new_client = chromadb.EphemeralClient()

## storing the data in the chroma database
vectorstore = Chroma.from_documents(
    docs, embeddings, client=new_client, collection_name="openai_collection"
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0)
retriever = vectorstore.as_retriever()

template = """You are DARPG AI Assistant, which is Ministry Specific to help the Citizens 
to resolve their common queries related to filing a Grievance in the 
CPGRAMS portal and expedite smooth submission of grievances.

If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}
Question: {question}

Helpful Answer:"""

rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
)

query = "What are the contact details of the Department of Administrative Reforms and Public Grievances?"

print(rag_chain.invoke(query))