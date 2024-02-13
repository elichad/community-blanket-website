# Deployment notes

These notes are currently disorganised and a product of experimenting with the server locally. These will be cleaned up once the project is deployed to a live server.

- set MEDIA_ROOT and MEDIA_URL in Django settings
  - for MEDIA_ROOT, if using Django default file storage backend, must be a directory that the web server user has write access to
