
# import account
# print(account.account_data['username'])

import instaloader

from account import account_data

L = instaloader.Instaloader()

# Login or load session
L.login(account_data['username'], account_data['password'])

# # Obtain profile metadata  
# profile = instaloader.Profile.from_username(L.context, account_data['username'])

# # Print list of followers
# follow_list = []
# count=0
# for follower in profile.get_followers():
#     print("Follower: ", follower)
#     follow_list.append(follower.username)
#     file = open("ddellagranna_followers.txt","a+")
#     file.write(follow_list[count])
#     file.write("\n")
#     file.close()
#     print(follow_list[count])
#     count=count+1
# follow_list.sort()
# print(follow_list)
# (likewise with profile.get_followers())
