import yfinance as yahooFinance

# in order to specify start date and
# end date we need datetime package
import datetime

# startDate , as per our convenience we can modify
startDate = datetime.datetime(2019, 5, 31)

# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 1, 7530)
GetFacebookInformation = yahooFinance.Ticker("FB")

# pass the parameters as the taken dates for start and end
print(GetFacebookInformation.history(start=startDate,
									end=endDate))
# 
startDate , as per our convenience we can modify
startDate = datetime.datetime(2019, 5, 31)

# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 1, 30)
GetFacebookInformation = yahooFinance.Ticker("FB")

# pass the parameters as the taken dates for start and end
print(GetFacebookInformation.history(start=startDate,
									end=endDate))
# startDate , as per our convenience we can modify
startDate = datetime.datetime(2019, 5, 31)

# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 1, 30)
GetFacebookInformation = yahooFinance.Ticker("FB")

# pass the parameters as the taken dates for start and end
print(GetFacebookInformation.history(start=startDate,
									end=endDate))
# 

# 
