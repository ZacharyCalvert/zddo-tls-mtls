MAKEFLAGS += --always-make
TLS_HOST ?= demo.zachcalvert.com

clean-rca:
	@rm rootCA.key > /dev/null 2>&1 || true
	@rm rootCA.crt > /dev/null 2>&1 || true
	@rm rootCA.srl > /dev/null 2>&1 || true
	@rm ext.cnf > /dev/null 2>&1 || true

inspect-rca:
	openssl x509 -in rootCA.crt -text -noout

inspect-server:
	openssl x509 -in server.crt -text -noout

inspect: inspect-rca inspect-server

gen-rca: clean-rca
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out rootCA.key
	openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.crt -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -subj "/C=US/ST=Texas/L=Dallas/O=ZDDO Demonstration/CN=Demo CA"

clean-server:
	@rm server.key > /dev/null 2>&1 || true
	@rm server.csr > /dev/null 2>&1 || true
	@rm server.crt > /dev/null 2>&1 || true

gen-server-key:
	openssl req -new -newkey rsa:2048 -nodes -keyout server.key -extensions v3_req -out server.csr -subj "/C=US/ST=State/L=City/O=Org/CN=${TLS_HOST}" -addext "subjectAltName=DNS:${TLS_HOST}"

rca-sign:
	envsubst '$$TLS_HOST' < ext_parameterized.cnf > ext.cnf
	openssl x509 -req  -in server.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out server.crt -days 365 -sha256  -extfile ext.cnf

prepare-chain:
	cat server.crt rootCA.crt > ssl-bundle.crt

build-certs: clean-rca gen-rca clean-server gen-server-key rca-sign prepare-chain

stop:
	@docker stop tls-demo > /dev/null 2>&1 || true

build-image: stop
	envsubst '$$TLS_HOST' < nginx_parameterized.conf > nginx.conf
	docker build -t nginx-tls-rca-demo .

demo: build-certs build-image
	docker run --rm -d --name tls-demo -p 8080:80 -p 8443:443 nginx-tls-rca-demo

clean-image: stop
	@rm nginx.conf > /dev/null 2>&1 || true

clean: clean-image clean-rca clean-server
