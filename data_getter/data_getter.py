import requests
from bs4 import BeautifulSoup


def get_cricket_rankings(start_year, end_year, dwn_path):
    #url = "https://www.relianceiccrankings.com/datespecific/odi/batting/1983/11/01/"
    
    month = [ ["January", 31], ["February", 28], ["March", 31], ["April", 30], ["May", 31], ["June", 30], ["July", 31], ["August", 31], ["September", 30], ["October", 31], ["November", 30], ["December", 31] ]

    count = 0
    try:
        for y in range(start_year, end_year, 1):
            for m in range(1, 12+1, 1):
                n = m-1
                for d in range(1, month[n][1]+1, 1):
    
                    year = y
                    mn = m
                    dt = d

                    mn_fr = str(mn).zfill(2)
                    dt_fr = str(dt).zfill(2)

                    url = "https://www.relianceiccrankings.com/datespecific/odi/batting/{}/{}/{}/"
                    url_fr = url.format(year,mn_fr,dt_fr)

                    test = "table table-sm mb-0 w-100"
                    
                    # Send a GET request to the URL
                    response = requests.get(url_fr)

                    if response.status_code == 200:
                        count += 1
                        # Parse the HTML content of the page
                        soup = BeautifulSoup(response.text, 'html.parser')
                
                        # Locate the table you want to extract (modify the tag and class accordingly)
                        table = soup.find('table', class_=test)

                        file_name = "table_data_{}.txt"
                        file_name_fr = file_name.format(count)
                        fpath = dwn_path
                        fwrite = fpath + file_name_fr
                        # Open a text file in write mode
                        with open(fwrite, 'w') as file:
                        
                            # Iterate through rows and columns of the table
                            countr = 0
                            for row in table.find_all('tr'):
                                countr +=1
                                columns = row.find_all(['th', 'td'])
                                if countr >= 2 and countr <= 101:
                                    file.write(f"{d}\t{month[n][0]}\t{y}\t")
                                    countc = 0
                                    for column in columns:
                                        countc +=1
                                        if countc <= 3:
                                            #print(column.text)
                                            # Write the content of each cell to the text file
                                            file.write(column.text + '\t')
                                        
                                    file.write('\n')
                                    
                    else:
                        print('Failed. Status code:', response.status_code)
                        return count
            return count
            
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return count
                
