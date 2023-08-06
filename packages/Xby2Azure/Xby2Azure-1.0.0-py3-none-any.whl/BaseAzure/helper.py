import json
import os

def help():
    print('''Steps for getting started:
* Install this package
* Run xby2-init
* Activate virtual environment (created as a part of init script)
* Install requirements (pip install -r requirements.txt)
* Add resources to resources.json file
* Run pulumi up (using active AWS profile)
* Push to BitBucket repo (Coming Soon)

VPC:
Here are the fields you can customize in KWARGS and the (defaults):  
* availability_zones (2)  
* cidr_block:  
    * partial: 192.168.0.0/16  
    * full: 10.0.0.0/16 (default)  
    * else: 172.31.0.0/16
* private_subnets (1)  
* public_subnets (1)  
* nat_gateways:  
    * ONE_PER_AZ (default)  
    * SINGLE: one nat gateway total  
    * else/NONE: no nat gateways 
* private_cidr_mask (22)  
* public_cidr_mask (20)  
* resource_name (test-vpc)

Security Group:
Here are the fields you can customize in KWARGS and the (defaults):  
* protocol (tcp)  
* i_from_port (0)  
* i_to_port (65535)  
* e_from_port (0)  
* e_to_port (65535)  
* i_cidr (10.0.0.0/16)  
* e_cidr (10.0.0.0/16)  
* resource_name (test-sec-group)  

ELB:
Here are the fields you can customize in KWARGS and the (defaults):  
* resource_name (test-lb)

EC2:
Here are the fields you can customize in KWARGS and the (defaults):  
* resource_name (test-ec2)  
* instance_type (t3a.micro)

RDS:
Here are the fields you can customize in KWARGS and the (defaults):  
* rds_instance_class (db.t4g.micro)  
* allocated_storage (8)  
* engine (PostgreSQL)  
* password (password)  
* username (username)  
* resource_name (test-rds)

AMI:
Here are the fields you can customize in KWARGS and the (defaults):    
* most_recent (True)  
* owners (["amazon"])  
* filters ([{"name": "description", "values": ["Amazon Linux 2 *]}])

Adding Resources:
Keep the order of declaration in mind. For example, the VPC should likely be the first thing declared. When using the options above, the resource will use require a "module", which will refer to a file within the Xby2AWS folder, a "resource_name", which will be the name of one of our custom classes, "overrides", which will be a list of any parameters that we want changed from the default values, and two booleans: "req_vpc" and "req_ami". These will indicate whether a particular resource will need us to pass in a vpc or an ami, respectively. Additionally, we can create resources that we haven't customized. This will require a "module", which will probably begin with either "pulumi_aws." or "pulumi_awsx.", the "resource_name", which will be a class within said module, "overrides", which will consist of **all** of the parameters needed for this resource, and the aforementioned booleans. For example:  
```json
{
    "module": "BaseAWS.elb",
    "resource_name": "BaseELB",
    "overrides": {},
    "req_vpc": true,
    "req_ami": false
},
{
    "module": "pulumi_aws.s3",
    "resource_name": "Bucket",
    "overrides": {
        "resource_name": "the-bucket"
    },
    "req_vpc": false,
    "req_ami": false
}
```

Resource Booleans
| Resource | req_vpc | req_ami |
| --- | ----------- | --------- |
| BaseAMI | false | false |
| BaseVPC | false | false |
| BaseSecurityGroup | true | false |
| BaseEC2 | true | true | 
| BaseRDS | true | false | 
| BaseELB | true | false | 
| Bucket | false | false |''')

def init():

    os.system('pulumi new python')
    os.system('git init')
    json_string = "{\"resources\": [{}]}"
    with open('resources.json', 'w') as outfile:
        outfile.write(json_string)

    main = '''"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
import BaseAzure
import json
import traceback
import importlib

with open ("resources.json", "r") as deployfile:
    res = json.load(deployfile)

current_vn = None

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

for resource in res["resources"]:
    try:
        assert resource["module"].startswith("BaseAzure") or resource["module"].startswith("azure")
        module = importlib.import_module(resource["module"])
        resource_class = getattr(module, resource["resource_name"])

        if resource["req_vn"]:
            instance = resource_class(resource_group, current_vn, **resource["overrides"])
        else:
            instance = resource_class(resource_group, **resource["overrides"])

        # set current vn
        if resource["resource_name"] == "BaseVN":
            current_vn = instance

        # add roles to a list of roles
        roles = {}
        if resource["resource_name"] == "RoleDefinition":
            roles[resource["overrides"]["resource_name"]] = instance.id

        pulumi.export(resource["resource_name"], instance)

    except:
        traceback.print_exc()
        print(resource["module"])'''

    with open('__main__.py', 'w') as outfile:
        outfile.write(main)

    req = '''pulumi>=3.0.0,<4.0.0
pulumi-azure-native>=1.0.0,<2.0.0
pulumi-azure
Xby2Azure>=1.0.0'''

    with open('requirements.txt', 'w') as outfile:
        outfile.write(req)

    pipeline = '''image: python:3.10
# this is a look at what a CI/CD pipeline for this package might look like
# feel free to make changes but this should work out of the box, assuming you find a way to connect to AWS
# check out this link if you'd like to see how I went about doing that
# https://support.atlassian.com/bitbucket-cloud/docs/deploy-on-aws-using-bitbucket-pipelines-openid-connect/
pipelines:
  default:
    - step:
        oidc: true
        caches:
          - pip
        script:
          # aws
          - export AWS_REGION=us-east-2
          - export AWS_ROLE_ARN=arn:aws:iam::854000326664:role/BitBucketRole
          - export AWS_WEB_IDENTITY_TOKEN_FILE=$(pwd)/web-identity-token
          - echo $BITBUCKET_STEP_OIDC_TOKEN > $(pwd)/web-identity-token
          # pulumi
          - curl -fsSL https://get.pulumi.com/ | sh
          - export PATH=$PATH:$HOME/.pulumi/bin
          - pulumi plugin install resource aws v5.4.0
          - pulumi stack select dev
          - pulumi up -y
          - pulumi destroy -y
          - pulumi stack export --file manifest.json'''

    # with open('bitbucket-pipelines.yml', 'w') as outfile:
    #     outfile.write(pipeline)
