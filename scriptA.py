# Importation Boto3
import boto3

numberVm=input("Veuillez saisir le nombre de machine virtuelle souhaité ?")

ec2 = boto3.resource('ec2')
# Création du nombre de machine virutelle demandé :
try :
    ec2.create_instances(ImageId='ami-0a49b025fffbbdac6', MinCount=int(numberVm), MaxCount=int(numberVm), SecurityGroupIds=['sg-045de45c2834b1b04'], UserData='user-data', InstanceType='t2.micro')
except ValueError :
    print("Ta saisie n'est pas un nombre !")

# Récupération sous forme d'un dictionnaire des ID des VM en clé et des IPs publiques en valeur
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instancesDetails=dict()
for instance in instances:
    instancesDetails[instance.id]=instance.public_ip_address



