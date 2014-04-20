Dyn Inc, Integration Team Deliverable
"Copyright © 2013, Dyn Inc.
All rights reserved.
 
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
 
* Redistribution of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
 
* Redistribution in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
 
* Neither the name of Dynamic Network Services, Inc. nor the names of
  its contributors may be used to endorse or promote products derived
  from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."

--------------------------------------------------------------------------

This is a simple Python wrapper for interacting with the Dynect Managed DNS
REST API.  

As it makes use of a JSON interface, one must either have the simplejson
module installed, or have Python 2.6/2.7 which have a JSON library that comes
with the language.

Use is fairly simple:

```python
import sys
from dynect.DynectDNS import DynectRest

rest_iface = DynectRest()

# Log in
arguments = {
	'customer_name': 'my_cust',
	'user_name': 'my_user',  
	'password': 'my_pass',
}
response = rest_iface.execute('/Session/', 'POST', arguments)

if response['status'] != 'success':
	sys.exit("Incorrect credentials")

# Perform action
response = rest_iface.execute('/Zone/', 'GET')
zone_resources = response['data']

# Log out, to be polite
rest_iface.execute('/Session/', 'DELETE')
```

Documentation on the REST resources can be found on the [DynECT Help site](https://help.dynect.net/dns-api-knowledge-base/)
