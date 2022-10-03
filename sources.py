from requests import get, post

def get_remote_resource(source_id: str):
    response = get(f"https://pastebin.com/raw/{source_id}")
    if response.ok:
        return response.text
    print("Unknown source")

def get_local_resource(source_path: str):
    with open(source_path) as file:
        return file.read().splitlines()