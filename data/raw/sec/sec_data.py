import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

#Ticker is a unique number of US Companies
def get_cik_from_ticker(ticker:str) -> str:
    url= "https://www.sec.gov/files/company_tickers.json"
    headers={'User-Agent': os.getenv('SEC_USER_AGENT')}
    response=requests.get(url, headers=headers)
    response.raise_for_status()
    data=response.json()
    
    #Search for ticker
    for company in data.values():
        if company['ticker'].upper() ==ticker.upper():
            cik=str(company['cik_str']).zfill(10)
            return cik
        
    return None




#Test
if __name__ == "__main__":
    cik = get_cik_from_ticker('AAPL')
    print(f"Apple CIK: {cik}")


