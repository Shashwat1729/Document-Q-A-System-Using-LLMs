from transformers import pipeline

# Load the pre-trained LLM for Q&A
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(question, document_text):
    # Use the pipeline to generate an answer
    result = qa_pipeline(question=question, context=document_text)
    return result['answer']
