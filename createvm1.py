#!/usr/bin/env python
import requests

# first we have to import random module as this
# provides the backbone for our random string
# generator and then we have to import the string
# module.
#github commit done 12/12/2018
#Another develop branch
#develop branch created
#add feature1 to the code

import random
import string

# now lets see what this string module provide us.
# I wont be going into depth because the python
# documentation provides ample information.
# so lets generate a random string with 32 characters.
#random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

r = randomString()
print(r)

def randomNumber(stringLength=10):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
n = randomNumber()
print(n)

a=r+n

print(a)


headers = {
    'Content-Type': 'application/json',
}

data={"u_name":r,"u_serial_number":n,"u_asset_tag":a,"u_is_virtual":"true","u_model_id":"VMware Virtual Platform","u_device_classification":"General Purpose Server","u_device_type":"Virtual"}

response = requests.post('https://dev54376.service-now.com/api/now/import/u_td_cloud_test', headers=headers, json=data, auth=('ws.dps', 'abcd1234'))

print(response)
print(response.text)

