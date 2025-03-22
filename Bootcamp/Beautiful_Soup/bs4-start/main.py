from bs4 import BeautifulSoup

with open(file="./website.html", mode="r") as file_stream:
    contents = file_stream.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())
