from transformers import pipeline

qa_pipeline = pipeline("question-answering")

context = """
  Apple: A Tech Titan

Apple Inc. is a household name synonymous with sleek design and cutting-edge technology. Founded in 1976 by Steve Jobs and Steve Wozniak, this American multinational corporation has grown from selling personal computers to becoming a leader in consumer electronics and software.  

Apple's product portfolio boasts iconic devices like the iPhone, iPad, and Mac computers. Their software offerings include the iOS and macOS operating systems, along with popular services like iTunes, iCloud, and Apple Music.  

The company is known for its user-friendly interfaces and focus on integration between hardware, software, and services. This focus has created a loyal customer base who appreciate the seamless Apple experience.  

Apple has a rich history of innovation, from the introduction of the first personal computers with a graphical user interface to their pioneering work in mobile devices. They continue to push boundaries and develop new products that shape the way we live and work.  

Today, Apple is one of the most valuable companies in the world. Their dedication to design and user experience has made them a true tech titan. 
"""

question = "In which year apple was founded?"
answer = qa_pipeline(question=question, context=context)
print(answer)
