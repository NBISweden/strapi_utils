# Strapi utils

## Admin API token

The token generated in the web ui is not allowed to talk to the admin inteface, and there is no way to create admin api tokens automatically. You can fish out the web browsers token though and use that one,

1. Login to the strapi admin panel in the web browser as usual.
1. Open devtools (ctrl+shift+c).
1. Open the `Network` tab.
1. Refresh the page.
1. Select the any of the rows that appear and find one that has `Request Headers` and a key called `Authorization`. Ex. `Authorization:	Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxMDAwMDAwMDAwLCJleHAiOjEwMDAwMDAwMDF9.lnp5LlOfXWzBBj6sxCoBWF-4fIXjYmR6v59AHufaxbc`
1. Copy the key, `eyJhb....`, and replace the `api_token` value in the `config.yaml` file.


## Usage

#### add_role_to_all_users.py

```bash
# to add the role "NBIS staff" to all users
python3 add_role_to_all_users.py config.yaml "NBIS staff"
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

