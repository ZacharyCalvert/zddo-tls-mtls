.PHONY: self-signed clean stop build demo

export TLS_HOST ?= demo.zachcalvert.com

self-signed:
	openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -noenc -out certificate.crt -keyout private.key -subj "/C=US/ST=State/L=City/O=Org/CN=${TLS_HOST}" -addext "subjectAltName=DNS:${TLS_HOST}"

clean:
	@rm certificate.crt > /dev/null 2>&1 || true
	@rm private.key > /dev/null 2>&1  || true
	@docker stop tls-demo > /dev/null 2>&1  || true

stop:
	@docker stop tls-demo > /dev/null 2>&1 || true

build: stop
	envsubst '$$TLS_HOST' < nginx_parameterized.conf > nginx.conf
	docker build -t nginx-tls-demo .

demo: clean self-signed build
	docker run --rm -d --name tls-demo -p 8080:80 -p 8443:443 nginx-tls-demo
