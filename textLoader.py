from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain


loader = TextLoader("scrapedText.txt")
pages = loader.load_and_split()
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(pages, embeddings).as_retriever()

# Choose any query of your choice
query = "How can irrigation system companies benefit from it?"
docs = docsearch.get_relevant_documents(query)
# chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
output = chain.run(input_documents=docs, question=query)
print(output)