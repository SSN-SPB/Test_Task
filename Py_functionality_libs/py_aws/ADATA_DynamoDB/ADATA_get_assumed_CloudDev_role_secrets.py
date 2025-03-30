import boto3

sts_client = boto3.client('sts')

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::818714496271:role/CloudServicesDevAdminRole",
    RoleSessionName="clds-admin-role-local-session"
)


print(assumed_role_object)


