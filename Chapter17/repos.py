import requests
import pygal
from  pygal.style import  LightColorizedStyle as LCS ,LightenStyle as LS 

#执行API调用并存储响应
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("status code:",r.status_code)

#并将响应存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#探究有关仓库的信息
repo_dicts =response_dict['items']

names, stars = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_lengend=False)
chart.title = "Most-Starred Python Projects on GitLab"
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('repos.svg')
