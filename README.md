# aicode
AI Coding Helper

Code creation and refactorign with ChatGPT assistance.

ai.py contains general settings (C language, doxygen etc.)

**Note: you have to use your API key. Set it with ```setx OPENAI_API_KEY “<yourkey>”``` in command prompt.**


Create a file with some functionality
```
py create.py "Function to get the date following a number of days. Starting date and number of days are paramters"
```

Use a text file for instructions
```
py create.py requirements.txt
```

Refactoring
```
py refactor.py get_next_date.c "Use a struct to store dates" 
```


29.04.2023 - First version C only.
