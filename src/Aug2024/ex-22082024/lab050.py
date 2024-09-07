#pass--> can be use in statement,functions, class an objects
#match statement
#switch in java
# match the op an execute
# python 3.10
"""match variable:
        case patern1:
        code block
    case patern2:
        code block"""


# write a program to ask the user which browser he want to run automation

browser_name=input("enter the name of browser\n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name=="firefox":
            print("Hello")
        print("execute the firefox code")
    case "crome":
        print("execute the crome code")
    case "edge":
        print("execute the edge code")