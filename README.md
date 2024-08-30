# SETUP

## Create the Docker Image

```
docker compose build
```
When caches cause unexpected errors, use below
```
docker compose build --no-cache
```

## Run the container

```
docker compose up
```
Error occurs when web service tries to load db before db service get ready.
In that case, stop the current container with `Ctrl + C` and start again by `docker compose up`

Log would be like this:
```bash
❯ docker compose up --remove-orphans
[+] Running 2/0
 ✔ Container dialy-back-db-1   Created                                                                                                                                                                 0.0s 
 ✔ Container dialy-back-web-1  Created                                                                                                                                                                 0.0s 
Attaching to db-1, web-1
db-1   | 
db-1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
db-1   | 
db-1   | 2024-08-30 20:46:03.552 UTC [1] LOG:  starting PostgreSQL 16.4 (Debian 16.4-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
db-1   | 2024-08-30 20:46:03.552 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db-1   | 2024-08-30 20:46:03.552 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db-1   | 2024-08-30 20:46:03.560 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db-1   | 2024-08-30 20:46:03.571 UTC [28] LOG:  database system was shut down at 2024-08-30 20:45:57 UTC
db-1   | 2024-08-30 20:46:03.581 UTC [1] LOG:  database system is ready to accept connections
web-1  | Watching for file changes with StatReloader
web-1  | Performing system checks...
web-1  | 
web-1  | System check identified no issues (0 silenced).
web-1  |
web-1  | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
web-1  | Run 'python manage.py migrate' to apply them.
web-1  | August 30, 2024 - 20:46:04
web-1  | Django version 5.1, using settings 'dialyproject.settings'
web-1  | Starting development server at http://0.0.0.0:8000/
web-1  | Quit the server with CONTROL-C.
```

## Start bash shell (Optional)

In order to interact within the docker container, you should start bash shell by
```
docker compose exec web bash
```
Then, you can type whatever command in the docker container.
