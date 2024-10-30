punc = '''!()-[]{};:'"\,<>./@#$%^&*_~'''

String = input("Enter anything here: ")

empty_str = ""

for i in String:
     if i not in punc:
        empty_str += i
    
print(empty_str)

