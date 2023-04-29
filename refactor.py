import os
import sys
import ai
import subprocess  

filename = sys.argv[1]
if not os.path.isfile(filename):
    sys.exit (f"File {filename} not found")

instruction = sys.argv[2]
if os.path.isfile(instruction):
    instrFile = open(instruction, "r")
    instruction = instrFile.read ()
    instrFile.close()

print (f"Refactoring {filename} following these instructions: {instruction}")

codeFile = open(filename, "r")
code = codeFile.read ()
codeFile.close()

backupfile = filename.replace (".","_.")
f = open(backupfile, "w")
f.write(code)
f.close()
    
newcode = ai.refactor (code, instruction)
#print (newcode) #sys.exit ()
f = open(filename, "w")
f.write(newcode)
f.close()

#TODO: this is only good for C/C++
execname = filename.replace (".c",".exe")
print (f"Building {execname}")

cmd = ["gcc", filename, "-o", execname];  
p = subprocess.Popen(cmd);  
p.wait();  

print (f"Executing test cases")
subprocess.call(execname);  #subprocess.call(["./"+execname]);  
