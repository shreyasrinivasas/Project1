import json
#numOfTests=int(input("Enter the number of tests you want to take for quiz:"))
Dict1={
    "Question1":
        {
            "Question":"Which is immutable data structure",
            "Option1": "List",
            "Option2": "Tuple",
            "Option3": "Dictionary",
            "Correct answer": "Option 2"},
    "Question2":
        {
            "Question":"Which is immutable data structure",
            "Option1": "Set",
            "Option2": "List",
            "Option3": "Tuple",
            "Correct answer": "Option 3"},
    "Question3":
        {
            "Question":"What is a correct syntax to output 'Hello World' in Python?",
            "Option1":"print('Hello World')",
            "Option2":'p("Hello World")',
            "Correct answer": "Option 1"},    
    "Question4":
        {
            "Question":"How do you insert COMMENTS in Python code?",
            "Option1":"#Comment",
            "Option1":"//Comment",
            "Option1":"*/comment/*",
            "Correct answer": "Option 1"
        }
            
}
l1=[]
l2=[]
print(type(Dict1))
for i in range(4):
    #print(((list(Dict1.values())[i]).keys()))
    l1=((list(Dict1.values())[i]).keys())
    l2=(list(l1))
    for i in range(len(l2)):
        print(l2[i])
