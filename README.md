# CS 1XA3 Project03 - aroram15

## Usage
1. Install the conda environment using environment.yml provided to you in Project03 folder, where manage.py is located.
2. Login using testuser01 and test1234.
3. Run locally with - python manage.py runserver localhost:8000
4. Run on mac1xa3.ca with command - python manage.py runserver localhost:10004
  
  
## Objective 01
Description:
- This feature is displayed in something.djhtml which is rendered by
function def signup_view in Project03/login/views.py
- It makes a POST Request to from something.js to /e/aroram15/something_post
which is handled by someting_post_view
Exceptions:
- If the /e/aroram15/something_post is called without arguments is redirects
to login.djhtml
-If user input account registered already, signup page will be display continue.

## Objective 02
Description:
- This feature is displayed in social_base.djhtml renders the left_column used by messages.djhtml,people.djhtml and account.djhtml
- To display this feature, some code was inserted in def: messages_view , people_view and acount_view
Exceptions:
- If userprofile doesn’t be inputed , “unspecified” is be displaying in the position of data.

## Objective 03
Description:
- This feature is displayed in Project03/social/templates/account.djhtml 
Created forms for changing the user and password, and updating userinfo
Forms.py in project03/social
- when completed inputing, data is inserted into database by account_view
It makes a POST Request to from Form action to url ‘login:signup_view’	
which is handled by function ‘account_view’

Exceptions:
- password and user profile form was integrated in one form.

## Objective 04
Description:
- This feature is displayed in Project03/social/templates/people.djhtml
	People data was sent by people_view in views.py
- when click ‘more’ button, number of displaying person is increasing one by one.
Exceptions:
- after click more button, number of displaying person doesn’t decrease.
	For this user have to logout.

## Objective 05
Description:
- The right column of people.djhtml was displayed friend requests to the current user (currently only displays a single static fake friend request)
- To render actual friend requests, function people_view and template people.djhtml was changed.

## Objective 06
Description:
- This feature is displayed in people.djhtml.
When click accept or decline button, post request was sent by people.js’s acceptDeclineRequest to python function accept_decline_view.
By Prefix “A-“ and “D-“, defined accept and decline request.
Exceptions:
- By loading time, There is case that request has don’t sent with correct id.

## Objective 07
Description:
- This feature is displayed in message.djhtml render by 
– the function def messages_view in Project03/social/views.py 
– the template Project03/social/templates/messages.djhtml 
– the javascript code Project03/social/static/messages.js.

## Objective 08
Description:
- This feature was by serviced by post_submit_view
When the current user click the post button, at first check the input value in message.js
If the value of input is null, the alert appear.
If yea, the ajax for posts will go on the view.py and then insert value in the post table
After saving, send the result(success) to the message.js and then will reload.
-Changed post_submit_view to handle the post submission, by adding a new entry to the Post model
Exceptions:
If the value is null , show alert.

## Objective 09
Description:
- changed messages.djhtml to display real posts given by messages_view when rendering the template
At first, show the one post after getting posts order by post id
-more button is displaying number of posts could display.
When the more button click, send the ajax to the more_post_view in the view.py
In that, increments the value of session : displayed post count
      *(at first getting messase.view, check the session value above, if the session is not will send the one post and if the session exists, send the counts of display posts to the message.djhtml)
Finally, I used the session value for this problem based on the requirements
For this , python function more_post_view was changed and session variable was created in def.
Exceptions:
- if there is no post data, more button was inactived

## Objective 10
Description:
- For Liking post, used the ajax in message.js to connect to the like_view in view.py
 At first, when the rendering template, in the view.py, message_view check the current user’s likes. 
If the current user likes, add the Boolean value ture, If not, add the Boolean false.
In the template, checked the Boolean, and then disable or active like button.
-Like event: used the ajax, go to the like_view in the view.py, add  the likes fields of posts.
Exceptions:
- if the current user already likes this post, the liked button disable.
-warning: when the ajax success return, we reload the current page according to the requirements in doc.

## Objective 11
Description:
-as follow test accounts was created
Username password
TestUser test1234
testuser01 test1234
testuser02 test1234
testuser03 test1234
testuser04 test1234
testuser05 test1234
testuser06 test1234
testuser07 test1234

                
## References
    Lectures and Labs of the professor.
      
#### Credits
    Thanks to my TA's and professor for the help and support required to build this project.

