#!/usr/bin/env python

import json

x = {
            'group': {
                'hosts': ['51.68.28.198' ],
                'vars': {
                    'ansible_ssh_user': 'centos',
                    'ansible_ssh_private_key_file':
                        '~/.ssh/id_rsa',
                    'example_variable': 'value'
                }
            },
            '_meta': {
                'hostvars': {
                    '51.68.28.198': {
                        'host_specific_var': 'centos'
                    }
                }
            }
        }

print (json.dumps(x));

