'''
    Bruno Salgado, February 2020
    This script contains functions that gets a user's Github username and lists out all the user's repositories along
    with the number of commits per repo.
'''

import requests


def retrieve_user(user_name):
    response = requests.get(f'https://api.github.com/users/{user_name}/repos')
    return response.json()

def retrieve_repos(json):
    repos = []
    for obj in json:
        repos.append(obj['name'])
    return repos

def retrieve_repo_commits(user_name, repo):
    response = requests.get(f'https://api.github.com/repos/{user_name}/{repo}/commits')
    return len(response.json())

def construct_repo_commits_object(user_name):
    user_json = retrieve_user(user_name)
    user_repos = retrieve_repos(user_json)
    repo_commits = {}
    for repo in user_repos:
        repo_commits[repo] = retrieve_repo_commits(user_name, repo)
    return repo_commits

def print_repo_commits(repo_commits):
    for repo, commit_count in repo_commits.items():
        print(f'Repo {repo} has {commit_count} commits.')