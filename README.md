# community-blanket
A community blanket project for EMF 2024

## Deploying

### Django & Postgres database

Copy the `secret_variables_django.env.template` file to `secret_variables_django.env` and configure the environment variables (see [Media files](media-files) for S3 config).

Create a username and password for the Postgres database and add them to files `secret_postgres_user.txt` and `secret_postgres_password.txt`

Deploy the Django app and Postgres with

```bash
docker compose up
```

On first run, log into the Django container and run `python manage.py collectstatic`. The static files are hosted locally (though `settings.py` does contain commented-out config to host them over S3 too).

### Media files

Two approaches: use S3 or don't use S3.

If using S3, set the following env variables according to your bucket & hosting provider (the provider does not have to be AWS but the variable names still have to have the `AWS_` prefix for the Django storage tooling to find them):
```
USE_S3=TRUE
AWS_ACCESS_KEY_ID='abc'
AWS_SECRET_ACCESS_KEY='def'
AWS_STORAGE_BUCKET_NAME='my-bucket-name'
AWS_URL='https://my-bucket-url.com'
AWS_DEFAULT_REGION='region-1'
```

If not using S3, set the following env variable:
```
USE_S3=FALSE
```
All the uploads will be hosted locally (nginx & django already have config to support this option)

### Nginx & SSL

The Nginx config template is in `blanket_site_nginx.conf`. Update the `server_name` with the actual domain.

Nginx is not included in the `docker-compose.yml` file. Instead it can be installed on the host itself:

```bash
apt install nginx
rm /etc/nginx/sites-enabled/default` # gets rid of the default nginx server (which clashes or takes priority otherwise)
cp -r nginx/sites-available/blanket_site_nginx.conf /etc/nginx/sites-available/blanket_site_nginx.conf`
ln -s /etc/nginx/sites-available/blanket_site_nginx.conf /etc/nginx/sites-enabled/blanket_site_nginx.conf`
service nginx reload
```

Use Certbot to get an SSL certificate: https://certbot.eff.org/instructions (or other means if you prefer). This can automatically update the Nginx config for you.

The reasons I set it up this way (not using Docker) are:
1. This allows the stack to run on a smaller VM because it avoids downloading & running a third Docker image
2. I don't understand nginx well and I got fed up trying to get it to work within a container
3. Less faff with creation & renewal of SSL certificates, I hope