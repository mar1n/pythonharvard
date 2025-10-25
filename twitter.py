import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")