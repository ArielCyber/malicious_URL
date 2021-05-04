import requests
import csv
from dns import resolver

# url = WHAT TO DOWNLOAD
url = 'http://data.phishtank.com/data/online-valid.csv'
# csv file name existing on new
csv_file_name = "malicious_urls.csv"


# download from the given url ande save to the current dir at phish_tank.csv
def download_phishtankcsv(url):
    phishtank_domains = requests.get(url, allow_redirects=True)
    open('phish_tank.csv', 'wb').write(phishtank_domains.content)


# extract the domain from the given CSV file (phishTank csv dataset)
def extract_Domain(phishTankCSV):
    malicious_urls = []
    with open(phishTankCSV, newline='') as downloadedcsv:
        downloadedURLs = csv.reader(downloadedcsv)
        for row in downloadedURLs:
            url = row[1].split('//')
            if url[0] == 'http:' or url[0] == 'https:':
                url.pop(0)
            url = url[0].split('/')
            malicious_urls.append(url[0])
    malicious_urls.pop(0)
    return malicious_urls


# combine the new malicious urls with the old urls you have the malicious_urls.csv file
# and filter it out into unique domain (no duplicates)
# def combine_new_old(new_urls, maliciousURLsCSV):
#     tmp_list = []
#     with open(maliciousURLsCSV, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for line in csv_reader:
#             line = line[0].split(';')
#             m_url = line [0]
#             tmp_list.append(m_url)
#     # filter the domains we had there information
#     for domain in new_urls:
#         if domain in tmp_list:
#             new_urls.remove(domain)
#
#     combined = list(dict.fromkeys(new_urls))
#     return combined


# take a list of all the new downloaded domains and filter only the new once
def urls_with_no_data(new_urls, maliciousURLsCSV):
    csv_list = []
    try:
        with open(maliciousURLsCSV, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                m_url = line [0]
                csv_list.append(m_url)
        tmp = []
        for domain in new_urls:
            if domain not in csv_list:
                tmp.append(domain)

        combined = list(dict.fromkeys(tmp))
        return combined

    except:
        combined = list(dict.fromkeys(new_urls))
        return combined

# get domains list and checks if the domain is valid
def filter_dns(domains):
    valid_domains = []
    for domain in domains:
        try:
            result = resolver.query(domain, 'A')
            valid_domains.append(domain)

        except:
            pass

    return valid_domains

#append the new domains to the csv file
def creat_csv(domains,file_name):
    with open(file_name ,'a') as f:
        for domain in domains:
            f.write("%s\n" % domain)
        f.write("*****\n")

if __name__ == '__main__':
    # download the new csv
    download_phishtankcsv(url)
    # extract the domains
    domains = extract_Domain('phish_tank.csv')
    # filter one the new once
    new_urls = urls_with_no_data(domains, csv_file_name)
    # filter only the valid once
    valid = filter_dns(new_urls)
    # apped them to the csv
    creat_csv(valid,csv_file_name)
    print(len(new_urls))


# TODO save the dns data and dont ask more