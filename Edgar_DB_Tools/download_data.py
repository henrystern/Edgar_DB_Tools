import requests
import zipfile
import io
from datetime import datetime

# Download and extract datasets over a specified period
def download_data(start_year=2009,
                  start_qtr=1,
                  end_year=(datetime.now().year - 1),
                  end_qtr=4,
                  output_dir="./edgar_data/"):

    for year in range(start_year, end_year + 1):
        for q in range(start_qtr, 4 + 1):
            if year == end_year and q == end_qtr + 1:
                break
            period = str(year) + "q" + str(q)
            print(f'{datetime.now():%m-%d %H:%M:%S}', "Downloading", period)
            u = "https://www.sec.gov/files/dera/data/financial-statement-data-sets/" + period + ".zip"
            r = requests.get(u, stream=True)
            print(f'{datetime.now():%m-%d %H:%M:%S}', "Extracting", period)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(output_dir + period)
        start_qtr = 1


if __name__ == "__main__":
    download_data()