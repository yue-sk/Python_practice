import requests

#执行API并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
r = requests.get(url)
print("status code:", r.status_code)



#将API响应存储再一个变量中
response_dict = r.json()
print("total_count:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("repoteturn:",len(repo_dicts))

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nkeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

#循环所有仓库
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])     
    print('Repository:', repo_dict['html_url'])   
    print('Description:', repo_dict['description'])

#处理结果
print(response_dict.keys())

