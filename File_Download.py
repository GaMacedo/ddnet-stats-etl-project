import wget

'''
This file is to download data from ddnet
'''


###### File url, all zip files ######

# csv file
url = 'https://ddnet.tw/stats/ddnet-stats.zip'

# Sql file 
# url = 'https://ddnet.tw/stats/ddnet-sql.zip'

# Sqllite file
# url = 'https://ddnet.tw/stats/ddnet.sqlite.zip'

local_file = 'data/stats.zip'

# Make http request for remote file data
wget.download(url, local_file)
