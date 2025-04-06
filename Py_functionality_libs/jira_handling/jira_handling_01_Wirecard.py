#!/usr/bin/pyton

import jira
from jira import JIRA
import os
import sys

target_of_file = "Jira treating"

jira_options = {"server": "https://wirecard-sg.atlassian.net/jira"}
USER = os.getenv("LOGON_VARIABLE_PROJECT_JIRA_LOGON")
PASSWORD = os.getenv("LOGON_VARIABLE_PROJECT_JIRA_PASSWORD")


def main():
    logon = USER
    print("The target of file: {}".format(target_of_file))
    print("logon: {}".format(logon))
    print("Password: {}".format(PASSWORD))
    ## jira = JIRA(options = jira_options, basic_auth=(USER, PASSWORD))
    ## failied with
    ## WARNING:root:Got recoverable error from
    ## GET https://wirecard-sg.atlassian.net/jira/rest/api/2/serverInfo,
    ## will retry [1/3] in 16.336353624573977s. Err: 401 Unauthorized
    ## need to be investigated


if __name__ == "__main__":
    main()
