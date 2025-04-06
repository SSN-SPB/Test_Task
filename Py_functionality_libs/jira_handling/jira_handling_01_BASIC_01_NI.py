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


if __name__ == "__main__":
    main()
