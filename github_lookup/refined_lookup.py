import requests
import sys
import csv

def main():
    user = username()
    data = request(user)
    response(data)

def username():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many arguments, just enter username")
        else:
            user = sys.argv[1]
            return user
    except IndexError:
        sys.exit("Missing username argument")

def request(user):
    try:
        data = requests.get(f"https://api.github.com/users/{user}")
        if data.status_code != 200:
            sys.exit("User not found")
        else:
            return data.json()
    except requests.RequestException:
        sys.exit("Error making request")

def response(data):
    if data["name"] is None:
        name = "No Name"
    else:
        name = data["name"]     

    creation = data["created_at"]

    repos = data["public_repos"]

    with open("gitlookup.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "creation", "repos"])
        writer.writerow({"name": name, "creation": creation, "repos": repos})

    print(f"{name}\n{creation}\n{repos}\n\nResults saved to gitlookup.csv")

main()