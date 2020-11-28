from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def labeveryday(task):
    task.run(task=netmiko_send_command, name="LAB EVERYDAY!!", command_string="show ip int brief")

results = nr.run(task=labeveryday)
print_result(results)
