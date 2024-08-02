# Reflection Questions

1. What experiences have you had with coding and/or programming so far? What other experiences (programming-related or not) have you had that may help you as you progress through this course?

- I've completed the Full Stack Web Development Immersion which covers MERN & MEAN Stack. 
  
- Check out my portfolio at [sam-my.com](http://sam-my.com)

- I've been in the mortgage/banking industry for 15+ years and am working on a transition to tech.

- I've also had experience in call center tech support and customer service.

- My communication & troubleshooting skills helped me learned how to code methodically and be able to internalize this programming learning experience in a relatable & simple way. 

2. What do you know about Python already? What do you want to know?

- Not much outside that it is predominatly used in Machine Learning, Data Science & AI. 

3. What challenges do you think may come up while you take this course? What will help you face them? Think of specific spaces, people, and times of day or week that might be favorable to your facing challenges and growing. Plan for how to solve challenges that arise.

- I'm sure I'll get stuck with and troubleshoot just to find out something silly like I forgot to capitalize something or a trailing slash. 

- Knowing that I have a mentor that I can reach out to is comforting
- The internet, AI, checking forums, learning how to use the python version/techniques of console logging and debugging.   

# Exercise 1.1: Getting Started with Python 

1.	In your own words, what is the difference between frontend and backend web development? If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?

- Frontend is what the user sees visually on the web app: for example buttons, images, text, all the pages and forms etc. 

- Backend is when the user enters info or requests/retrieve data like clicking a button or submitting a form. 
   -  a. A process happens that either grabs info from the server or delivers info to the server handling it to update/store it in the database as necessary: API. For example, loading a picture of a movie poster when the user clicks on an icon or link. 
  
   - b. This involves a security system that handles the user logging in or registering where the user has to be verified: Authentication. 
  
   - c. Also a system is in place where user priveleges have been defined: Authorization.  

2.	Imagine you’re working as a full-stack developer in the near future. Your team is asking for your advice on whether to use JavaScript or Python for a project, and you think Python would be the better choice. How would you explain the similarities and differences between the two languages to your team? Drawing from what you learned in this Exercise, what reasons would you give to convince your team that Python is the better option? 
(Hint: refer to the Exercise section “The Benefits of Developing with Python”)

- Based on what I've learned in this course so far in exercise 1.1: 
  
- Python may be easier to read due to it's syntax resembling the natural English language which can make it easier to use and learn when having a team of newer developers or a team that wants to incorporate AI or Machine Learning in the project later down the road.  

3.	Now that you’ve had an introduction to Python, write down 3 goals you have for yourself and your learning during this Achievement. You can reflect on the following questions if it helps you. What do you want to learn about Python? What do you want to get out of this Achievement? Where or what do you see yourself working on after you complete this Achievement?

- I want to demonstrate that I'm versatile to be able to learn a new language outside of the MERN & MEAN stack that I already know. 

- I want to put in practice what the programming & troubleshooting techniques I've learned so far to picking up Python. 

- I want to position myself and use this as a stepping stone to better learn about AI and Machine Learning in the future.

### Exercise 1.2: Data Types in Python

#### Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

#### Reflection Questions

1. **Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

   **Answer:** 
   - **Enhanced Interactivity:** IPython Shell offers an enhanced interactive environment compared to the default Python shell, making it easier to experiment and test code snippets.
   - **Advanced Features:** IPython includes advanced features like tab completion, syntax highlighting, and magic commands that streamline workflow and increase productivity.
   - **Better Debugging:** It provides better debugging tools with detailed tracebacks, which help in identifying and fixing errors quickly.
   - **Rich Display Capabilities:** IPython can handle rich media like images, videos, and even interactive visualizations, which are beneficial for data analysis and scientific computing.
   - **Integrated Documentation:** IPython allows easy access to documentation and help for functions and modules using commands like `?` and `??`.

2. **Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

   | Data type   | Definition                                                                 | Scalar or Non-Scalar |
   |-------------|---------------------------------------------------------------------------|----------------------|
   | **int**     | Represents whole numbers, e.g., 1, 2, 3                                  | Scalar               |
   | **String**   | Charactes representing text, e.g., 'hello', 'world'                  | Non-Scalar               |
   | **list**    | Ordered, mutable collection of elements, e.g., [1, 2, 3]                  | Non-Scalar           |
   | **dict**    | Unordered collection of key-value pairs, e.g., {'name': 'Alice', 'age': 30}| Non-Scalar           |

3. **A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

   **Answer:** 
   Lists and tuples are both used to store collections of items in Python. The primary differences are:
   - **Mutability:** Lists are mutable, meaning their elements can be changed after they are created. Tuples are immutable, so once they are created, their elements cannot be changed.
   - **Syntax:** Lists are defined using square brackets, e.g., `[1, 2, 3]`, whereas tuples are defined using parentheses, e.g., `(1, 2, 3)`.
   - **Use Cases:** Lists are suitable for collections of items that may change, such as a list of tasks or items in a cart. Tuples are suitable for collections of items that should remain constant, such as the coordinates of a point or a record of data.

4. **In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

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

### Exercise 1.3: Functions and Other Operations in Python

## Learning Goals

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

## Reflection Questions

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
  
### Exercise 1.4: File Handling in Python
Learning Goals
- Use files to store and retrieve data in Python

###  Reflection Questions


1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

- File storage is important in Python because it allows you to persist data between program executions. Without storing local files, any data generated or modified during a program's execution would be lost once the program terminates. This would make it impossible to maintain state or save progress, which is crucial for many applications such as databases, user settings, and logs.

2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?

- Pickles are a way to serialize and deserialize Python objects, allowing them to be saved to a file and later loaded back into a program. The pickle.dump() method is used to serialize an object and write it to a file. Pickles are useful in situations where you need to save complex data structures like dictionaries, lists, or custom objects to a file and retrieve them later in the same state. This is particularly useful for caching, saving machine learning models, or any scenario where you need to save the state of an object.

3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

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
4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

- To prevent the entire script from terminating due to an error, you can use a try-except block to catch and handle exceptions. This allows you to manage errors gracefully and continue executing the rest of the script.

```python
try:
    # Code that might raise an exception
    risky_code()
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {e}")
```
5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.

Reflection:

- How is it going? The course is going well, and I feel more confident in my Python skills.
Something I'm proud of: I'm proud of my ability to handle file operations and understand the pickling process.
- Something I'm struggling with: I sometimes struggle with debugging complex code and understanding error messages.
- What I need more practice with: I need more practice with exception handling and working with different file formats