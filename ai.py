import openai
import os

openai.api_key  = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

#Include this description in the header comment in the format "<instruction> ... </instruction>"
def get_code (function, filename):
    prompt = f"""
    Write a C code as described in the triple backticks
    ```{function}```
    The code will be saved in a file named {filename}
    Include 5 test cases that print parameter, expected value, actual value and the test outcome.
    Add doxygen comments.
    Use camel case for names.
    """

    response = get_completion(prompt)
    return (response)

def get_filename (function):
    prompt = f"""
    Choose a good filename for the C code described in the triple backticks
    ```{function}```
    Reply with the sole file name, without any other comment or consideration.
    """
    
    filename = get_completion(prompt)
    return (filename)
    
def refactor (code, instruction):
    prompt = f"""
    Modify the code between the tags <code> ... </code>
    following the instruction provided  between the tags <instr> ... </instr>.
    Return the entire code with modification, without enclosing tags.
    
    <code>{code}</code>
    
    <instr>{instruction}</instr>
    """

    response = get_completion(prompt)
    return (response)

if __name__ == "__main__":
    function = f"""
    The function should return the date 
    of the day after the one provided as parameter.
    Use an enum for months.
    """

    filename = get_filename (function)
    code = get_code (function,filename)

    print (filename)
    print (code)
