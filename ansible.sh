#!/usr/bin/env bash
 ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory ansible/site.yml  -v
