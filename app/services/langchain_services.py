from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class LangChainService:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = PromptTemplate(
            input_variables=["query"],
            template="O que você acha sobre: {query}?",
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def process_query(self, query: str) -> str:
        return self.chain.run(query)
