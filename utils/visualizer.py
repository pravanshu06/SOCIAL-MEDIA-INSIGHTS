import matplotlib.pyplot as plt

def visualize(data):
    usernames = [p['username'] for p in data]
    followers = [p['followers'] for p in data]

    plt.figure(figsize=(10, 5))
    plt.bar(usernames, followers, color='skyblue')
    plt.title("Follower Count per Profile")
    plt.xlabel("Username")
    plt.ylabel("Followers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
