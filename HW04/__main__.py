'''
    Bruno Salgado, February 2020
    This is the main script that calls the retrieve github script's functions.
'''

import retrieve_github

if __name__ == "__main__":
    user_name = input("Enter your username: ")
    repo_commits_object = retrieve_github.construct_repo_commits_object(user_name)
    retrieve_github.print_repo_commits(repo_commits_object)

