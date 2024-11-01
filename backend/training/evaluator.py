import os
print(os.getcwd())

# training/evaluator.py
from backend.models.llm_models import HFModel 
from vectorstore.vectorstore_manager import VectorStoreManager
from edges import get_rag_prompt
from edges import get_retrieval_grader_prompt
from edges import get_hallucination_grader_prompt

class Evaluator:
    def __init__(self):
        self.llm = HFModel()
        self.vectorstore_manager = VectorStoreManager()

    def test_query(self, question):
        # Retrieve documents and format the context
        docs = self.vectorstore_manager.retrieve_documents(question)
        context = "\n\n".join(doc.page_content for doc in docs)
        
        # Generate the response
        rag_prompt = get_rag_prompt(context, question)
        response = self.llm.generate_response(rag_prompt)
        print("Response:", response)

        # Relevance grading
        retrieval_grader_prompt = get_retrieval_grader_prompt(context, question)
        relevance_grade = self.llm.generate_json_response(retrieval_grader_prompt)
        print("Relevance Grade:", relevance_grade['binary_score'])

        # Hallucination grading
        hallucination_grader_prompt = get_hallucination_grader_prompt(response)
        hallucination_grade = self.llm.generate_json_response(hallucination_grader_prompt)
        print("Hallucination Grade:", hallucination_grade['binary_score'])
        print("Explanation:", hallucination_grade['explanation'])

if __name__ == "__main__":
    evaluator = Evaluator()
    test_question = "What are the rules for a weather situation to count for a full hour?"
    evaluator.test_query(test_question)
