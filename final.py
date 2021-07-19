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
def write_to_data():
    status = net_connect.send_command('show int status')
    with open('data.txt', 'w') as data:
        data.write(status)

def read_data():
    with open('data.txt', 'r') as data:
        data.seek(text)
        data_content = data.readline()
        print("Your port has this configuration: \n" + data_content)

def configuration_access(port,typ,vlan):
    switching_commands = ['int ' + port,'no shut','switchport','switchport mode ' + typ, "switchport " + typ + ' vlan ' + vlan]
    config = net_connect.send_config_set(switching_commands)
    print('\n'  + '#'*135 + '\n' + config + '\n'  + '#'*135)


def configuration_trunk(port,typ):
    switching_commands = ['int ' + port,'no shut','switchport','switchport mode ' + typ]
    config = net_connect.send_config_set(switching_commands)
    print('\n'  + '#'*135 + '\n' + config + '\n'  + '#'*135)


###########################################################################################################################
###########################################################################################################################

net_connect = ConnectHandler(**cisconexus)
print('You are connected to the #SW')
status = net_connect.send_command('show int status')
print(status)
while a != 'no':
    print(' DO YOU WANT TO CONFIGURE PORT?: write yes|no')
    a = input()

    
    if a == 'yes':
        write_to_data()

        print('\n\nWhich port do you want configure? [for example: Eth1/x]?: ')
        port = input()
        text = (status.find(port))

        read_data()

        print('\n\nDo you want trunk or access ?: ')
        typ = input()

        if typ == 'access':
            print('\n\nWhich vlan do you want [10,20,30]?: ')
            vlan = input()
            configuration_access(port,typ,vlan)
            write_to_data()
            read_data()

        elif typ == 'trunk':
            configuration_trunk(port,typ)
            write_to_data()
            read_data()

    elif a == 'no':
        print('                    End of configuration, thanks')















