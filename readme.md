# Python Training Agenda
[Visit the Githubpages Site for the Live Page](https://vinay87.github.io/python_training)
#### By __Vinay Keerthi__

----
### TODO: Rewrite this.

## Session 1:

### Basics of Python

---

* How to launch the interpreter from Windows or Linux
    
    - How to check if Python is installed correctly on the current system.
    
    - How to search for help.
    
    - How to read the documentation.

* The interpreter as a calculator
    
    - How to do simple calculations in the interpreter. Addition, subtraction, division, multiplication and exponents.
    
    - How to store variables of different types. Integers, Floating point numbers, date and time, strings, directory paths.
    
    - How to read a text file.
    
    - How to write to a text file.
    
    - How to modify a text file.

* Datatypes
    
    - Integers
    
    - Floating Point Numbers
    
    - Strings
        > String Formatters (%s %d %f %r)
        > Escape Sequences (\n \b \\\\ etc)
        
    - Lists
    
    - Dictionaries
    
    - Boolean
        > Boolean Logic

* Conditional Statements
    
    - If.. else
    
    - Nested If else
    
    - Single line if statements.

* Iteration
    
    - For loop
    
    - While loop
    
    - Nested Loops
    
    - The break statement

* Running Python from a *.py file.
    
    - Using an editor
    
    - The 'if \_\_name\_\_ == \"\_\_main\_\_\"' line
    
    - Indentation
    
    - Saving the File

* The os module
    
    - File Paths introduction
    
    - Linux vs Windows paths.
    
    - How to build paths.
        > os.path.join()
    
    - How to check if a file exists
        > os.path.isfile()
    
    - How to check if a folder exists
        > os.path.isdir()
        > os.path.exists()
    
    - How to get the basename of a file, given its path.
        > os.path.basename()
        > os.path.splitext()

    - How to get the current path.
        > os.path.getcwd()
    
    - How to split paths
        > os.path.split()
    
    - How to create a directory
        > os.makedirs()
    
    - How to check which OS the program is running on.
        > os.name()
    
    - How to check the modification time of a file.
        > os.path.getmtime()
    
    - How to check the creation time of a path.
        > os.path.getctime()

* The datetime module
    
    - How to get the current date and time.
        > datetime.datetime.now()
    
    - How to get the current time
        > datetime.datetime.now().time()
    
    - How to get the current date
        > datetime.datetime.now().date()
    
    - How to calculate the difference between two dates.
        > datetime.timedelta(days, seconds, microseconds)
    
    - How to get a particular date or time
        > datetime.date(yyy, mm, dd)
        > datetime.datetime.now().date() + datetime.timedelta(days=30)
    
    - How to read date/time from a string.
        > datetime.datetime.strptime()
        > datetime.date.strptime()
        > datetime.time.strptime()
    
    - How to print time in a specific format.
        > datetime.datetime.strftime()
        > datetime.date.strftime()
        > datetime.time.strftime()

* The csv module
    
    - How to read a csv file
    
    - How to write to a csv file.
    
    - How to find a particular row in a csv file.
    
    - How to modify a csv file.

* Reading User Input 
    
    - input("> ")

* Exercises
    
    - How to ask a user for the information for several people and write that to a file.
        > First name
        > Last Name
        > Date of Birth
    
    - Then it should store the above information and the age to a file: "infodump.csv"

---

## Session 2:

### Intermediate Python
---

* Functions
    
    - Why do we use functions?
    
    - Reusing Code
    
    - import module
    
    - from module import something
    
    - \_\_init\_\_.py file
    
    - os.path.append()

* Reading User Input
    
    - The argparse library

* Writing your first function
    
    - How to write a function to create a series of folders based on some input.
        def create_function(path, template_number = [0, 1, 2, 3])
    
    - Default values to function arguments.
    
    - Common mistakes
    
    - Why is def my_funct(a, b=10) a bad idea?

* Recursive Functions
    
    - The search algorithm
    
    - The sort algorithm

* The shutil module
    
    - How to copy a file
    
    - How to move a file
    
    - How to copy an entire directory and its contents
    
    - How to move an entire directory and its contents

* Exercises
    
    - How to find files in a directory when you know a part of their name and to copy those files into another directory.
    
    - How to open files which might have some text and copy those files into another directory.
    
    - How to write the file data for the above exercises into a csv file which has the modification time, the file name and file paths into a csv.
    
    - Writing a program that does matrix multiplication.
    
    - Writing a program that calculates the factorial of a number.
    
    - Writing a program that calculates the value of Pi to a certain decimal and writes it to a file.

---

## Session 3

### Advanced Python
---

* Modules that come in handy
    
    - pandas
    
    - numpy
    
    - matplotlib
    
    - scipy
    
    - PIL
    
    - xlsxwriter
    
    - xlrd
    
    - multiprocessing

* Exercises
    
    - Making a time sheet
    
    - Making a balance sheet
    
    - Plotting balance sheet
    
    - Plotting time sheet as a barchart
    
    - Plotting a x-bar r Control Chart for a part.
    
    - Saving results to an excel file.
    
    - Using Numpy, scipy.

* Making your own modules
    
    - Version control
    
    - Sharing code
    
    - Good programming principles

