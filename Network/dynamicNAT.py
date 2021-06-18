#usr/bin/python3

dev = {'dev-pc1':"10.0.0.1", 'dev-pc2':"10.0.0.2",'dev-pc3':"10.0.0.3"}
qa = {'qa-pc1':"10.0.1.1",'qa-pc2':"10.0.1.2",'qa-pc3': "10.0.1.3"}
sales = {'sales-pc1':"10.0.2.1",'sales-pc2':"10.0.2.2",'sales-pc3':"10.0.2.3"}
admin = {'admin-pc1':"10.0.3.1",'admin-pc2': "10.0.3.2", 'admin-pc3':"10.0.3.3"}
nat_pool = {"32.63.52.123":False, "132.63.121.25":False,"93.121.21.1":False,"10.42.237.235":False}


def get_pubip():
    for pub_ip in nat_pool:
        if nat_pool[pub_ip] == False:
                return pub_ip
        else:
            print("All addresses reserved")

def nat(host,destination_ip):
    if host in sales or host in admin:
        private_ip = host
        public_ip = get_pubip()
        nat_pool[public_ip] = True
        print("Internal host ", private_ip, "is translated to public_ip ",public_ip, " and forwared to",destination_ip)
    else:
        print("Access Denied !")



def main():
    host = input("Host>")
    if not host:
        exit()
    destination = input("Destination>") or "www.google.com"

    nat(host, destination)

try:
    while True:
        main()
except :
    print("Something went wrong\n")
