import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import smtplib
import time

load_dotenv(r'033_Day_33_API_Endpoints_and_API_Parameters_ISS_Overhead_Notifier\issoverhead\.env')
MY_LAT = float(getenv('MY_LAT'))
MY_LONG = float(getenv('MY_LONG'))
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')

def check_for_ISS_proximity(iss_location: tuple, my_location: tuple):
    """If the ISS is within 5 lat/long of your location, it returns True, otherwise False.

    Args:
        iss_location (tuple): A tuple containing the ISS's latitude and longitude; make sure both locations are in the same order (lat --> lat, long --> long)
        my_location (tuple): A tuple containing your latitude and longitude

    Returns:
        is_near_me (bool): True means it's in proximity to you; False means it's not
    """
    is_near_me: bool = False
    if iss_location[0] in range(int(my_location[0]-5), int(my_location[0]+5)) and iss_location[1] in range(int(my_location[1]-5), int(my_location[1]+5)):
        is_near_me = True
    return is_near_me


def check_for_darkness(sunset: int, sunrise: int, curr_time: datetime):
    """Returns a boolean with a value based on whether or not it's dark outside. It takes in the sunrise and sunset for the region for which it calculates this, based on the current time.

    Args:
        sunset (int): The local hour of the sunset
        sunrise (int): The local hour of the sunrise
        curr_time (datetime): The current local time

    Returns:
        is_dark(bool): Whether or not it is currently dark outside
    """
    
    is_dark: bool = False
    if curr_time.hour > sunset or curr_time.hour < sunrise:
        is_dark = True
    return is_dark


def notify_via_email():
    with smtplib.SMPTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER,
            msg=f"Subject: Check the Sky for the ISS!\n\nThe International Space Station should be visible now somewhere in the night skies!"
        )


# I could also stash all of this inside the check_for_ISS_proximity function
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()






while True:
    #If the ISS is close to my current position
    if check_for_ISS_proximity(iss_location=(iss_latitude, iss_longitude), my_location=(MY_LAT, MY_LONG)):
        # and it is currently dark
        if check_for_darkness(sunset=sunset, sunrise=sunrise, curr_time = time_now):
            # could make this more modular to take any email / password / recipient
            # Then send me an email to tell me to look up.
            notify_via_email()
        else:
            print("The International Space Station is presently near you, but it isn't dark outside so you won't be able to see it.")
    else:
        print("The International Space Station is not presently near you.")
    
    # BONUS: run the code every 60 seconds.
    time.sleep(60)


