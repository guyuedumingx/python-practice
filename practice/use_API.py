import requests

#执行API调用并存储在一个变量中
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories ",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName: ',repo_dict['name'])
    print('Owner: ',repo_dict['owner']['login'])
    print('Star: ',repo_dict['stargazers_count'])
    print('Repository: ',repo_dict['html_url'])
    print('Description: ',repo_dict['description'])






"""
#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print('Name:',repo_dict['name'])
"""