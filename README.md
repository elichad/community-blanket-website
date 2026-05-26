# community-blanket
A community blanket project for EMF 2024

## Deploying

Deploy the Django app and Postgres with

```bash
docker compose up
```

Nginx is not included in the `docker-compose.yml` file. Instead it can be installed on the host itself:

```bash
apt install nginx
rm /etc/nginx/sites-enabled/default` # gets rid of the default nginx server (which clashes or takes priority otherwise)
cp -r nginx/sites-available/blanket_site_nginx.conf /etc/nginx/sites-available/blanket_site_nginx.conf`
ln -s /etc/nginx/sites-available/blanket_site_nginx.conf /etc/nginx/sites-enabled/blanket_site_nginx.conf`
service nginx reload
```

The reasons I set it up this way are:
1. This allows the stack to run on a smaller VM because it avoids downloading a third docker image
2. I don't understand nginx well and I got fed up trying to get it to work within a container
3. Less faff with SSL certificates, I hope