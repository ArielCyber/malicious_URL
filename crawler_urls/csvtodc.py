import csv

output = []

with open('/home/nour/Desktop/RobustMaliciousURLDetection/Datasets/urls/newdataset/m_urls.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = row[0].split(',')
        output.append(row[0] + ';1')

output = list(dict.fromkeys(output))


with open('/home/nour/Desktop/m_url_test_full','w') as out:

    for i in range(10):
        out.write('%s\n' % output[i])


print('done',len(output))