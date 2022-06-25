#!/usr/bin/env python3
from csv import writer

from models.website import Website


def main():
    path = "domains.csv"

    domains: list[str] = []
    sites: list[Website] = []

    with open(path) as file:
        contents = file.readlines()

        for line in contents:
            domains.append(line.strip())


    for domain in domains:

        site = Website(domain)
        print(f"Scanning {site.domain} ...")
        site.crawl()
        

        sites.append(site)

    """ for site in sites:
        print(f"{site.domain}: {site.banner.name}") """
    with open("output.csv", 'w', encoding='UTF8', newline='') as file:
        w = writer(file)
        
        w.writerow(["Domain", "Banner"])

        for site in sites:
           w.writerow([site.domain, site.banner.name.capitalize()])



if __name__ == '__main__':
    main()