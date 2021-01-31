import requests
import json
from collections import deque

def get_user_repos(username):
    request = requests.get('https://api.github.com/users/' + username + '/repos?sort=updated')
    my_json = request.json()
    
    user_repos = deque()

    for i in range(0, len(my_json)):
        repo_dict = {}
        repo_dict["name"] = my_json[i]["name"]
        repo_dict["description"] = my_json[i]["description"]
        repo_dict["url"] = my_json[i]["svn_url"]
        repo_dict["fork"] = my_json[i]["fork"]
        repo_dict["created"] = my_json[i]["created_at"]

        
        user_repos.append(repo_dict)
        repo_dict = {}

        # user_repos[my_json[i]['name']] = (my_json[i]['svn_url'], my_json[i]['description'])
    
    return list(user_repos)
