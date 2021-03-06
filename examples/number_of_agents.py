#!/usr/bin/env python
__author__ = 'Jacolon Walker'
__email__ = 'jacolon.walker@collectivehealth.com'

import sentinelone
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

user = parser.get('creds', 'user')
passwd = parser.get('creds', 'passwd')
console = parser.get('endpoints', 'prod_domain')

# Init
client = sentinelone.SMgmt(user, passwd, console)
client.auth()

results = client.agents_count()

count = results['count']

print("There are %s registered endpoints" %(count))
