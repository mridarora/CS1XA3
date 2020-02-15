# CS 1XA3 Project 01 - **aroram15**
### 1. Usage
       1.1 Execute this scrip with:
           chmod +x CS1XA3/Project01/project_analyze.sh
           ./CS1XA3/Project01/project_analyze
       1.2 Don't include any arguements.
       1.3 The script will automatically prompt user to enter the feature he/she wants to implement
       
### 2. Feature 01
       2.1 **Description** : This feature will save the names of all the files in the directory 
                             which have *#FIXME* word in the last line of the file
       2.2 **Execution**   : This feature can be executed by entering 1. as the input argument as 
                             and when the user gets the prompt.
       2.3 **References**  : https://unix.stackexchange.com/questions/286544/how-to-extract-first-and-last-lines-in-a-file

### 3. Feature 02
       3.1 **Description** : This feature will extract the size of all the files in a given directory
                             and will display them in increasing order in a human readable form. Note that 
                             the file size will be displayed in bytes
       3.2 **Execution**   : This feature can be executed by entering 2. as the input argument as 
                             and when the user gets the prompt.
       3.3 **References**  : https://superuser.com/questions/90008/how-to-clear-the-contents-of-a-file-from-the-command-line
                             https://unix.stackexchange.com/questions/286544/how-to-extract-first-and-last-lines-in-a-file
                             https://www.geeksforgeeks.org/sort-command-linuxunix-examples/
                             
### 4. Feature 03
       4.1 **Description** : This feature will output the number of files in the directory with the extension endered 
                             by the user.
       4.2 **Execution**   : This feature can be executed by entering 3. as the first input when prompted to do so and                              
                             entering the extension of the file on the second attempt. 
                             
### 5. Custome Feature
       5.1 First custom feature will incorporate security feature in project_analyze.sh file. If the user enters the correct
           password, only then he/she will be allowed to execute the file. Also the user will have an option to change the 
           password.
       5.2 Second custom feature will sort the files in the repository according to the user input. For example if the user
           enters name then files will be arranged alphabetically.
       
###### ***Note*** All features will have statements giving user the instructions on the type of input the user can enter.
