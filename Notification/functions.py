import requests
import schedule
import time
import pandas as pd


df = pd.DataFrame(columns=["Time", "Connected"])

def check_connection():
    url = "https://www.google.com"
    current_time = time.ctime()
    try:
        response = requests.get(url)
        connected = response.status_code == 200
        if connected:
            print("Connected", current_time)
            df.loc[len(df)] = [current_time, 1]
        else:
            print("Disconnected", current_time)
            df.loc[len(df)] = [current_time, 0]
    except requests.ConnectionError:
        print("Disconnected", current_time)
        df.loc[len(df)] = [current_time, 0]

schedule.every(1).seconds.do(check_connection)

while True:
    schedule.run_pending()
    time.sleep(1)
    df.to_csv("connection_status.csv", index=False)
