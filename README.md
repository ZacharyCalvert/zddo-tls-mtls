# TLS and mTLS Demonstration and Training Repository

This repo is a demonstration repository for showcasing how TLS and mutual TLS works.  It is a back-to-the-basics effort with documentation for providing a strong foundation for 12-factor application developers and web service engineers.  

The audience for this repository is developers and DevOps engineers looking to tinker at the lower levels of TLS certificate management, including self-signed certificates, signed certs from a generated root certificate authority, intermediate certificate authorities, and bi-directional trust using Mutual TLS.

TLS Provides:

- Confidentiality (Encryption) across the network between the client and the server
- Data integrity (ensures data cannot be forged from services across the network)
- Authentication (Identity) for the server you're connecting with
- Chain of trust (I trust authority A, A issued certificate B, B was presented by the server)
- Non-repudiation (can't deny the authenticity of the server)

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

Scripts within the [Part 3](./Part_3/) folder showcase generating a Root Certificate Authority (RCA), generating an Intermediate Certificate Authority (ICA), the RCA used to sign the ICA, and then the ICA sued to sign a server certificate.  Finally, the Makefile will launch a local nginx webservice with the certificate chain and server private key.

To demonstrate locally:

1. Set an environment variable value for TLS_HOST such as "local.example.com"
2. Run ```make demo```
3. Add the "rootCA.crt" as a trusted root certificate authority to your browser's certificate trusts.  If your browser is delegated to your local workstation, you'll need to add it to your local workstation's trusts.
4. Update your hosts file to resolve your TLS_HOST value to 127.0.0.1.  On Windows, this file must be edited in Administrator mode at ```C:\Windows\System32\drivers\etc\hosts```.  On Mac, this is at ```/etc/hosts```.  Create a new line in the file like ```127.0.0.1 local.example.com```
5. Open your browser to the TLS_HOST you specified, but at port 8443.  For example, if you used "local.example.com", that would be https://local.example.com:8443/

# Part 4 - Mutual TLS

The [Part 4](./Part_4/) folder showcase Mutual TLS (mTLS) whereby we take part 3 and expand the server (nginx) configuration to require the client to provide a certificate.  This is less common for workstations and browsers, and more for ensuring identity is bidirectional, the server provides a certificate indicating who they are and that they were signed by a trusted third party, and the client must provide a TLS certificate as well, also signed by a trusted third party.  

This pattern is found in zero trust environments, such as Kubernetes adopting Istio with services configured to require client authentication.

To demonstrate locally:

1. Set an environment variable value for TLS_HOST such as "local.example.com"
2. Run ```make demo```
3. Add the "rootCA.crt" as a trusted root certificate authority to your browser's certificate trusts.  If your browser is delegated to your local workstation, you'll need to add it to your local workstation's trusts.
4. Update your hosts file to resolve your TLS_HOST value to 127.0.0.1.  On Windows, this file must be edited in Administrator mode at ```C:\Windows\System32\drivers\etc\hosts```.  On Mac, this is at ```/etc/hosts```.  Create a new line in the file like ```127.0.0.1 local.example.com```
5. Load the "client.pfx" file in your browser's client certificates.  In firefox, this is in privacy and security settings.  It is browser specific, or even development language specific (Python vs Java vs .NET for example).
5. Open your browser to the TLS_HOST you specified, but at port 8443.  For example, if you used "local.example.com", that would be https://local.example.com:8443/

