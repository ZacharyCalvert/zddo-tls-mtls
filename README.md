# TLS and mTLS Demonstration and Training Repository

This repo is a demonstration repository for showcasing how TLS and mutual TLS works.  It is a back-to-the-basics effort with documentation for providing a strong foundation for 12-factor application developers and web service engineers.  

# Part 1 - Self Signed TLS

Scripts within the [Part 1](./Part_1/) folder showcase creating your own private key, and using it for launching an nginx local webservice.  

To demonstrate locally: 

1. Set an environment variable value for TLS_HOST such as "local.example.com"
2. Run ```make demo```
3. Update your hosts file to resolve your TLS_HOST value to 127.0.0.1.  On Windows, this file must be edited in Administrator mode at ```C:\Windows\System32\drivers\etc\hosts```.  On Mac, this is at ```/etc/hosts```.  Create a new line in the file like ```127.0.0.1 local.example.com```
4. Open your browser to the TLS_HOST you specified, but at port 8443.  For example, if you used "local.example.com", that would be https://local.example.com:8443/

# Part 2 - TLS Signed by Root Certificate

Scripts within the [Part 2](./Part_2/) folder showcase generating a Root Certificate Authority (RCA), and using it for signing a server certificate, then launching a local nginx webservice with the certificate chain and server private key.

To demonstrate locally:

1. Set an environment variable value for TLS_HOST such as "local.example.com"
2. Run ```make demo```
3. Add the "rootCA.crt" as a trusted root certificate authority to your browser's certificate trusts.  If your browser is delegated to your local workstation, you'll need to add it to your local workstation's trusts.
4. Update your hosts file to resolve your TLS_HOST value to 127.0.0.1.  On Windows, this file must be edited in Administrator mode at ```C:\Windows\System32\drivers\etc\hosts```.  On Mac, this is at ```/etc/hosts```.  Create a new line in the file like ```127.0.0.1 local.example.com```
5. Open your browser to the TLS_HOST you specified, but at port 8443.  For example, if you used "local.example.com", that would be https://local.example.com:8443/

# Part 3 - TLS Signed by Intermediate Certificate

# Part 4 - Mutual TLS

# Part 5 - Manual Commands - CSR Extraction and Cert Inspection
