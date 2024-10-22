import requests
import pandas as pd
def fect_data():
    url="http://www.geoplugin.net/json.gp"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data =response.json()

        data_info=[
            {
                'Country':data.get('geoplugin_countryName','N/A'),
                'State':data.get('geoplugin_region','N/A'),
                'City':data.get('geoplugin_city','N/A'),
            }
        ]
        df=pd.DataFrame(data_info)
        df.to_csv('Data.csv',index=False)
        print("Data Convertes Successfully")
    except Exception as e:
        print(f"Error is :{e}")
fect_data()