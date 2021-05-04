from dns import resolver


# get domains list and checks if the domain is valid
def filter_dns(domains):

    valid_domains = []
    print(len(domains))
    for domain in domains:
        try:
            result = resolver.query(domain, 'A')
            valid_domains.append(domain)
            for ipval in result:
                print(ipval)
        except:
            pass

    print(len(valid_domains))



