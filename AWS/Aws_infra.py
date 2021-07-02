#!usr/bin/python3

import boto3
import json
from boto.utils import get_instance_metadata

id = ''
key = ''
region = ''

SEP = '--------------------------------------------------------------------------------------------------------------------------------------'
VPCdetails = ["VpcId","CidrBlock","State","IsDefault","Tags"]
RTdetails = ["RouteTableId","VpcId","Associations","Tags","Routes"]
client = boto3.client('ec2',aws_access_key_id=id,aws_secret_access_key=key,region_name=region)
ec2 =  boto3.resource('ec2',aws_access_key_id=id,aws_secret_access_key=key,region_name=region)


class bcolors:
    H = '\033[95m'
    OB = '\033[94m'
    OC = '\033[96m'
    OG = '\033[92m'
    W = '\033[93m'
    F = '\033[91m'
    E = '\033[0m'
    B = '\033[1m'
    U = '\033[4m'

def getVPC():
	response = client.describe_vpcs()
	Vpcs = response.get('Vpcs')
	print(bcolors.U + SEP + bcolors.E)
	print(bcolors.OG + "[+] Found %s VPC" % len(Vpcs) + bcolors.E)
	print(bcolors.W + "[+] Ignoring Default VPC" + bcolors.E)
	for i in range(0,len(Vpcs)):
		VPC = dict()
		if not Vpcs[i]['IsDefault']:
			for d in VPCdetails:
				if (d == "Tags"):
					VPC.update({"Name":Vpcs[i][d][0]['Value']})
					continue
				VPC.update({d:Vpcs[i][d]})
			print(SEP)
			print(bcolors.OC + "\n\t[+] VPC:\n " +bcolors.E,json.dumps(VPC,indent=4))
			print(bcolors.OB + "\t\t[*] Routes:\n" +bcolors.E,json.dumps(getRoutes(VPC['VpcId']),indent=16))
#			print("\t\t[+] Subnets:", getSubnet(VPC['VpcId']))


def getRoutes(id):
	vpc = ec2.Vpc('id')
	route_tables = client.describe_route_tables()

	for r in range(len(route_tables)):
		routes = dict()
		for d in RTdetails:
			if (d == 'Associations'):
				subdetails = ['AssociationState','Main','SubnetId']
				for i in range(0,len(subdetails)-1):
					for s in subdetails:
						if s not in route_tables['RouteTables'][r][d][i].keys():
							continue
						routes.update({d:route_tables['RouteTables'][r][d][i][s]}) 
			elif (d == 'Routes'):
				subdetails =['DestinationCidrBlock','GatewayId','State']
				for i in range(0,len(subdetails)):
#					for s in subdetails:
					routes.update({d:route_tables['RouteTables'][r][d]})

			routes.update({d:route_tables['RouteTables'][r][d]})
		return routes


def getSubnet(id):
	vpc = ec2.Vpc('id')
	subnets = client.describe_subnets()
	sub = dict()
	details = ['CidrBlock','SubnetId','VpcId','Tags']
	for s in range(len(subnets['Subnets'])):
		if subnets['Subnets'][s]['VpcId'] == id:
			sub.update({"Subnet CIDR" : subnets['Subnets'][s]['CidrBlock'],"VPC ID": id,"Tags":subnets['Subnets'][s]['Tags'][0]['Value']})
	return sub

def main():
	getVPC()


main()
