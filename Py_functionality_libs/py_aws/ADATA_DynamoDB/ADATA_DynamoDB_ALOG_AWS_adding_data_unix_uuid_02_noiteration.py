import boto3
from boto3.dynamodb.conditions import Key
import uuid
import time


sts_client = boto3.client('sts')
table_name = 'sn2-qa-audit-log-table'

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::818714496271:role/CloudServicesDevAdminRole",
    RoleSessionName="clds-admin-role-local-session"
)


# printing assumed role CloudServicesDevAdminRole
# print(assumed_role_object)

# assigning secrets CloudServicesDevAdminRole
credentials=assumed_role_object['Credentials']
aws_access_key_id=credentials['AccessKeyId'],
aws_secret_access_key=credentials['SecretAccessKey'],
aws_session_token=credentials['SessionToken'],
# print(aws_session_token)



# Get the service resource.
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=credentials['AccessKeyId'],
                          aws_secret_access_key=credentials['SecretAccessKey'],
                          aws_session_token=credentials['SessionToken'],)

# assigning table
table = dynamodb.Table(table_name)

# preparing data to send
string_uuidOne = str(uuid.uuid1())
current_unix_time = int(time.time())*1000
print('new item uuid: {}'.format(string_uuidOne))
response = table.put_item(
    Item = {'id': string_uuidOne,
            'tenant': 'default-qatestenv',
            'eventType': 'IP-Range-Added',
            'properties': {},
            'service': 'ADMIN_PORTAL',
            'message': 'Test filling message2',
            "messageTimestamp": current_unix_time,
            'tenantService': "default-qatestenv#ADMIN_PORTAL",
            'user': 'clds_test',
            'entityId': 'NULL',
            'cause': 'NULL'
        }
    )
