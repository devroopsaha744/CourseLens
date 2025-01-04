import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.prompts import PromptTemplate

#Configuring API keys
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
hf_token = os.getenv('HF_TOKEN')
pinecone_api_key = os.getenv("PINECONE_API_KEY")


#Instantiating the LLM
chat = ChatGroq(
    temperature=0,
    model="llama-3.3-70b-versatile",
     api_key= groq_api_key
)

#Embedding Model 
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= hf_token)


# Connect to Pinecone
vectorstore = PineconeVectorStore.from_existing_index(
    index_name= 'courselens',
    embedding= embedding,
)

#Setting up the retriever
retriever = vectorstore.as_retriever()

#Prompt Template
template = '''
You are CourseLens, an AI-powered assistant designed to power an AI-driven smart search system for Analytics Vidhya's free courses.
Your primary role is to assist users by answering questions about the available free courses on Analytics Vidhya and quickly suggesting the most relevant courses based on their natural language queries or keywords.
Help users discover course topics, prerequisites, learning paths, and curriculum details by leveraging a RAG-based (Retrieval-Augmented Generation) approach.
Retrieve and recommend courses from a structured knowledge base containing course links, headings, and descriptions while maintaining accuracy and relevance.
Provide clear, concise responses and ensure the search experience is user-friendly and efficient. Also include the course link as well.
{context}:
{Question}:

Answer:

'''
prompt_template = PromptTemplate.from_template(template=template)

#Setting up the chain

#1
set_ret = RunnableParallel(
    {"context": retriever, "Question": RunnablePassthrough()} 
)
rag_chain = set_ret |  prompt_template | chat | StrOutputParser()



#Defining the response function
#1
def generate_response(text):
    response = rag_chain.invoke(text)
    return response

#print(generate_response("I want to learn tableau. How to learn it?"))
