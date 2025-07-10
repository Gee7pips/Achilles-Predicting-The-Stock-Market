import yaml

def verify_admin(username, password):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
    return username == config["admin_user"] and password == config["admin_password"]