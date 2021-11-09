import boto3

ec2 = boto3.resource('ec2')

# Récupération des ID des instaces running
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instancesId=[]
for instance in instances:
    instancesId.append(instance.id)

# Termine les instances running
ec2.instances.filter(InstanceIds=instancesId).terminate()