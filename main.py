import requests

endpoint = 'https://swat.wiki/api/users/all'
client = requests.session()
data_set = client.get(endpoint).json()

def iterate_swat_wiki_users(json_obj):
    def process_users(users):
        if not users:
            return

        max_id_width = max(len(user['_id']) for user in users)
        max_username_width = max(len(user['username']) for user in users)
        max_role_width = max(len(user['role']) for user in users)
        max_created_at_width = max(len(user['createdAt']) for user in users)
        max_joined_at_width = max(len(user['joined']) for user in users)

        for user in users:
            _id = user['_id'].ljust(max_id_width)
            username = user['username'].ljust(max_username_width)
            role = user['role'].ljust(max_role_width)
            created_at = user['createdAt'].ljust(max_created_at_width)
            joined = user['joined'].ljust(max_joined_at_width)

            print(f"\n[{user['username']}]")
            print(f"\\___[ {_id} ]\n\t| username: {username}\n\t| rank: {role}\n\t| created at: {created_at}\n\t| joined: {joined}")
            print('_' * 32)

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if isinstance(value, list):
                process_users(value)
            elif isinstance(value, dict):
                iterate_swat_wiki_users(value)
    elif isinstance(json_obj, list):
        process_users(json_obj)

iterate_swat_wiki_users(data_set)
