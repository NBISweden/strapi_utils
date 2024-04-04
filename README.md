# Strapi utils

## Admin API token

The token generated in the web ui is not allowed to talk to the admin inteface, and there is no way to create admin api tokens automatically. You can fish out of the web browser though and use that one, as they are valid for 30 days.

1. Login to the strapi admin panel in the web browser as usual.
1. Open devtools (ctrl+shift+c).
1. Open the `Storage` tab.
1. Select `Session Storage` and your site.
1. Copy the value for the key `jwtToken`, e.g. `eyJhb....`, and replace the `api_token` value in the `config.yaml` file or give it as `-t` when running the script.


## Usage

#### add_role_to_all_users.py

```bash
# to add the role "NBIS staff" to all users
python3 add_role_to_all_users.py -c config.yaml -r "NBIS staff"

# see -h for additional option
```


## Development

Documentation for the `api/` endpoints: https://docs.strapi.io/dev-docs/api/rest

There is no documentation of the `admin/` api that i have found, so you have to use devtools to inspect the requests/posts the web ui does when you do thing in it.

1. Login to the strapi admin panel in the web browser as usual.
1. Open devtools (ctrl+shift+c).
1. Open the `Network` tab.
1. Do the thing you want to automate.
1. Look at the `File` column for your request and select it.
1. Look at the `Headers` or `Request` tab depending on what info you are looking for.

