#command library
#function defining
def function_example("input 1", "input 2"):
    print("This doesn't actually do anything")
    return("It's just an example of formatting. Do include the return clause.")

# = equals set equal, == equals check if equal
#while loop = until a condition is no longer met keep looping it
#if = do it once if its met or not at all if its not
a = 0
while a < 10:
    a = a + 1
    print(a)
a = 1
if a > 5:
    print("This shouldn't happen.")
else:
    print("This should happen.")
#else just means do it if if isn't fulfilled. "elif" is also a thing, means if A isn't true and B is true do X
#remember the colon
#tuple is a list you can't edit
tuple = (1,2,3,4)
print(tuple(1))
#lists you can edit and use square brackets
list = ['a','b','c','d']
print(list[1])
#note that the ID's start with [0]! so the above command prints "b"
#add to list
list.append('e')
print(list[4])
#subtract from list
del list[1]
print(list[3])
#dictionary correlates short keys to long definitions, curly brackets
dictionary = {'Apple':"A red fruit with anti-medical-personnell applications", \
              'Banana':"A yellow fruit used for scaling", \
              'Grape':"A young raisin"}
# \ is used to continue the line and make things readable
#just use dictionary[key] to access the value
print(dictionary['Apple'])
#note that we call the key with square brackets, not curlies
#add entries to the dictionary with dictionary['new key'] = new value
dictionary['Grapefruit'] = "A renegade pineapple"
print(dictionary['Grapefruit'])
#has_key() will return a TRUE value if the given key is somewhere in the dictionary
if dictionary.has_key['Grapefruit']:
    print("The Grapefruit is present. The ritual may begin.")
#list all keys
print(dictionary.keys())
#okay delving into new and confusing
#classes! a class takes inputs and uses them to define functions (the group of resulting functions is an instance)
class example:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.value = "An arbitrary value"
        #the first argument isn't positional but describes the internal marker
    def function(self):
        return(self.x)
    def print(self):
        return(self.value)
#__init__ is a function used to generate an instance of this example class
ex1 = example(2,3)
print(ex1.function())
#When we first describe a class, we are defining it (like with functions)
#The ability to group similar functions and variables together is called encapsulation
#The word 'class' can be used when describing the code where the class is defined (like how a function is defined), and it can also refer to an instance of that class - this can get confusing, so make sure you know in which form we are talking about classes
#A variable inside a class is known as an Attribute
#A function inside a class is known as a method
#A class is in the same category of things as variables, lists, dictionaries, etc. That is, they are objects
#A class is known as a 'data structure' - it holds data, and the methods to process that data
#(shameless quoting)

#you can copy a classes attributes with any changes into a new class with the following syntax
#class New(Old): [whatever you want to add or change]
class example2(example):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.value = "An arbitrary value"
    def function2(self):
        return(self.z)
ex2 = example2(2,3,4)
print(ex2.function2())
#prints 4, our fresh addition
print(ex2.function())
#uses the original function defined in example
#you can store class instances as values (not keys) in dictionaries
class_library = {}
#defines it as a dictionary
class_library["First Example"]= example(2,3)
print(class_library["First Example"].function())
#you can then use the dictionary key+function name to get that output again
#as to python's infamous importing
#import brings in a class definition including functions+variables from another script in the same directory as yours or from python's default scripts
#it can also have non-class functions and variables but its basically one big class
import program
#don't add the .py extension
#this doesn't actually go anywhere because I'm lazy but lets pretend I wrote a separate script called program.py
print(program.function("input"))
#you can also only grab a subset of the module if you know its name
from program import function
#don't need the modifier then
print(function("input"))

#working with text files
openfile = open('path', 'r')
#the second argument is a parameter defining method of opening
#"r"=read only, "w"=writing only (overwrights), "a"=appending, "r+" for both reading & writing
openfile.read()
#there's this cursor thing the program uses while looking at the file, it can only see after the cursor
#so if you did the above command and then
print(openfile.read())
#it would error because its at the end of the document and doesn't know how to go back and read again
#use .seek to set the cursor
#takes two arguments, offset and whence
#offset is the main one, tells you how far to move the cursor
#whence is optional defaults to 0,which is start point
#using it moves the cursor to whence+offset bytes from the start of the file
#note that whence isn't also a byte count, its 0=count from start 1=count from current position 2=from end (use negative offset)
openfile.seek(50,0)
#moves the cursor 50 bytes downstream of the starting point 0
tell()
#describes current location
readline()
#reads from current position to end of the line (to the next /n newline)
openfile.readlines()
#reads all the lines from the current one as separate elements in a list
write()
#writes to a file from the point where the cursor is, overwriting everything in its way like a madman
#watch out for that cursor lest you erase your essay
close()
#closes the file so you can't do anything with filename.function() until you open(path, type) again

#pickles- a pickled python object is saved to a file
import pickle
#pickle module comes with python
#basically the reverse of import
testpickle=[1,2,3]
file=open('testfile','w')
#this creates the file if it doesn't already exist and puts it in write-only mode
pickle.dump(file, testpickle)
file.close()
#now there's a text file that says 1,2,3 called testfile, also other junk (machine code)
unpicklefile = open("testfile", "r")
unpickletest = pickle.load(unpicklefile)
for number in unpickletest
    print item
unpicklefile.close()
#only one pickle per file, but you can load everything, all your classes and such into a dictionary then pickle that

#try and except are good debug operators, ways to display error messages
try:
    function(parameter)
except:
    print("error")
#this catches all errors, you can be more specific with error types
except NameError:
    print("name error")
#this version of except only triggers on an error failure that is a NameError
#additional arguments for stuff includes continue (restart the current loop) and break (ends the loop)
#NameError uses the wrong argument formatting (letter in a number slot), SyntaxError involves odd characters (! or extra parentheses)
#that's the basics of it, learn about additional modules as you go

