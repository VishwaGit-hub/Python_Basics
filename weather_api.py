import requests
import datetime 
import time



########################$torme weather api#########################################
# api="b13a50fa-07c9-11f1-8129-0242ac120004-b13a515e-07c9-11f1-8129-0242ac120004"

# url="https://api.stormglass.io/v2/weather/point"

# params={
#     "lat":21.17,
#     "lng":72.83,
#     "params":"airTemperature"
    
# }
# headers={
#     'Authorization':api
# }

# response=requests.get(url=url,params=params,headers=headers)
# print(response)
# json_data=response.json()
# print(json_data)
#################################################


import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

url="https://api.open-meteo.com/v1/forecast"


cache_session=requests_cache.CachedSession('.cache',expire_after=3600)
retry_session=retry(cache_session,retries=5,backoff_factor=0.2)
open_mateo=openmeteo_requests.Client(session=retry_session)

parms={
    "latitude":21.17,
    "longitude":72.83,
    "hourly":"temperature_2m"
}
responses=open_mateo.weather_api(url,params=parms)
response=responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

hourly=response.Hourly() #fetches hourly data 
hourly_temperature_2m=hourly.Variables(0).ValuesAsNumpy() #converts hourly data to numpy 
print(hourly_temperature_2m)

hourly_data={"date": pd.date_range(
    start=pd.to_datetime(hourly.Time(),unit='s',utc=bool),
    end=pd.to_datetime(hourly.TimeEnd(),unit='s',utc=bool),
    freq=pd.Timedelta(seconds=hourly.Interval()),
    inclusive="left" 
)}

hourly_data['temperature_2m']=hourly_temperature_2m

hourly_dataframe=pd.DataFrame(data=hourly_data)
print("Hourly data")
print(hourly_dataframe)




#Open weather 