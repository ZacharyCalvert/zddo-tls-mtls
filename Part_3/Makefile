MAKEFLAGS += --always-make
TLS_HOST ?= demo.zachcalvert.com

gen-rca: clean-rca
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out rootCA.key
	openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.crt -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=ZDDO Demo Root CA"

gen-intermediate: clean-intermediate
	@# Generate the intermediate private key
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out intermediateCA.key

	@# Generate the Certificate Signing Request (CSR) for the intermediate key to be signed by the root certificate authority (RCA)
	openssl req -new -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=ZDDO Intermediate CA" -addext "keyUsage=critical,keyCertSign,cRLSign" -key intermediateCA.key -out intermediateCA.csr

gen-server-key:
	openssl req -new -newkey rsa:2048 -nodes -keyout server.key -extensions v3_req -out server.csr -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=${TLS_HOST}" -addext "subjectAltName=DNS:${TLS_HOST}"

rca-sign-intermediate:
	openssl x509 -req -in intermediateCA.csr -extfile root.cnf -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out intermediateCA.crt -days 365 -sha256

intermediate-sign-server:
	envsubst '$$TLS_HOST' < ext_parameterized.cnf > ext.cnf
	openssl x509 -req  -in server.csr -CA intermediateCA.crt -CAkey intermediateCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile ext.cnf

prepare-chain:
	cat server.crt intermediateCA.crt rootCA.crt > ssl-bundle.crt

build-certs: clean-certs gen-rca gen-intermediate rca-sign-intermediate gen-server-key intermediate-sign-server prepare-chain

stop:
	@docker stop tls-demo > /dev/null 2>&1 || true

build-image: stop
	envsubst '$$TLS_HOST' < nginx_parameterized.conf > nginx.conf
	docker build -t nginx-tls-rca-demo .

demo: clean build-certs build-image
	docker run --rm -d --name tls-demo -p 8080:80 -p 8443:443 nginx-tls-rca-demo

inspect-rca:
	openssl x509 -in rootCA.crt -text -noout

inspect-intermediate:
	openssl x509 -in intermediateCA.crt -text -noout

inspect-server:
	openssl x509 -in server.crt -text -noout

inspect: inspect-rca inspect-intermediate inspect-server

clean-rca:
	@rm rootCA.key > /dev/null 2>&1 || true
	@rm rootCA.crt > /dev/null 2>&1 || true
	@rm rootCA.srl > /dev/null 2>&1 || true

clean-intermediate:
	@rm intermediateCA.csr > /dev/null 2>&1 || true
	@rm intermediateCA.key > /dev/null 2>&1 || true
	@rm intermediateCA.crt > /dev/null 2>&1 || true
	@rm ext.cnf > /dev/null 2>&1 || true

clean-server:
	@rm server.key > /dev/null 2>&1 || true
	@rm server.csr > /dev/null 2>&1 || true
	@rm server.crt > /dev/null 2>&1 || true

clean-image: stop
	@rm nginx.conf > /dev/null 2>&1 || true

clean-certs: clean-rca clean-intermediate clean-server

clean: clean-image clean-certs
