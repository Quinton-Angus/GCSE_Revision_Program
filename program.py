topics = [
   "Computer systems", 
   "Data representation", 
   "Images", 
   "Sound", 
   "Programming fundamentals", 
   "Making robust programs", 
   "IDEs and programming languages logic"
   ]

questions = [
   [
      [ "What is the function of RAM?" , [ "To store the cpu status" , "To store the device firmware" , "To store the temporary data of active programs" , "To load software from the CPU into secondary storage" ], 3]
      ["What does MDR stand for?", [ "Memory Data Read" , "Memory Data Registar" , "Memory Done Read" , "Memory Dump Registar" ], 2]
   ],
   [],
   [],
   [],
   [],
   [],
   []
]

loadedQuestions = []

def printLoadingPercent(percent):
   print(f"{percent}%")
 

def generateQuestions(topicId):
   
   
 

def select_topic():
   print("#----------------------------#")
   print()
   print("Select a topic.")
   print()
   
   indexId = 1
   
   for i in topics:
      print(f"({indexId}) {i}")
      indexId = indexId + 1
   
   print()
   topicSelected = int(input(f"Please select your desired topic (1 - {indexId}): "))
      
select_topic()

generateQuestions(1)