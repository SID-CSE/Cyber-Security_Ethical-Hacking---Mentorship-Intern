import argparse
import nmap
import requests

def argument_parser():
    parser = argparse.ArgumentParser(description="TCP Port Scanner, will accept Hostname/IP Adress alonng with a list of ports to scan")
    parser.add_argument("-o","--host",nargs="?",help="Host IP Address")
    parser.add_argument("-p","--ports",nargs="?",help="Comma Seperated port List. Example: 22,80,443,8080'")
    var_args = vars(parser.parse_args())
    return var_args

def is_host_up(host_id):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, arguments="-sn")
    return nm_scan.all_hosts() and nm_scan[host_id].state() == "up"

def nmap_scan(host_id , port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id ,port_num) 
    print(nm_scan[host_id])
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    name = nm_scan[host_id]['tcp'][int(port_num)]['name']
    result = f"[*] {host} tcp/{port} {state} {name}"
    return result

if __name__=='__main__':
    try:
        users_args = argument_parser()
        host = users_args["host"]
        r = requests.get("http://"+host)
        if is_host_up(host):
            print(f"Host {host} is Live!")
        else:
            print(f"Host {host} is Non or unreachable.")

        if r.status_code:
            ports = users_args["ports"].split(",")
            for port in ports:
                print(port)
                print(nmap_scan(host, port.strip()))
        else:
            print("Machine not reachable")
    except AttributeError:
        print("Error in Input, Please provide the command_line arguments before running the script")
        