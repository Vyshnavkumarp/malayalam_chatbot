from transformers import pipeline

qa_pipeline = pipeline("question-answering")

context = """
Hola! 
I'm Vinayak
I solve problems using something called A.I  ; )
I'm Vinayak - currently an active student of Artificial Intelligence. I am on a journey to helping companies build better products with Artificial Intelligence and also learn new things.

P.S, I have a love for design as well."""

question = "Who is Vinayak?"
answer = qa_pipeline(question=question, context=context)
print(answer)
