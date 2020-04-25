from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.core import serializers
from .models import UserInfo
from .forms import UserProfileForm
from .models import FriendRequest
from .models import Post
import json
from django.db.models import Q

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        user=request.user
        all_people = UserInfo.objects.filter(~Q(user=request.user))
        table_friend = FriendRequest.objects.filter(Q(from_user_id=user.id) | Q(to_user_id=user.id))
        all_friend=[]
        all_friend_many = UserInfo.objects.filter(user=request.user)
        for friend in all_friend_many:
            all_friend=friend.friends.all()                    
        serializers.serialize('json', all_friend)
        for interest in all_friend_many:
            interest = interest.interests.all()

        # print("dkdjfkd----interest:", serializers.serialize('json', interest))
        # interest = serializers.serialize('json', interest)
        total_post = Post.objects.all().count()     
        
        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        if( 'more_posts') in request.session:
            count_posts = request.session['more_posts']
            if count_posts > total_post:
                count_posts = total_post
            posts = Post.objects.order_by('-id')[:count_posts].prefetch_related('owner')
        else:
            count_posts  = 1
            posts = Post.objects.order_by('-id')[:1].prefetch_related('owner')

        for post in posts:
            post.already_liked = 0
            p_count = 0
            uu = post.likes.all()
            for u in uu:
                p_count=p_count+1
                if u==user_info:
                    post.already_liked=1
                    print('ok')
            post.post_counts = p_count

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post
        context = { 'user_info' : user_info
                  , 'posts' : posts
                  ,'rest_posts': total_post-count_posts
                  , 'all_friend' : all_friend
                  , 'interest' : interest}
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:
        
        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
        if 'employment' in request.POST:
            user=request.user
            label=models.Interest(label = request.POST['interest'])
            label.save()
            labelobject=models.Interest.objects.get(label=request.POST['interest'])
            user_info = models.UserInfo.objects.get(user=request.user)
            user_info.employment=request.POST['employment']
            user_info.birthday=request.POST['birthday']
            user_info.location=request.POST['location']
            user_info.interests.add(labelobject)
            
            user_info.save()
            
            user=models.User.objects.get(username=request.user)
            user.set_password(request.POST['new_password2'])
            user.save()             
            
            request.session['failed'] = True
            return redirect('login:login_view')
        else:
            form = PasswordChangeForm(request.POST)       
            profileUpdate_form = UserProfileForm(request.POST)
            user_info = models.UserInfo.objects.get(user=request.user)
            context = { 'user_info' : user_info,
                            'passwordChange_form' : form,
                            'profileUpdate_form' : profileUpdate_form }
            return render(request,'account.djhtml',context)
  

    

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user=request.user
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        count_display=1
        if ('more_view') in request.session:
            count_display = request.session.get('more_view')
        else:
            request.session['more_view']=1
        all_friend_many = UserInfo.objects.filter(user=request.user)
        for friend in all_friend_many:
            all_friend=friend.friends.all()
        for interest in all_friend_many:
            interest = interest.interests.all()
        # interest = serializers.serialize('json', interest)
        all_people_total = UserInfo.objects.filter(~Q(user=request.user))
        un_friendlist=[]  
        for person in all_people_total:
            define_friend=False
            if count_display == len(un_friendlist):
                break
            for friend in all_friend:
                if person.user_id == friend.user_id:
                    define_friend=True
            if define_friend==False:
                un_friendlist.append(person)
        request.session['more_view'] = len(un_friendlist)          
            
        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = []
        friend_requests_all = FriendRequest.objects.filter(to_user_id=user.id)
        print("friend_requests_all:",friend_requests_all)
        for friend in friend_requests_all:
            for person in all_people_total:                
                if person.user_id==friend.from_user_id:
                    friend_requests.append(person)                       
                    

        context = { 'user_info' : user_info,
                    'unfriend_list' : un_friendlist,
                    'friend_requests' : friend_requests,
                    'all_friend' : all_friend,
                    'interest' : interest,
                    }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = postIDReq
        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            user_info = models.UserInfo.objects.get(user=request.user)
            post = Post.objects.get(id=postID)
            post.likes.add(user_info)
            return HttpResponse('success')
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            post = Post(owner=user_info, content=postContent)
            post.save()

            # TODO Objective 8: Add a new entry to the Post model

            # return status='success'
            return HttpResponse(status=200)
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed
        if( 'more_posts') in request.session:
            request.session['more_posts'] = request.session.get('more_posts') + 1
        else:
            request.session['more_posts'] = 1

        # TODO Objective 9: update how many posts are displayed/returned by messages_view

        # return status='success'
        return HttpResponse(status=200)

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        # return status='success'
        if ('more_view') in request.session:
            request.session['more_view'] = request.session.get('more_view')+1
        else:
            request.session['more_view']=1

        return HttpResponse(status=200)

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    user = request.user  
    from_user_id = user.id 

    frID = request.POST
    username = frID['frID']
    if frID is not None:      
        # remove 'fr-' from frID   
        id_request = username[3:]       
        print("id:",id_request)
        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            to_request_list=FriendRequest.objects.filter(from_user_id=from_user_id, to_user_id=id_request)
            print("to_request_list---12:",to_request_list)
            try:
                print(to_request_list[0])
            except IndexError:
                p=FriendRequest(to_user_id=id_request,from_user_id=from_user_id)
                p.save()
            
            return HttpResponse(status=200)
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
        decision = data[0]
        id_request = data[2:]   
        print("decision:",decision)
        print("id_request:",id_request)    

        if request.user.is_authenticated:

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users
            
            if decision=="A":
                print("---12----")            
            #write for requester
                user=request.user
                mainid=user.id
                print("---12----") 
                request_friend = models.User.objects.get(username=id_request)
                print("---13----", request_friend) 
                requester_id=request_friend.id
                print("---14----", requester_id) 
                friend_request_detail=FriendRequest.objects.get(from_user_id=requester_id, to_user_id=mainid)
                print("---16----") 
                mainuserInfo=models.UserInfo.objects.get(user_id=mainid)
                print("---17----") 
                requestuserInfo=models.UserInfo.objects.get(user_id=requester_id)
                print("---18----") 
                FriendRequest.objects.filter(from_user_id=requester_id)
                print("---19----") 
                userinfo=UserInfo.objects.get(pk=requester_id)
                print("------20----")
                userinfo.friends.add(mainuserInfo)    
                friend_request_detail.delete()
            
            #write for user
                print("-----21---")
                mainuser=UserInfo.objects.get(user_id = mainid)
                mainuser.friends.add(requestuserInfo)
            elif decision=="D":
                request_friend = models.User.objects.get(username=id_request)
                FriendRequest.objects.filter(id=request_friend.id).delete()
            
            # FriendRequest.object.filter(from_user_id=pk_accept).delete()
            # return status='success'
            return HttpResponse(status=200)
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
