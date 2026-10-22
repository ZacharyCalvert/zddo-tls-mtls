import os
import requests

cert_config = ('./out/client.crt', './out/client.key')
ca_verify = './out/serverRCA.crt'

host = os.environ.get('TLS_HOST')

# Send the GET request
response = requests.get(f'https://{host}:8443/index.html', cert=cert_config, verify=ca_verify)
response.raise_for_status()

print(response.text)