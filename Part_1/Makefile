.PHONY: gen-self-signed

self-signed:
	openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -noenc -out certificate.crt -keyout private.key -subj "/C=US/ST=State/L=City/O=Org/CN=zddo.zachcalvert.com" -addext "subjectAltName=DNS:demo.zachcalvert.com,DNS:local.zachcalvert.com"

clean:
	@rm certificate.crt || true
	@rm private.key || true
	@docker stop zddo-tls || true

stop:
	@docker stop zddo-tls || true

build: stop
	@echo "hello world" > index.html
	docker build -t nginx-tls-demo .

demo: clean self-signed build
	docker run --rm -d --name zddo-tls -p 8080:80 -p 8443:443 nginx-tls-demo
