#import everything from tkinter
from tkinter import *
import time
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
#import json to use json file for data
import json



#Quiz Class
class Quiz:
    def __init__(self):
        self.q_no=0 
        # assigns ques to the display_question function to update later.
        self.display_question()
        # opt_selected holds an integer value which is used for selected option in a question.
        self.opt_selected=IntVar()
        # displaying radio button for the current question and used to display options for the current question
        self.opts=self.radio_buttons()
        # display options for the current question
        self.display_options()
        # displays the button for next and exit.
        self.buttons()
         
        # no of questions
        self.data_size=len(question)
         
        # counter of correct answers
        self.correct=0
 
 
    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):
         
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        labelimage = Label(gui,background = "#ffffff",border = 0)
        labelimage.pack(pady=(50,30))
        labelresulttext = Label(gui,font = ("Consolas",20),background = "#ffffff",)
        labelresulttext.pack()
        if score >= 20:
            img = PhotoImage(file="image/great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Are Excellent !!")
        elif (score >= 10 and score < 20):
            img = PhotoImage(file="image/ok.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Can Be Better !!")
        else:
            img = PhotoImage(file="image/bad.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Should Work Hard !!")
         
        # Shows a message box to display the result
        x = mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        return x
 
 
    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
         
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True
 
    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self):
         
        # Check if the answer is correct
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct += 1
         
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 
    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self):
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=5,bg="green",fg="white",font=("ariel",16,"bold"))
         
        # placing the button  on the screen
        next_button.place(x=1250,y=450)
         
        

        # img_exit = gui.PhotoImage(file=r"C:\Users\SHIVANI\Downloads\Quiz\b.jpg")
        # photoimage = img_exit.subsample(5, 200)
        # #startButton
        # quit_button = Button(gui,
        # image = photoimage,
        # text='c',
        # relief = FLAT,
        # border = 0,
        # width=5,
        #  compound = LEFT,
        # command = gui.destroy)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="#b30000", fg="white",font=("ariel",16," bold"))
         
        # placing the Quit button on the screen
        # quit_button.pack()
        quit_button.place(x=1250,y=40)
 
 
    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates each of the options for the current question of the radio button.
    def display_options(self):
        val=0
        # deselecting the options
        self.opt_selected.set(0)
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
 
    # This method shows the current Question on the screen
    def display_question(self): 

        # setting the Question properties
        q_no = Label(gui,background='white', text=question[self.q_no], width=60,font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        #placing the option on the screen
        q_no.place(x=70, y=150)
 

 
 
    # This method shows the radio buttons to select the Question on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        # initialize the list with an empty list of options
        q_list = []
        # position of the first option
        y_pos = 200
        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, background="white",text=" ",variable=self.opt_selected,value = len(q_list)+1,font = ("ariel",14))
        
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list

#intialization and assignment of counter
counter  = 20
hour =0
minute = 0
second= 0

#functionality after pressing start button
def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    question_view()
    count_down()
    







# Create a GUI Window
gui = Tk()
# set the size of the GUI Window
gui.geometry("2000x2000")
# set the title of the Window
gui.title("Python Quiz")
gui.configure(bg='white')
#TransparentImage
img1 = PhotoImage(file="image/transparentGradHat.png")

labelimage = Label(
    gui,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))


# The title to be shown
title = Label(gui, text="PYTHON QUIZ",width=80, bg="green",fg="white", font=("ariel", 20, "bold"))		
# place of the title
title.place(x=10, y=1)

#QuizStartLabel
labeltext = Label(
    gui,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="image/Frame.png")

#startButton
btnStart = Button(gui,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
	
)
btnStart.pack()
#RulesLabel
lblInstruction = Label(
    gui,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    gui,
    text = "This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()




with open('data.json') as f:
        data = json.load(f)

	# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
#to start quiz


def question_view():
 # create an object of the Quiz Class. 
    quiz = Quiz()
    return quiz
   

def count_down():
    # q1 = Quiz()
	 # Initital value of counter
    
    global counter, hour ,minute,second
    #updating value of min and sec from counter value
    mins,secs = divmod(counter,60)
    hours = 0
    #updating value of hour and minute from counter value
    if mins >60:
        hours, mins = divmod(mins, 60)
    hour= "{0:2d}".format(hours)
    minute = "{0:2d}".format(mins)
    second = "{0:2d}".format(secs)
    #checking value of counter
    if counter < 0:
        # question_view().display_result()
        mb.showinfo("Time Countdown", "Time's up ")
        return
    counter=counter-1 # decrease value by 1 

    l1.config(text=str(hour)+" :") # Update the hour label text using string
    l2.config(text=str(minute)+" :") # Update the minute label text using string
    l3.config(text=str(second)) # Update the second label text using string
    l3.after(1000,count_down) # time delay of 1000 milliseconds 
   
    

my_font=('times',20,'bold') # display size and style
l1=Label(gui,font=my_font,bg='white',width=2) # hour label
l1.place(x=1085,y=40) 
# la = Label(gui,text=":",width=1)
# la.place(x=1090,y=40)
l2=Label(gui,font=my_font,bg='white',width=2) # minute label
l2.place(x=1125,y=40)
l3=Label(gui,font=my_font,bg='white',width=2) #second label
l3.place(x=1165,y=40)


# Start the GUI
gui.mainloop()
