FROM nginx
COPY index.html /usr/share/nginx/html
COPY dependencies /usr/share/nginx/html