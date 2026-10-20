# TLS and mTLS Demonstration and Training Repository

This repo is a demonstration repository for showcasing how TLS and mutual TLS works.  It is a back-to-the-basics effort with documentation for providing a strong foundation for 12-factor application developers and web service engineers.  

# Part 1 - Self Signed TLS

Scripts within the [Part 1](./Part_1/) folder showcase creating your own private key, and using it for launching an nginx local webservice.  

To demonstrate locally: 

1. Set an environment variable value for TLS_HOST such as "local.example.com"
2. Run ```make demo```
3. Update your hosts file to resolve your TLS_HOST value to 127.0.0.1.  On Windows, this file must be edited in Administrator mode at ```C:\Windows\System32\drivers\etc\hosts```.  On Mac, this is at ```/etc/hosts```.  Create a new line in the file like ```127.0.0.1 local.example.com```
4. Open your browser to https://${TLS_HOST}:8443/index.html.  If you used "local.example.com", that would be https://local.example.com:8443/index.html

# Part 2 - TLS Signed by Root Certificate

# Part 3 - TLS with Intermediate Signature

# Part 4 - Mutual TLS

# Part 5 - Manual Commands - CSR Extraction and Cert Inspection
