### Project File Structure
1. Install Tkinter <br>
2. Importing Libraries<br>
3. Initializing test window and variables<br>
4. Function for making the text float on the top of the window<br>
5. Function for calculating time<br>
6. Game Function<br>
7. Defining labels<br>

### 1. Install Tkinter:
Tkinter is a standard graphical user interface library that is available for python. You need to install Tkinter to begin the project. 
Write the command given below to install Tkinter on your system.<br>
`pip install tkinter`

### 2. Importing Libraries:
`from words import words`<br>
`from tkinter import *`<br>
`import random` <br>
`from tkinter import messagebox`

### Code Explanation:

a. words: words is another file that contains a list of words that will be displayed on the screen.<br>
b. random: It helps in generating random strings and numbers.<br>
c. messagebox: It helps in displaying a message box on the screen.<br>

### 3. Initializing test window and variables:
![image](https://user-images.githubusercontent.com/61057666/147369763-25cfbb27-9407-4eb2-8d54-27abe4dd235f.png)

###  Code Explanation:

a. Tk(): It helps in initializing the tkinter module.<br>

b. geometry(): It defines the geometry of the typing test window.<br>

c. title(): It displays the title on the top of the typing test window.<br>

d. bg: It helps in applying the background color of the typing test window.<br>

e. Score: It is a variable that stores the score.<br>

f. Missed: This variable stores all the misspelled words entered by the user.<br>

g. time: This variable stores the time allotted to complete the test.<br>

### 4. Function for making the text float on the top of the window:
![image](https://user-images.githubusercontent.com/61057666/147369777-3ceb5352-a860-431a-8f34-7ac1c49ba9cc.png)

### Code Explanation:

a. movingtext(): This function will help the text to move on the top of the screen.<br>

b. floatingtext: This variable stores the text that needs to be floated.<br>

c. configure(): Overwriting over a label widget is performed by configure().<br>

d. after(): This method schedules an action after a timeout has elapsed.<br>
