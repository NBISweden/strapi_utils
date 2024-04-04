import argparse
import yaml
import requests
import json
import pdb

def custom_get(url, admin_token):
    headers={
        'Authorization': f'Bearer {admin_token}',
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='Path to the YAML config file', required=True)
parser.add_argument('-r', '--role', help='Name of role to assign to all users', required=True)
parser.add_argument('-t', '--admin_token', help='Admin token, overrides the one in the config file')
parser.add_argument('-d', '--dry_run', help='Dry run mode, does not make any changes', action='store_true')
args = parser.parse_args()

# Load config from YAML file
with open(args.config, 'r') as file:
    config = yaml.safe_load(file)

# Strapi's base URL
base_url = config['url']

# Get admin token
admin_token = args.admin_token or config.get('api_token') or sys.exit('Admin token is required')

# Initialize pagination
page = 1
pagesize = 100  # Adjust this value based on your needs

while True:
    print(f'Fetching users from {pagesize*(page-1)} to {pagesize*page}...')
    # Get users with pagination
    users_response = requests.get(
        f'{base_url}/users/?pageSize={pagesize}&page={page}',
        headers={
            'Authorization': f'Bearer {admin_token}',
        }
    )

    users = users_response.json()['data']['results']

    if not users:
        break  # Exit the loop if no more users are returned

    # Get role
    role_response = requests.get(
        f'{base_url}/roles',
        headers={
            'Authorization': f'Bearer {admin_token}',
        }
    )
    
    roles = role_response.json()['data']
    requested_role = None
    for role in roles:
        if role['name'] == args.role:
            requested_role = role
            break

    if requested_role is None:
        print('Failed to fetch role.')
        exit()

    # Assign role to all users
    for i,user in enumerate(users, 1):

        if args.dry_run:
            print(f'Dry run {i}/{len(users)}: Would have assigned role "{args.role}" to user {user["firstname"]} {user["lastname"]} ({user["email"]}).')

        else:
            print(f'{i}/{len(users)}: Assigning role "{args.role}" to user {user["firstname"]} {user["lastname"]} ({user["email"]}).')
            requests.put(
                f'{base_url}/users/{user["id"]}',
                headers={
                    'Authorization': f'Bearer {admin_token}',
                },
                data={'roles': list(set([role['id'] for role in user['roles'] ] + [requested_role['id']]))}
            )

    # Move to the next page
    page += 1

print('Role has been assigned to all users.')
