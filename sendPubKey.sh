#!/bin/bash

#ansible-playbook -i hostlist/allinone-inventory pubkey.yml
# ansible-playbook -i hostlist/master-inventory pubkey.yml
ansible-playbook -i hostlist/vm01-inventory pubkey.yml
ansible-playbook -i hostlist/vm02-inventory pubkey.yml

