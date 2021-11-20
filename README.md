# Auto-File-Organizer
welcome to my first ever project in python programming and that is auto file organizer.so lets first discuss the problem and the problem  is we have a different file in a sample folder and  In this project we make a simple code which can help us to arrange all your different Files like audio file ,video file,pdf file,image file,zip file,etc inside the directory.

And this program is very useful if you don't like to arrange files manually. We have a python program to automate this task.

So let's begin

First we import os and glob.
Os module which operate with our operating system and 
We will use glob function of glob module to detect all files inside current directory
and now Creating a set of extension type inside the folder to avoid duplicate entries it will store all the extension file

And now we are going to insert a for loop 
For file in files_list    
For any type files that are present inside the files_list then it will enter into the loop.
And then the extension of that file is stored in extension and goes to the extension_set.
And this for loop keeps repeating itself till the all files extension is  stored in the extension set.

And now we define a function to create a directory for each type of extension named as createdirs(). It will make different folders based on their extension.

And then we define our next  function to move files based on their extension to the respective folder named as arrange(). 
After that we call the function createdirs() and arrange().

And that’s it. Our program is done . let’s run it …
Our program is run successfully .  Let's see the result. Ooo, our code is working.

So, that’s it  
Thanks for watching. 
