from app.env import get_env


def get_mongo_conn_url():
    env = get_env()
    cluster_url = env.get("MONGO_CLUSTER_URL")
    mongo_user = env.get("MONGO_USER")
    mongo_password = env.get("MONGO_PASSWORD")
    if not cluster_url or not mongo_user or not mongo_password:
        return "No connection string"
    conn_string = f"mongodb+srv://{mongo_user}:{mongo_password}@{cluster_url}/?retryWrites=true&w=majority"
    return conn_string
