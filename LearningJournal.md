# Reflection Questions

### 1. What experiences have you had with coding and/or programming so far? What other experiences (programming-related or not) have you had that may help you as you progress through this course?

- I've completed the Full Stack Web Development Immersion which covers MERN & MEAN Stack. 
  
- Check out my portfolio at [sam-my.com](http://sam-my.com)

- I've been in the mortgage/banking industry for 15+ years and am working on a transition to tech.

- I've also had experience in call center tech support and customer service.

- My communication & troubleshooting skills helped me learned how to code methodically and be able to internalize this programming learning experience in a relatable & simple way. 

### 2. What do you know about Python already? What do you want to know?

- Not much outside that it is predominatly used in Machine Learning, Data Science & AI. 

### 3. What challenges do you think may come up while you take this course? What will help you face them? Think of specific spaces, people, and times of day or week that might be favorable to your facing challenges and growing. Plan for how to solve challenges that arise.

- I'm sure I'll get stuck with and troubleshoot just to find out something silly like I forgot to capitalize something or a trailing slash. 

- Knowing that I have a mentor that I can reach out to is comforting
- The internet, AI, checking forums, learning how to use the python version/techniques of console logging and debugging.   

## Exercise 1.1: Getting Started with Python 

### 1.	In your own words, what is the difference between frontend and backend web development? If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?

- Frontend is what the user sees visually on the web app: for example buttons, images, text, all the pages and forms etc. 

- Backend is when the user enters info or requests/retrieve data like clicking a button or submitting a form. 
   -  a. A process happens that either grabs info from the server or delivers info to the server handling it to update/store it in the database as necessary: API. For example, loading a picture of a movie poster when the user clicks on an icon or link. 
  
   - b. This involves a security system that handles the user logging in or registering where the user has to be verified: Authentication. 
  
   - c. Also a system is in place where user priveleges have been defined: Authorization.  

### 2.	Imagine you’re working as a full-stack developer in the near future. Your team is asking for your advice on whether to use JavaScript or Python for a project, and you think Python would be the better choice. How would you explain the similarities and differences between the two languages to your team? Drawing from what you learned in this Exercise, what reasons would you give to convince your team that Python is the better option? 
(Hint: refer to the Exercise section “The Benefits of Developing with Python”)

- Based on what I've learned in this course so far in exercise 1.1: 
  
- Python may be easier to read due to it's syntax resembling the natural English language which can make it easier to use and learn when having a team of newer developers or a team that wants to incorporate AI or Machine Learning in the project later down the road.  

### 3.	Now that you’ve had an introduction to Python, write down 3 goals you have for yourself and your learning during this Achievement. You can reflect on the following questions if it helps you. What do you want to learn about Python? What do you want to get out of this Achievement? Where or what do you see yourself working on after you complete this Achievement?

- I want to demonstrate that I'm versatile to be able to learn a new language outside of the MERN & MEAN stack that I already know. 

- I want to put in practice what the programming & troubleshooting techniques I've learned so far to picking up Python. 

- I want to position myself and use this as a stepping stone to better learn about AI and Machine Learning in the future.

## Exercise 1.2: Data Types in Python

#### Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

#### Reflection Questions

### 1. **Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

   **Answer:** 
   - **Enhanced Interactivity:** IPython Shell offers an enhanced interactive environment compared to the default Python shell, making it easier to experiment and test code snippets.
   - **Advanced Features:** IPython includes advanced features like tab completion, syntax highlighting, and magic commands that streamline workflow and increase productivity.
   - **Better Debugging:** It provides better debugging tools with detailed tracebacks, which help in identifying and fixing errors quickly.
   - **Rich Display Capabilities:** IPython can handle rich media like images, videos, and even interactive visualizations, which are beneficial for data analysis and scientific computing.
   - **Integrated Documentation:** IPython allows easy access to documentation and help for functions and modules using commands like `?` and `??`.

### 2. **Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

   | Data type   | Definition                                                                 | Scalar or Non-Scalar |
   |-------------|---------------------------------------------------------------------------|----------------------|
   | **int**     | Represents whole numbers, e.g., 1, 2, 3                                  | Scalar               |
   | **String**   | Charactes representing text, e.g., 'hello', 'world'                  | Non-Scalar               |
   | **list**    | Ordered, mutable collection of elements, e.g., [1, 2, 3]                  | Non-Scalar           |
   | **dict**    | Unordered collection of key-value pairs, e.g., {'name': 'Alice', 'age': 30}| Non-Scalar           |

### 3. **A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

   **Answer:** 
   Lists and tuples are both used to store collections of items in Python. The primary differences are:
   - **Mutability:** Lists are mutable, meaning their elements can be changed after they are created. Tuples are immutable, so once they are created, their elements cannot be changed.
   - **Syntax:** Lists are defined using square brackets, e.g., `[1, 2, 3]`, whereas tuples are defined using parentheses, e.g., `(1, 2, 3)`.
   - **Use Cases:** Lists are suitable for collections of items that may change, such as a list of tasks or items in a cart. Tuples are suitable for collections of items that should remain constant, such as the coordinates of a point or a record of data.

### 4. **In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

   **Answer:** 
   For the language-learning app, a dictionary would be the most suitable data structure to store the flashcards. Each flashcard can be represented as a dictionary with keys for the word, definition, and category. This allows easy access and modification of each flashcard's attributes. The structure provides flexibility for future extensions, such as adding pronunciation, example sentences, or difficulty levels.

   **Example:**
   ```python
   flashcard = {
       'word': 'elucidate',
       'definition': 'make (something) clear; explain',
       'category': 'verb'
   }

   flashcards = [
       {
           'word': 'elucidate',
           'definition': 'make (something) clear; explain',
           'category': 'verb'
       },
       {
           'word': 'gregarious',
           'definition': 'fond of company; sociable',
           'category': 'adjective'
       }
       
   ]

## Exercise 1.3: Functions and Other Operations in Python

### Learning Goals

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

### Reflection Questions

### 1. Travel App Script

In this exercise, you learned how to use `if-elif-else` statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an `if-elif-else` statement for the following situation:

- The script should ask the user where they want to travel.
- The user’s input should be checked for 3 different travel destinations that you define.
- If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
- If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”

Write your script here. (Hint: remember what you learned about indents!)

```python
def travel_app():
    destination = input("Where would you like to travel? ")

    if destination.lower() == "paris":
        print("Enjoy your stay in Paris!")
    elif destination.lower() == "tokyo":
        print("Enjoy your stay in Tokyo!")
    elif destination.lower() == "new york":
        print("Enjoy your stay in New York!")
    else:
        print("Oops, that destination is not currently available.")

travel_app()

```

### 2. Explaining Logical Operators in Python

Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.

Logical operators in Python are used to combine conditional statements. The main logical operators are:

- `and`: Returns True if both statements are true.
- `or`: Returns True if at least one of the statements is true.
- `not`: Reverses the result, returns False if the result is true.

For example:

```python
a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

```
### 3. What are functions in Python? When and why are they useful?
Functions in Python are reusable blocks of code that perform a specific task. They are defined using the def keyword followed by a function name and parentheses containing any parameters. Functions are useful because they help organize code, make it more readable, and allow for code reuse. They also make debugging easier and help in breaking down complex problems into simpler, manageable pieces.

### 4. Progress Towards Goals
In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

- Goal 1: Improve problem-solving skills: I've been practicing writing scripts and solving different coding problems, which has significantly improved my problem-solving abilities.

- Goal 2: Learn Python syntax and best practices: By completing exercises and writing functions, I’ve become more familiar with Python syntax and better at writing clean, efficient code.

- Goal 3: Build a project portfolio: I’ve started a few small projects, like a recipe app, and plan to expand them into a larger portfolio to showcase my skills.
  
## Exercise 1.4: File Handling in Python
Learning Goals
- Use files to store and retrieve data in Python

###  Reflection Questions


### 1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

- File storage is important in Python because it allows you to persist data between program executions. Without storing local files, any data generated or modified during a program's execution would be lost once the program terminates. This would make it impossible to maintain state or save progress, which is crucial for many applications such as databases, user settings, and logs.

### 2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?

- Pickles are a way to serialize and deserialize Python objects, allowing them to be saved to a file and later loaded back into a program. The pickle.dump() method is used to serialize an object and write it to a file. Pickles are useful in situations where you need to save complex data structures like dictionaries, lists, or custom objects to a file and retrieve them later in the same state. This is particularly useful for caching, saving machine learning models, or any scenario where you need to save the state of an object.

### 3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

- To find out which directory you’re currently in, you can use the os.getcwd() function from the os module. To change your current working directory, you can use the os.chdir(path) function, where path is the directory you want to switch to.

```python
import os

# Get current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Change current working directory
os.chdir('/path/to/new/directory')
print("Directory changed to:", os.getcwd())
```
### 4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

- To prevent the entire script from terminating due to an error, you can use a try-except block to catch and handle exceptions. This allows you to manage errors gracefully and continue executing the rest of the script.

```python
try:
    # Code that might raise an exception
    risky_code()
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
```
### 5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.

Reflection:

- How is it going? The course is going well, and I feel more confident in my Python skills.
Something I'm proud of: I'm proud of my ability to handle file operations and understand the pickling process.
- Something I'm struggling with: I sometimes struggle with debugging complex code and understanding error messages.
- What I need more practice with: I need more practice with exception handling and working with different file formats

## Exercise 1.5: Object-Oriented Programming in Python

Learning Goals
- Apply object-oriented programming concepts to your Recipe app
### Reflection Questions
### 1. In your own words, what is object-oriented programming? What are the benefits of OOP?

- Object-oriented programming (OOP) is a programming paradigm that organizes software design around objects, which can be thought of as instances of classes. Each object is capable of storing data (attributes) and performing actions (methods) related to that data. OOP allows for modeling real-world entities and interactions within a program by defining classes that serve as blueprints for creating objects.

The benefits of OOP include:

- Modularity: Code is organized into separate classes, making it easier to maintain and update.
Reusability: Once a class is defined, it can be reused to create multiple objects, reducing redundancy.
Abstraction: OOP allows for hiding the complex implementation details and exposing only the necessary components, simplifying interaction with the code.
Encapsulation: OOP enables bundling data with methods that operate on that data, protecting the internal state of objects from unintended interference.
Inheritance: It allows new classes to inherit properties and behavior from existing classes, promoting code reuse and a hierarchical class structure.
Polymorphism: It provides the ability to define methods in different classes with the same name, allowing them to be used interchangeably based on the object type.
### 2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

- In Python, a class is a blueprint for creating objects. A class defines attributes and methods that the created objects will have. An object, on the other hand, is an instance of a class, meaning it is a specific realization of the class with actual values assigned to its attributes.

Real-world example:
- Consider a Car as a class. The Car class might have attributes such as make, model, color, and year. It might also have methods such as start_engine(), stop_engine(), and drive(). An object is a specific car, like a Toyota Camry 2020 in Red. This object would have the make attribute set to "Toyota", model to "Camry", color to "Red", and year to "2020". The object can perform actions like starting the engine or driving, just as defined in the Car class.

```python
class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def start_engine(self):
        return "Engine started."

    def stop_engine(self):
        return "Engine stopped."

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", "Red", 2020)

# Accessing object methods
print(my_car.start_engine())  # Output: Engine started.
```

### 3. In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine.

Inheritance
- Inheritance is an OOP concept where a new class, known as a subclass, derives attributes and methods from an existing class, known as a superclass. This allows the subclass to inherit the behavior and characteristics of the superclass while also introducing new features or modifying existing ones. Inheritance promotes code reuse, as common functionality can be defined in a superclass and shared across multiple subclasses. For example, consider a superclass Animal with attributes like name and methods like speak(). A subclass Dog can inherit from Animal, automatically gaining the name attribute and speak() method, while also adding its unique method, such as fetch(). This hierarchical relationship simplifies code maintenance and enhances extensibility.

Polymorphism
- Polymorphism is an OOP concept that allows objects of different classes to be treated as objects of a common superclass. The key idea is that different classes can define methods with the same name, and the correct method will be called based on the object’s actual class at runtime. Polymorphism enables flexibility and makes code more generic and extensible. For instance, consider a method draw() that exists in both Circle and Square classes. Even though the method has the same name, the way each shape is drawn differs. Polymorphism allows the draw() method to be called on any object of type Shape (a common superclass), and the correct version of the method will execute, whether it's a Circle, Square, or any other shape.

Operator Overloading
- Operator overloading is a feature in OOP that allows predefined operators (like +, -, *, etc.) to have different meanings based on the context in which they are used. In Python, classes can overload operators by defining special methods (also known as magic methods) that begin with double underscores (__). 
  
- For example, the __add__ method can be defined within a class to customize how the + operator behaves when applied to objects of that class. This enables objects to be combined or compared in a way that is meaningful to their context. For example, in a Vector class, overloading the + operator allows two vector objects to be added together using v1 + v2, which might result in a new vector representing the sum of the two.

## Exercise 1.6: Connecting to Databases in Python
Learning Goals
- Create a MySQL database for your Recipe app
  
### Reflection Questions

### 1. What are databases and what are the advantages of using them?

Databases are organized collections of data that allow for efficient storage, retrieval, and management of information. The advantages of using databases include:

- Data Integrity: Ensures accuracy and consistency of data.
- Scalability: Can handle large volumes of data and concurrent users.
- Security: Provides mechanisms to protect data from unauthorized access.
- Data Management: Facilitates easy data manipulation and querying.
- Backup and Recovery: Supports data backup and recovery processes.
  
### 2. List 3 data types that can be used in MySQL and describe them briefly:

Data type	Definition
INT	A whole number without a decimal point. Used for storing integer values.
VARCHAR	A variable-length string. Used for storing text with a specified maximum length.
DATE	A date value in the format 'YYYY-MM-DD'. Used for storing date information.

### 3. In what situations would SQLite be a better choice than MySQL?

SQLite would be a better choice than MySQL in situations where:

- Lightweight Applications: The application requires a lightweight, serverless database.
- Embedded Systems: The database needs to be embedded within the application.
- Development and Testing: Quick setup and ease of use are needed for development and testing purposes.
- Single-User Applications: The application is intended for single-user or low-concurrency environments.

### 4. Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?

- Syntax: Python has a more readable and concise syntax compared to JavaScript.
- Use Cases: JavaScript is primarily used for web development (both frontend and backend with Node.js), while Python is versatile and used in web development, data science, machine learning, automation, and more.
- Libraries and Frameworks: Python has extensive libraries for data science and machine learning (e.g., Pandas, TensorFlow), whereas JavaScript has a rich ecosystem for web development (e.g., React, Angular).
- Performance: JavaScript is generally faster for web applications due to its asynchronous nature, while Python may be slower but is highly efficient for data processing tasks.

### 5. Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?

- Performance: Python can be slower than compiled languages like C++ or Java due to its interpreted nature.
- Mobile Development: Python is not as popular or well-supported for mobile app development compared to languages like Swift or Kotlin.
- Concurrency: Python's Global Interpreter Lock (GIL) can be a limitation for multi-threaded applications, affecting performance in CPU-bound tasks.
- Memory Consumption: Python can consume more memory compared to some other languages, which might be a concern for memory-constrained environments.

# Exercise 1.7: Finalizing Your Python Program

## Learning Goals
- Interact with a database using an object-relational mapper (ORM)
- Build your final command-line Recipe application

## Reflection Questions

### 1. What is an Object Relational Mapper and what are the advantages of using one?

An **Object Relational Mapper (ORM)** is a tool that allows developers to interact with a database using the object-oriented paradigm of their programming language, rather than writing raw SQL queries. 

**Advantages of using an ORM:**
- **Abstraction**: ORMs abstract away the complexity of SQL, allowing developers to perform database operations using the programming language they are comfortable with.
- **Maintainability**: Code is generally more maintainable and readable when using an ORM because it reduces the amount of SQL code scattered throughout the application.
- **Security**: ORMs often provide protection against SQL injection attacks by using parameterized queries.
- **Portability**: ORMs can make switching between different database systems easier, as the ORM handles differences in SQL dialects.

### 2. By this point, you’ve finished creating your Recipe app. How did it go? What’s something in the app that you did well with? If you were to start over, what’s something about your app that you would change or improve?

The creation of the Recipe app went smoothly overall. One aspect I did well with was the organization of the code and the implementation of functions that performed specific tasks, keeping the app modular and easy to maintain. 

If I were to start over, I would focus on improving the user experience by adding more input validation and error handling. Additionally, I would consider implementing a feature for categorizing recipes, which could help in better organizing and searching for recipes.

### 3. Imagine you’re at a job interview. You’re asked what experience you have creating an app using Python. Taking your work for this Achievement as an example, draft how you would respond to this question.

In my recent project, I developed a command-line Recipe application using Python and SQLAlchemy, an Object Relational Mapper (ORM). The app allows users to create, view, search, edit, and delete recipes stored in a MySQL database. I used SQLAlchemy to define models, manage database connections, and perform CRUD operations efficiently. Throughout the project, I focused on ensuring the app was user-friendly by implementing input validation and clear user prompts. This project helped me solidify my understanding of database interactions in Python, and I’m confident in my ability to build similar applications.

### 4. You’ve finished Achievement 1! Before moving on to Achievement 2, take a moment to reflect on your learning in the course so far: 

#### a. What went well during this Achievement? 
One thing that went well was my ability to integrate Python with a MySQL database using SQLAlchemy. I successfully implemented various functions to handle different user operations, which helped me understand the flow of data between the application and the database.

#### b. What’s something you’re proud of? 
I’m proud of how I structured the application and the clarity of the code. Additionally, the fact that I was able to implement a robust search function based on user-selected ingredients is something I take pride in.

#### c. What was the most challenging aspect of this Achievement? 
The most challenging aspect was ensuring that the application handled various edge cases, such as invalid user inputs and database errors. I had to spend extra time refining my error handling to ensure the app behaved correctly in all scenarios.

#### d. Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Python skills?
Yes, this Achievement met my expectations. It gave me hands-on experience with Python and databases, which boosted my confidence in applying these skills to real-world projects.

#### e. What’s something you want to keep in mind to help you do your best in Achievement 2?
I want to keep in mind the importance of planning and designing the application before diving into the code. A well-thought-out plan can save time and prevent issues later in the development process.
