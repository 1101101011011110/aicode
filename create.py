import os
import sys
import ai
import subprocess  

instruction = sys.argv[1]
if os.path.isfile(instruction):
    instrFile = open(instruction, "r")
    instruction = instrFile.read ()
    instrFile.close()

print (f"Creating code following these instructions: {instruction}")

filename = ai.get_filename (instruction)
#while os.path.isfile(filename):
#    filename.replace (".","_.")
    
print (f"File name is {filename}")

code = ai.get_code (instruction, filename)
f = open(filename, "w")
f.write(code)
f.close()

#TODO: this is only good for C/C++
execname = filename.replace (".c",".exe")
print (f"Building {execname}")

cmd = ["gcc", filename, "-o", execname];  
p = subprocess.Popen(cmd);  
p.wait();  

print (f"Executing test cases")
subprocess.call(execname);  #subprocess.call(["./"+execname]);  
