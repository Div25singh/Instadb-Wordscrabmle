# Open the file is input is not there create one
try:
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")
except IOError:
    print("File in.txt does not exist creating default one.")
    in_file = open("in.txt", "w")
    string = """
After completing this project, a learner should be able to understand and implement the following fundamental concepts of Python Programming in solving a real world problem.
Variables
Data Structures
String Lists
Control Structures
If / else statements, For loop
Functions
File Handling and Operations
""".strip()

    print(string, file = in_file)
    in_file.close()
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")

# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first+last)[::-1]

# Function to scramble the word
def scramble(word):
    if len(word) < 3:
        return word

    first = word[:1]
    last = word[-1:]
    mid = word[1:-1]
    
    if last == "." or last == ",":
        last = word[-2:]
        mid = word[1:-2]

    return str(first) + str(shuffle(mid)) + str(last)

# Read the input and write the scrambled words to the output
for line in in_text:
    line = line.strip()
    new_line = ""

    for word in line.split(" "):
        new_line += scramble(word) + " "

    print(new_line, file = out_text)

# Close open files
in_text.close()
out_text.close()
f1=open("in.txt","r")
f2=open("out.txt","r")
print("---------original Text File---------\n",f1.read(),"\n")
print("---------Scrambled Text File---------\n",f2.read())
f1.close()
f2.close()
