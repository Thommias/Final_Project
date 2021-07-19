#!python
import netmiko
from netmiko import ConnectHandler
a = 'yes'
cisconexus = {
                'device_type': 'cisco_nxos',
                'ip': '192.168.150.46',
                'username': 'admin',
                'password': 'cisco',
            }
def configuration_access(port,typ,vlan):
    switching_commands = ['int ' + port,'no shut','switchport','switchport mode ' + typ, "switchport " + typ + ' vlan ' + vlan]
    config = net_connect.send_config_set(switching_commands)
    print('\n'  + '#'*135 + '\n' + config + '\n'  + '#'*135)


def configuration_trunk(port,typ):
    switching_commands = ['int ' + port,'no shut','switchport','switchport mode ' + typ]
    config = net_connect.send_config_set(switching_commands)
    print('\n'  + '#'*135 + '\n' + config + '\n'  + '#'*135)

def post_check(port):
    status = net_connect.send_command("show int " + port + " status")
    print(status)

###########################################################################################################################
###########################################################################################################################

net_connect = ConnectHandler(**cisconexus)
print('You are connected to the #SW')


# y = y.split()
# print(len(y))
# print(y.index('Eth1/60'))
# x = y.index('Eth1/60')
# z = y[x:x+7]
# print(z[0] +"  "+ z[1] +"  "+ z[2] +"  "+ z[3] +"  "+ z[4] +"  "+ z[5] +"  "+ z[6])
# print(z[3])



while a != 'no':
    print(' DO YOU WANT TO START?: write yes|no')
    a = input()
    status = net_connect.send_command('show int status')
    split_status = status.split()


    if a == 'yes':
        b = input('Which port do you want to check? for example [Eth1/30] :: ')
        answer = split_status.index(b)
        x = split_status[answer:answer+7]
#       print(x[0] +"  "+ x[1] +"  "+ x[2] +"  "+ x[3] +"  "+ x[4] +"  "+ x[5] +"  "+ x[6])        
     
        if x[3] == "trunk":
            print(x[0] + " is trunk")

        elif x[3] == "routed":
            print(x[0] + " is not configured")
        
        else:
            print(x[0] + " is acces")

        b = input('Do you want to check vlan on this port? write: yes|no ')

        if b == "yes":
            print(x[0] + " is in Vlan " + x[3])
            b = input('Do you want to configure this port? write: yes|no ')

            if b == "yes":
                b = input("Which vlan do you want to configure on " + x[0] + "? : ")
                configuration_access(x[0],"access",b)
                post_check(x[0])
            
            else:
                print("")

        else:
            print("")
        
        
    else:
        print("THANKS BYE BYE")


