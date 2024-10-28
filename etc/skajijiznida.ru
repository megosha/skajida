server {
    server_name skajijiznida.ru;
    listen 80;

    location / {
        proxy_pass         http://127.0.0.1:8060/;
        proxy_redirect     off;

        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;

        client_max_body_size       10m;
        client_body_buffer_size    128k;

        proxy_connect_timeout      90;
        proxy_send_timeout         90;
        proxy_read_timeout         90;

        proxy_buffer_size          4k;
        proxy_buffers              4 32k;
        proxy_busy_buffers_size    64k;
        proxy_temp_file_write_size 64k;
    }

    location /static/ {
        root   /www/skajida_bf/;
    }

    location /assets/ {
        root   /www/skajida_bf/static/;
    }

    location /fonts/ {
        root   /www/skajida_bf/static/;
    }

    location /styles/ {
        root   /www/skajida_bf/static/;
    }

    location ~* ^.+\.(ico|json|xml|txt)$ {
        root   /www/skajida_bf/static/;
    }

    location /media/ {
        root   /www/skajida_bf/;
    }

    location /images/ {
        root   /www/skajijiznida.ru/public_html/;
    }
    location /js/ {
        root   /www/skajijiznida.ru/public_html/;
    }
    location /style/ {
        root   /www/skajijiznida.ru/public_html/;
    }

    location ~ /.well-known {
        root /var/www/html;
        allow all;
    }
}
