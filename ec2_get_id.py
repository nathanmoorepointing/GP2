import boto3    

ec2client = boto3.client('ec2')

response = ec2client.describe_instances()

instance_Results = []

for reservation in response["Reservations"]:

    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])
        print(instance["Tags"][0])
        #instance_Results.append(((instance["InstanceId"]),(instance["Tags"][0])))
        
        
try:
    if len(instance_Results) > 0:
        print ('There are ', len(instance_Results), ' Runnning instances')
    #else:
    #    print ('There are more than 0 running instances')
    else:
        raise NameError('There are more than 0 running instances')

except NameError:
    print('instance_Results is empty are you connected to the internet, awscli?')

    raise
    

