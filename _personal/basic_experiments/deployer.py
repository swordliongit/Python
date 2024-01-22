#!/bin/python

import subprocess
from time import sleep

DB_NAME = ""
DOMAIN = ""
XMLRPC_PORT = ""
LPOLLING_PORT = ""

ODOO_VERSION = "odoo15"

conf_content = """
[options]
proxy_mode = True
; This is the password that allows database operations:
addons_path = /odoo/odoo15/odoo/odoo/addons,/odoo/odoo15/odoo/addons,/odoo/odoo15/odoo-custom-addons
admin_passwd = $pbkdf2-sha512$25000$q9X6XytlzFnLWQthjFGq1Q$zkSwXnry.DUBPo8ErAzBrp9GHoscc5HhZzI0TyZy1Armirfr0bviAlBBPhCe1hhaKOjVjAX6bkmMzLlVIBuKbQ
db_host = False
db_port = False
db_user = odoo
db_password = False
log_db = True
;workers = 2
;proxy_mode = true
;logrotate = True
;log_db_level = info
;log_handler = werkzeug:WARNING, :INFO
;log_level = info

"""


def create_conf():
    global conf_content
    conf_content = (
        conf_content
        + f"dbfilter = {DB_NAME}\n"
        + f"xmlrpc_port = {XMLRPC_PORT}\n"
        + f"longpolling_port = {LPOLLING_PORT}\n"
        + f"logfile = /var/log/odoo/{ODOO_VERSION}-{DB_NAME}.log"
    )

    with open(f'/etc/{ODOO_VERSION}-{DB_NAME}.conf', 'w') as f:
        f.write(conf_content)


def create_service():
    service_content = f"""
[Unit]
Description=Odoo15-{DB_NAME}
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo-{DB_NAME}
PermissionsStartOnly=true
User=odoo
Group=odoo
ExecStart=/odoo/odoo15/odoo-venv/bin/python3 /odoo/odoo15/odoo/odoo-bin -c /etc/{ODOO_VERSION}-{DB_NAME}.conf
StandardOutput=journal+console
        
[Install]
WantedBy=multi-user.target
"""
    with open(f"/etc/systemd/system/{ODOO_VERSION}-{DB_NAME}.service", 'w') as f:
        f.write(service_content)

    subprocess.run(['sudo', 'systemctl', 'enable', '--now', f'{ODOO_VERSION}-{DB_NAME}'])


def create_nginx():
    first_setup = f"""
server {{
    listen 80;
    server_name {DOMAIN};
    include snippets/letsencrypt.conf;
}}
"""

    with open(f"/etc/nginx/sites-available/{DOMAIN}", 'w') as f:
        f.write(first_setup)

    subprocess.run(['sudo', 'ln', '-s', f'/etc/nginx/sites-available/{DOMAIN}', '/etc/nginx/sites-enabled/'])
    subprocess.run(['nginx', '-t'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'])
    subprocess.run(
        [
            'sudo',
            'certbot',
            '--nginx',
            '--agree-tos',
            '--email',
            'info@autoronics.com',
            '--redirect',
            '--hsts',
            '-d',
            f'{DOMAIN}',
        ]
    )

    if "www" not in DOMAIN:
        nginx_conf = f"""
upstream odooserver{DB_NAME}{{
    server 127.0.0.1:{XMLRPC_PORT};
}}

upstream odoochat{DB_NAME}{{
    server 127.0.0.1:{LPOLLING_PORT};
}}

#HTTP -> HTTPS
server {{
    listen [::]:80;
    listen 80;
    server_name {DOMAIN};
    return 301 https://$host$request_uri;
}}

#HTTP -> HTTPS
server {{
    listen [::]:8081;
    listen 8081;
    server_name {DOMAIN};
    #return 301 http://{DOMAIN}$request_uri;
location / {{
	proxy_pass http://odooserver{DB_NAME};
	proxy_http_version 1.1;
	#add_header Content-Security-Policy upgrade-insecure-requests;
	proxy_set_header Upgrade $http_upgrade;
	proxy_set_header Connection 'upgrade';
	proxy_set_header Host $host;
	proxy_cache_bypass $http_upgrade;
	}}

}}

server {{
listen 443 ssl http2;
server_name {DOMAIN};

proxy_read_timeout 720s;
proxy_connect_timeout 720s;
proxy_send_timeout 720s;

# Proxy Headers
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
add_header Content-Security-Policy upgrade-insecure-requests;

#SSL CERTICATION
ssl_certificate /etc/letsencrypt/live/{DOMAIN}/fullchain.pem; # managed by Certbot
ssl_certificate_key /etc/letsencrypt/live/{DOMAIN}/privkey.pem; # managed by Certbot
ssl_trusted_certificate /etc/letsencrypt/live/{DOMAIN}/chain.pem;
include snippets/ssl.conf;
include snippets/letsencrypt.conf;

# log files
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;


# Specifies the maximum accepted body size of a client request,
# as indicated by the request header Content-Length.
client_max_body_size 200m;

# increase proxy buffer to handle some odoo web requests
proxy_buffers 16 64k;
proxy_buffer_size 128k;

# Handle long poll requests
location /longpolling {{
    proxy_pass http://odoochat{DB_NAME};
}}

# Handle / requests
location / {{
    proxy_redirect off;
    proxy_pass http://odooserver{DB_NAME};
}}

# Cache static files
location ~* /web/static/ {{
    proxy_cache_valid 200 90m;
    proxy_buffering off;
    expires 864000;
    proxy_pass http://odooserver{DB_NAME};
}}
# Gzip
gzip_types text/css text/less text/plain text/xml application/xml application/json application/javascript;
gzip on;

}}
"""
    else:
        domain_woutw = DOMAIN.lstrip("www.")
        nginx_conf = f"""
upstream odooserver{DB_NAME}{{
    server 127.0.0.1:{XMLRPC_PORT};
}}

upstream odoochat{DB_NAME}{{
    server 127.0.0.1:{LPOLLING_PORT};
}}

#HTTP -> HTTPS
server {{
    listen [::]:80;
    listen 80;
    server_name {domain_woutw} {DOMAIN};
    return 301 https://{DOMAIN}$request_uri;
}}

server {{
listen 443 ssl http2;
server_name {DOMAIN};

proxy_read_timeout 720s;
proxy_connect_timeout 720s;
proxy_send_timeout 720s;

# Proxy Headers
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
add_header Content-Security-Policy upgrade-insecure-requests;

#SSL CERTICATION
    ssl_certificate /etc/letsencrypt/live/{DOMAIN}/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/{DOMAIN}/privkey.pem; # managed by Certbot
ssl_trusted_certificate /etc/letsencrypt/live/{DOMAIN}/chain.pem;
include snippets/ssl.conf;
include snippets/letsencrypt.conf;

# log files
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;


# Specifies the maximum accepted body size of a client request,
# as indicated by the request header Content-Length.
client_max_body_size 200m;

# increase proxy buffer to handle some odoo web requests
proxy_buffers 16 64k;
proxy_buffer_size 128k;

# Handle long poll requests
location /longpolling {{
    proxy_pass http://odoochat{DB_NAME};
}}

# Handle / requests
location / {{
    proxy_redirect off;
    proxy_pass http://odooserver{DB_NAME};
}}

# Cache static files
location ~* /web/static/ {{
    proxy_cache_valid 200 90m;
    proxy_buffering off;
    expires 864000;
    proxy_pass http://odooserver{DB_NAME};
}}

# Gzip
gzip_types text/css text/less text/plain text/xml application/xml application/json application/javascript;
gzip on;
}}

server {{
listen 443 ssl http2;
server_name {domain_woutw};

proxy_read_timeout 720s;
proxy_connect_timeout 720s;
proxy_send_timeout 720s;

# Proxy Headers
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
add_header Content-Security-Policy upgrade-insecure-requests;

#SSL CERTICATION
    ssl_certificate /etc/letsencrypt/live/{domain_woutw}/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/{domain_woutw}/privkey.pem; # managed by Certbot
ssl_trusted_certificate /etc/letsencrypt/live/{domain_woutw}/chain.pem;
include snippets/ssl.conf;
include snippets/letsencrypt.conf;

# log files
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;


# Specifies the maximum accepted body size of a client request,
# as indicated by the request header Content-Length.
client_max_body_size 200m;

# increase proxy buffer to handle some odoo web requests
proxy_buffers 16 64k;
proxy_buffer_size 128k;

# Handle long poll requests
location /longpolling {{
    proxy_pass http://odoochat{DB_NAME};
}}

# Handle / requests
location / {{
    proxy_redirect off;
    proxy_pass http://odooserver{DB_NAME};
}}

# Cache static files
location ~* /web/static/ {{
    proxy_cache_valid 200 90m;
    proxy_buffering off;
    expires 864000;
    proxy_pass http://odooserver{DB_NAME};
}}
# Gzip
gzip_types text/css text/less text/plain text/xml application/xml application/json application/javascript;
gzip on;
}}

"""

    with open(f"/etc/nginx/sites-available/{DOMAIN}", 'w') as f:
        f.write(nginx_conf)

    subprocess.run(['sudo', 'systemctl', 'restart', f'{ODOO_VERSION}-{DB_NAME}'])
    subprocess.run(['nginx', '-t'])
    sleep(5)
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'])


if __name__ == "__main__":
    DB_NAME = input("Enter db name: ")
    XMLRPC_PORT = input("Enter XMLRPC Port: ")
    LPOLLING_PORT = input("Enter Longpolling Port: ")
    DOMAIN = input("Enter domain: ")

    create_conf()
    create_service()
    create_nginx()
