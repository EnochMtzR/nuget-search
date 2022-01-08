#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tabulate import tabulate
import re
import sys

def get_title(package):
    return package.find_all("a", {"class": "package-title"})[0].text

def get_version(package):
    version_container = package.find_all("span", {"class": "icon-text"})[2]
    return version_container.find_all("span")[0].text

def get_authors(package):
    container = package.find_all("span", {"class": "package-by"})[0]
    author_containers = container.find_all("a")
    return list(map(lambda author_container: author_container.text, author_containers))

def get_downloads(package):
    downloads_container = package.find_all("span", {"class": "icon-text"})[0]
    return downloads_container.text.replace("total downloads", " ").strip()

def get_package(packageContainer):
    return [
        get_title(packageContainer),
        get_version(packageContainer),
        get_authors(packageContainer),
        get_downloads(packageContainer)
    ]
    

def get_packages(package_containers):
    return list(map(lambda container: get_package(container), package_containers))

def print_page(packages, page):
    print(tabulate(packages, headers=["Title", "Version", "Authors", "Downloads"]))

page = 1
search = sys.argv[1]

while True:
    url = f"https://www.nuget.org/packages?q={search}&page={page}&sortBy=relevance"
    web_page = urlopen(url)
    html = web_page.read().decode("utf-8")
    html = BeautifulSoup(html, "html.parser")
    package_containers = html.find_all("article", {"class": "package"})

    packages = get_packages(package_containers)

    print_page(packages, page)
    
    command = input(":")
    
    if command == "q":
        break
    if command == "n" or command == "":
        page += 1
    else:
        search = command