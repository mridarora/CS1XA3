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

### 5. Feature 04
       5.1 **Description** : This feature will backup all the files with an extension of tmp and can also restore them as 
                             specified by user during the prompt.
       5.2 **Execution**   : This feature can be executed by entering 4. as the first input when prompted to do so and                              
                             again asks user either for backup or restore during the next prompt.
       5.3 **References**  : https://docstore.mik.ua/orelly/unix/upt/ch45_18.htm

### 6. Feature 05
       6.1 **Description** : This feature will do as per the assignment requirements.
       6.2 **Execution**   : This feature can be executed by entering 5. as the first input when prompted to do so.

### 7. Feature 06 ( Custom Feature )
       7.1 **Description** : User will be allowed to enter the file or is allowed to execute the file after the user 
                             enters the correct password for the file. User can also change the password.
                             Remember not to delete password file.
       7.2 **Execution**   : This feature can be executed by entering 6. as the first input when prompted to do so and
                             can easily follow along.

### 8. Feature 07 ( Custom Feature )
       8.1 **Description** : This feature allows user to sort his files alphabatically.
       8.2 **Execution**   : This feature can be executed by entering 7. as the first input when prompted to do so and
                             can easily follow along.
       8.3 **References**  : https://unix.stackexchange.com/questions/289228/sorting-files-using-a-bash-script
                             This site helped my a lot to achieve the final output of the feature.

### 9. Feature 08 ( Custom Feature )
       9.1 **Description** : This feature will do the exact same thing as required by the project.
       9.2 **Execution**   : This feature can be executed by entering 8. as the first input when prompted to do so and
                             can easily follow along.                             
###    Custome Feature
       1.  First custom feature will incorporate security feature in project_analyze.sh file. If the user enters the correct
           password, only then he/she will be allowed to execute the file. Also the user will have an option to change the 
           password.
       2.  Second custom feature will sort the files in the repository according to the user input. For example if the user
           enters name then files will be arranged alphabetically.
       
###### ***Note*** All features will have statements giving user the instructions on the type of input the user can enter.
