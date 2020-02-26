"""
    Bruno Salgado, February 2020
    This script contains an incomplete pass of unit tests for the retrieve github functions
"""

import retrieve_github
from unittest.mock import Mock, patch
import json


@patch('retrieve_github.retrieve_user')
def test_retrieve_github(mock_user_data):
    with open('mock_user_data.json') as json_file:
        mock_user_data = json.load(json_file)
    assert mock_user_data is not None
    assert retrieve_github.retrieve_repos(mock_user_data) is not None

@patch('retrieve_github.retrieve_repo_commits')
def test_retrieve_repo_commits(mock_repo_data):
    with open('mock_repo_data.json') as json_file:
        mock_repo_data = json.load(json_file)
        mock_repo_data.github_username = "bsalgado98"
    assert mock_repo_data is not None
    assert retrieve_github.retrieve_repo_commits(mock_repo_data.github_username) is not None
