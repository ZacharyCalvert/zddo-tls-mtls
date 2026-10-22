MAKEFLAGS += --always-make
TLS_HOST ?= demo.zachcalvert.com

init:
	mkdir -p ./out/

gen-rca: init clean-rca
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out ./out/serverRCA.key
	openssl req -x509 -new -nodes -key ./out/serverRCA.key -sha256 -days 3650 -out ./out/serverRCA.crt -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=ZDDO Demo Root CA"

gen-intermediate: init clean-intermediate
	@# Generate the intermediate private key
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out ./out/intermediateCA.key

	@# Generate the Certificate Signing Request (CSR) for the intermediate key to be signed by the root certificate authority (RCA)
	openssl req -new -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=ZDDO Intermediate CA" -addext "keyUsage=critical,keyCertSign,cRLSign" -key ./out/intermediateCA.key -out ./out/intermediateCA.csr

gen-server-key: init
	openssl req -new -newkey rsa:2048 -nodes -keyout ./out/server.key -extensions v3_req -out ./out/server.csr -subj "/C=US/ST=Texas/L=Dallas/O=Zach Does DevOps/CN=${TLS_HOST}" -addext "subjectAltName=DNS:${TLS_HOST}"

rca-sign-intermediate: init
	openssl x509 -req -in ./out/intermediateCA.csr -extfile ./certs/root.cnf -CA ./out/serverRCA.crt -CAkey ./out/serverRCA.key -CAcreateserial -out ./out/intermediateCA.crt -days 365 -sha256

intermediate-sign-server: init
	envsubst '$$TLS_HOST' < ./certs/server_parameterized.cnf > ./out/server.cnf
	cd out && openssl x509 -req  -in server.csr -CA intermediateCA.crt -CAkey intermediateCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile server.cnf

gen-client: init clean-client
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out ./out/client.key

	@# Generate the Certificate Signing Request (CSR) for the client key to be signed by the root certificate authority (RCA)
	openssl req -new -key ./out/client.key -out ./out/client.csr -subj "/CN=ZDDO Client Cert"

prepare-chains:
	cat ./out/server.crt ./out/intermediateCA.crt ./out/serverRCA.crt > ./out/ssl-bundle.crt
	openssl pkcs12 -export -keypbe NONE -certpbe NONE -nomaciter -passout pass: -out ./out/client.pfx -inkey ./out/client.key -in ./out/client.crt -certfile ./out/serverRCA.crt

sign-client:
	openssl x509 -req -in ./out/client.csr -CA ./out/serverRCA.crt -CAkey ./out/serverRCA.key -CAcreateserial -days 365 -out ./out/client.crt -sha256 -extfile ./certs/client.cnf

build-certs: init clean-certs gen-rca gen-client gen-intermediate rca-sign-intermediate gen-server-key intermediate-sign-server sign-client prepare-chains 

stop:
	@docker stop tls-demo > /dev/null 2>&1 || true

build-image:
	envsubst '$$TLS_HOST' < nginx_parameterized.conf > nginx.conf
	docker build -t nginx-tls-rca-demo .

run-image: stop
	docker run --rm -d --name tls-demo -p 8080:80 -p 8443:443 nginx-tls-rca-demo

demo: clean build-certs build-image run-image

inspect-rca:
	openssl x509 -in serverRCA.crt -text -noout

inspect-intermediate:
	openssl x509 -in intermediateCA.crt -text -noout

inspect-server:
	openssl x509 -in server.crt -text -noout

inspect-client:
	openssl x509 -in server.crt -text -noout

clean-rca:
	@rm ./out/serverRCA.key > /dev/null 2>&1 || true
	@rm ./out/serverRCA.crt > /dev/null 2>&1 || true
	@rm ./out/serverRCA.srl > /dev/null 2>&1 || true

clean-client:
	@rm ./out/client.key > /dev/null 2>&1 || true
	@rm ./out/client.csr > /dev/null 2>&1 || true
	@rm ./out/client.crt > /dev/null 2>&1 || true
	@rm ./out/client.pfx > /dev/null 2>&1 || true

clean-intermediate:
	@rm ./out/intermediateCA.csr > /dev/null 2>&1 || true
	@rm ./out/intermediateCA.key > /dev/null 2>&1 || true
	@rm ./out/intermediateCA.crt > /dev/null 2>&1 || true
	@rm .out/intermediateCA.srl > /dev/null 2>&1 || true
	@rm ./out/ext.cnf > /dev/null 2>&1 || true

clean-server:
	@rm ./out/server.key > /dev/null 2>&1 || true
	@rm ./out/server.csr > /dev/null 2>&1 || true
	@rm ./out/server.crt > /dev/null 2>&1 || true

clean-image: stop
	@rm nginx.conf > /dev/null 2>&1 || true

clean-certs: clean-rca clean-client clean-intermediate clean-server

clean: clean-image clean-certs
	@rmdir out > /dev/null 2>&1 || true
