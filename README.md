# ***Quiz Web App***

Hello everyone, my name is **Ishita Bharadwaj** and I am from India. I have built a Quiz app as my final project for cs50 Web. I have made use of Django and JavaScript for building my project. 

A short video demonstrating my project can be found [here](https://www.youtube.com/watch?v=hbVRXIEa-x8)

#### ***Distinctiveness and Complexity:***
-	My web application is sufficiently distinct from the other projects in this course. It is neither a social network nor an e-commerce site. 
-	It utilizes Django on the back-end and JavaScript on the front-end.
-	It is mobile-responsive.


I have included the following specifications in my app. Let’s jump right in:

#### ***Home Page:***
   This is my main home page consisting of the instructions for the quiz along with a list of topics for the user to choose from. There is a small description with a link for taking the quiz on a particular topic. I have included Mathematics -1 and 2, Physics 1 and chemistry 1 as the topics for my quiz app.

#### ***Start:***
  On clicking on one of the quizzes, a modal box appears giving the user a description of the quiz. It specifies the difficulty, number of questions, score to pass and the time limit for the given quiz. Below that are 2 buttons, yes and no, asking the user if he/she wants to go to the quiz or go back home.

#### ***Specific Quiz:***
   Clicking on any one of the topic links on the home page and saying yes to the start modal takes the user to the quiz pertaining to that topic.  This page consists of the heading, the timer, go back button, quiz questions and submit button. The timer runs at the top right corner of the page. 

#### ***Results Page:***
   Clicking on the save button on the quiz form shows the user the results of the quiz (on the same page using JavaScript) where he/she can see his/her score along with a detailed review of the questions that were correct or incorrect (with the correct answer given) or not attempted. The green boxes show the questions answered correctly and the red boxes show the questions that were either incorrect or not attempted. If the user has scored above the passing marks, then a congratulations message is displayed below otherwise a sorry message is displayed.

#### ***Timer:***
 If while attempting the quiz the time expires before submitting the quiz then the quiz form gets submitted automatically and an alert is rendered saying “time over” and the user is then shown the results of his/her unfinished quiz. 

#### ***Apps:***
 I have 3 apps in my project namely: Questions, Quizes and Results. 

 > - The Questions app consists of 2 models: Answers and Questions. It is used for feeding in the questions and their respective answers into the database for each of the given topics. The Answers model keeps track of the questions, their right answers and the answers marked by user.

 > - The Quizes app consists of Quizes model that pertains to the specifications of the topics/domains in my quiz app. I have filled in the name of the quiz domain, the topic(concept) on which the quiz is based, the difficulty, time duration, score to pass, and number of questions to be displayed on the screen when the quiz topic is selected.

 > - The Results app consists of the Results model. This has the quiz field for the topic that the user was quizzed on, the user who took the quiz and the score the user got in that quiz.


#### ***Mobile Responsive:***
 My project is also mobile responsive, i.e., it can be easily viewed on a mobile phone also.

#### ***Requirements***: 
My project doesn’t need any extra requirements apart from django installation (`pip install django`) and needs to be run just like the previous cs50 web projects using the command:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`. 
I am using Django version- Django==3.2.3

> Be sure to create an admin account using the command: `python manage.py createsuperuser` so as to fill in the models with questions and answers for making your own quiz.


I have had an amazing experience working on cs50 Web and have learnt a whole lot in the field of web development. This course not only taught me how and what to code but also how to figure things out myself and fix any problems that come my way. I faced many issues regarding the working of my models and the interdependence of my apps to carry out the required function. The styling was slightly smoother thanks to bootstrap documentation from which I included modals and cards in my project. Overall, it was an enriching experience with lots of learning and even more of logical analysis. Thank You Harvard for this course!



I hope you like my project: The Quiz App 😊

##### ***Thank You!!***
