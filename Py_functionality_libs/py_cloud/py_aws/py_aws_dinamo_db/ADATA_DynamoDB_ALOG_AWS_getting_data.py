import boto3
from boto3.dynamodb.conditions import Key


sts_client = boto3.client("sts")
table_name = "sn2-qa-audit-log-table"
# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::818714496271:role/CloudServicesDevAdminRole",
    RoleSessionName="clds-admin-role-local-session",
)


# printing assumed role CloudServicesDevAdminRole
print("The assumed role is {}".format(assumed_role_object))

# assigning secrets CloudServicesDevAdminRole
credentials = assumed_role_object["Credentials"]
aws_access_key_id = (credentials["AccessKeyId"],)
aws_secret_access_key = (["SecretAccessKey"],)
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

print("The table creation time is {}".format(table.creation_date_time))
# define attributes
attrs = table.attribute_definitions
print(attrs)

response = table.query(
    KeyConditionExpression=Key("tenant").eq("default-qatestenv")
    & Key("id").eq("157a63ab-ab8a-11ec-99b0-34cff61b3dba")
)
for x in response:
    print(x)
print("\nitem data example \n{}".format(response))
