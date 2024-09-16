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

## Start bash shell (Optional)

In order to interact within the docker container, you should start bash shell by

```
docker compose exec web bash
```

Then, you can type whatever command in the docker container.

# ROOTING

`/` : 未設定
`/doc/` : APIドキュメント
`/admin/` : 管理画面
`/users/` : アカウントに対する処理 (API)
