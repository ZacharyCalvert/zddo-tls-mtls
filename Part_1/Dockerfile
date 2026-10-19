FROM nginx:alpine

# Create directory for local cert and key material
RUN mkdir -p /etc/nginx/ssl

# Custom zddo.zachcalvert.com conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy hello world index file
COPY index.html /usr/share/nginx/html/index.html

# Copy TLS certificates into the container
COPY certificate.crt /etc/nginx/ssl/certificate.crt
COPY private.key /etc/nginx/ssl/private.key

# Read only access for key and certificate
RUN chmod 400 /etc/nginx/ssl/certificate.crt
RUN chmod 400 /etc/nginx/ssl/private.key

# Expose both HTTP and HTTPS ports, 80 being a 301 redirect to 443
EXPOSE 80 443