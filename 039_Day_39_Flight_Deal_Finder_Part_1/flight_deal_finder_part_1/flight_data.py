from datetime import datetime, timedelta

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.departure_city = "DEN" # fly_from
        # self.arrival_city = fly_to #fly_to
        self.currency = "USD" #curr
        self.max_stopovers = 0 #max_stopovers (direct)
        self._today = datetime.now()
        # self.search_date_start = (self._today + timedelta(days=1)).strftime("%d/%m/%y") #date_from
        # self.search_date_end = (self.search_date_start + timedelta(days=6*30)).strftime("%d/%m/%y") #date_to
        self.search_date_start = self._today + timedelta(days=1)
        self.search_date_end = self.search_date_start + timedelta(days=6*30)
        self.flight_type = "round" #flight_type
        self.return_flight_min_max_days = (7,28) #nights_in_dst_from | nights_in_dst_to
        self.price = 0 
        self.search_date_start = self.format_search_dates_for_tequila(self.search_date_start)
        self.search_date_end = self.format_search_dates_for_tequila(self.search_date_end)


    def format_search_dates_for_tequila(self, date):
        date = date.strftime("%d/%m/%y")
        # date = str(date).split(' ')[0]
        print(date)
        return date