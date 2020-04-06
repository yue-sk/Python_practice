current_users = ["john","jack","tom"]
new_users = ["Tom","jerry","red"]
for nu in new_users:
    if nu.lower() in  current_users:
        print("reject")
    else:
        print("pass")
