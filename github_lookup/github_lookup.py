import requests
import sys

try:
    username = sys.argv[1]
    if len(sys.argv) > 2:
        sys.exit("Too many arguments, just enter username")
except IndexError:
    sys.exit("Missing username argument")
try:
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        sys.exit("User not found")

except requests.RequestException:
    sys.exit("Error making request")

data = response.json()

if data["name"] is None:
    name = "No Name"
else:
    name = data["name"]

creation = data["created_at"]

repos = data["public_repos"]

print(f"{name}\n{creation}\n{repos}")