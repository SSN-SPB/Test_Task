#!/usr/bin/pyton

import jira
from jira import JIRA

import os


# suppress all warnings
import warnings

warnings.filterwarnings("ignore")

target_of_file = "Jira treating"


def main():
    # NI server:
    # jira_optionsNI = {'server': 'https://jira.network.ae/jira' , 'verify':False}
    # issue with SSL - SSL: CERTIFICATE_VERIFY_FAILED
    # ingored by 'verify':False
    # Remark: the warning is supressed. See above
    USER = os.getenv("LOGON_JIRA_NI")
    PASSWORD = os.getenv("LOGON_JIRA_NI_PASSWORD")
    print("used logon: {}".format(USER))
    print("used password: {}".format(PASSWORD))
    jira_optionsNI = {"server": "https://jira.network.ae/jira", "verify": False}
    jiraNI = JIRA(options=jira_optionsNI, basic_auth=(USER, PASSWORD))
    if jiraNI:
        print("Logon to Jira is successful")
    else:
        print("Logon to Jira is successful")
    query_duedate_past = """key in (MAF-4781, MAF-4785, MAF-4768)"""
    issue = jiraNI.issue("MAF-4768")
    print(issue)  # repsonse: MAF-4768
    print(issue.fields.project.key)  # 'MAF'
    print(issue.fields.issuetype.name)  # 'User Story'
    print(issue.fields.reporter.displayName)  # 'Pavel Pokrovskii'
    ##jql = 'project = ' + 'ADCBIUAT' + 'AND issuetype = ' + 'Test' + 'AND STATUS = ' + 'Automated'
    jql = (
        "project = "
        + "ADCBIUAT"
        + " AND issuetype = "
        + "Test"
        + " AND STATUS = "
        + "Automated"
    )

    # jql = 'project = ' + project_key + ' AND  worklogDate >= ' + work_date

    issues_list = jiraNI.search_issues(jql, startAt=0, maxResults=15)
    # print (issues_list)
    # response like: [<JIRA Issue: key='ADCBIUAT-12005', id='331527'>, ... , <JIRA Issue: key='ADCBIUAT-11918', id='331440'>]
    for i in issues_list:
        print(i)
        # response like:
        # ADCBIUAT-12005
        # ADCBIUAT-12004
        # ADCBIUAT-12001

        issue = jiraNI.issue(i)
        print(
            "type: {}, assigner: {}".format(
                issue.fields.issuetype.name, issue.fields.reporter.displayName
            )
        )


# response like:
# ADCBIUAT-11985
# type: Test, assigner: Sujay Sankar


if __name__ == "__main__":
    main()
