import boto3
from boto3.dynamodb.conditions import Key
import uuid
import time
import datetime


sts_client = boto3.client("sts")
table_name = "sn2-qa-audit-log-table"
tenant_name = "default-qatestenv"
service_name = "ADMIN_PORTAL"
tenantService_string = tenant_name + "#" + service_name

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::818714496271:role/CloudServicesDevAdminRole",
    RoleSessionName="clds-admin-role-local-session",
)

# printing assumed role CloudServicesDevAdminRole
# print(assumed_role_object)

# assigning secrets CloudServicesDevAdminRole
credentials = assumed_role_object["Credentials"]
aws_access_key_id = (credentials["AccessKeyId"],)
aws_secret_access_key = (credentials["SecretAccessKey"],)
aws_session_token = (credentials["SessionToken"],)
# print(aws_session_token)


# Get the service resource.
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
)

# assigning table
table = dynamodb.Table(table_name)


def sending_message(y):
    # preparing data to send
    uuidOne = uuid.uuid1()
    string_uuidOne = str(uuid.uuid1())
    print("new message uuid: {}".format(string_uuidOne))
    # format unix time and ALOG message
    ts = time.time()
    current_unix_time = int(ts * 1000)
    actual_time = datetime.datetime.fromtimestamp(ts)
    formatted_time = actual_time.strftime("%Y_%m_%d_%H_%M_%S.%f")[:-3]
    text_for_message = "Test filling message " + formatted_time + " " + str(y)

    response = table.put_item(
        Item={
            "id": string_uuidOne,
            "tenant": tenant_name,
            "eventType": "IP-Range-Added",
            "properties": {},
            "service": service_name,
            "message": text_for_message,
            "messageTimestamp": current_unix_time,
            "tenantService": tenantService_string,
            "user": "clds_test",
            "entityId": "NULL",
            "cause": "NULL",
        }
    )


def main():
    for i in range(5):
        sending_message(i)


if __name__ == "__main__":
    main()
