1) Check you have python installed
#python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

2) check you have Flask installed
#pip install Flask
Requirement already satisfied: Flask in /Library/Python/2.7/site-packages
Requirement already satisfied: Werkzeug>=0.7 in /Library/Python/2.7/site-packages (from Flask)
Requirement already satisfied: Jinja2>=2.4 in /Library/Python/2.7/site-packages (from Flask)
Requirement already satisfied: itsdangerous>=0.21 in /Library/Python/2.7/site-packages (from Flask)
Requirement already satisfied: MarkupSafe in /Library/Python/2.7/site-packages (from Jinja2>=2.4->Flask)


3) Execute the below command to start the flask server
#python hello.py

4) Now the application should be up and running. You can test that using the below commands.

  #curl -v -H "Accept: application/json" http://127.0.0.1:5000/

  #curl -H "Accept: application/json" -X POST http://127.0.0.1:5000/
  
  #curl -X POST http://127.0.0.1:5000/
    
  #curl http://127.0.0.1:5000/
  
5) run hello_test.py to test the use cases
#python hello_test.py
