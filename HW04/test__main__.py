'''
    Bruno Salgado, February 2020
    This script contains an incomplete pass of unit tests for the retrieve github functions
'''

import retrieve_github

def test_retrieve_github():
    assert retrieve_github.retrieve_user('bsalgado98') != None