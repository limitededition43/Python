#!usr/bin/python3

import boto3
import json

from boto.utils import get_instance_metadata
id=""
key=""

details = ["VpcId","CidrBlock","State","IsDefault","Tags"]
client = boto3.client('ec2',aws_access_key_id=id,aws_secret_access_key=key,region_name='us-east-1')
ec2=  boto3.resource('ec2',aws_access_key_id=id,aws_secret_access_key=key,region_name='us-east-1')

def getVPC():
	response = client.describe_vpcs()
	resp = response['Vpcs']
	print("Found %s VPC" % len(resp))
	print("Ignoring Default VPC")
	for i in range(len(resp)):
		VPC = dict()
		if not resp[i]['IsDefault']:
			for d in details:
				if not (d == "Tags"):
					VPC.update({d:resp[i][d]})
				VPC.update({"Name":resp[i][d]})

			print("\n\t[+] VPC: ",VPC)
			print("\t\t[+] Routes:", getRoutes(VPC['VpcId']))
			print("\t\t[+] Subnets:", getSubnet(VPC['VpcId']))


def getRoutes(id):
	vpc = ec2.Vpc('id')
	route_tables = client.describe_route_tables()
	routes = []
	for r in range(len(route_tables)):
		if route_tables['RouteTables'][r]['VpcId'] == id:
			routes.append(route_tables['RouteTables'][r]['Routes'][1])
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
