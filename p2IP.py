# extract info from csv documents to create a big csv containing all the info we need for our study
# @author: 2022-2023, Charles DUVAL, Dylan DRAY

#%% import libraries
import pandas as pd # to analyse data
from icecream import ic # a better print
import time as t
#%% data of the first user

# user = "user_1"
# data = pd.read_csv("MMASH\\DataPaper\\" + user + "\\Actigraph.csv", sep = ",", header = 0)
# ic(data)

# #put inside the useful_data dataframe the colums hr, day and time 
# useful_data = data[['HR', 'day', 'time']]
# ic(useful_data) 

# # get the sleep time per day of the user
# data_sleep = pd.read_csv("MMASH\\DataPaper\\" + user + "\\sleep.csv", sep = ",", header = 0)
# #put inside the useful_data_sleep dataframe the colums day and sleep time
# useful_data_sleep = data_sleep[['In Bed Date', 'Out Bed Date', 'In Bed Time', 'Out Bed Time', 'Efficiency']]
# ic(useful_data_sleep)




# value = useful_data_sleep['In Bed Time'][0]
# value_2 = useful_data_sleep['Out Bed Time'][0]
#  #convert value from string to datetime
# value_date = pd.to_datetime(value, format = '%H:%M')
# value_2_date = pd.to_datetime(value_2, format = '%H:%M')





# #for each line of the dataframe useful_data_sleep
# sleep_dataframes = [] # a list of daframe, containinf the sleep HR of each sleep period
# for index, row in useful_data_sleep.iterrows():
#     hr_sleep_dataframe = pd.DataFrame(columns = ['HR', 'day', 'time'])
#     #fill the hr_sleep_dataframe with the HR contained in the useful_data dataframe where the day coincide and the time is between IN BED TIME and OUT BED TIME
#     for index2, row2 in useful_data.iterrows():
#         if row['In Bed Date'] == row['Out Bed Date']:
#             if row2['day'] == row['In Bed Date'] and row2['time'] >= row['In Bed Time'] and row2['time'] <= row['Out Bed Time']:
#                 hr_sleep_dataframe = hr_sleep_dataframe.append(row2, ignore_index = True)
#         else:
#             if (row2['day'] == row['In Bed Date'] and row2['time'] >= row['In Bed Time']) or (row2['day'] == row['Out Bed Date'] and row2['time'] <= row['Out Bed Time']):
#                 hr_sleep_dataframe = hr_sleep_dataframe.append(row2, ignore_index = True)
#     sleep_dataframes.append(hr_sleep_dataframe)
#     ic("sleep period " + str(index) + " done")
# #for every dataframe in sleep_dataframes
# # write the content in a csv file with the name of the user and the index of the dataframe
# for i in range(len(sleep_dataframes)):
#     sleep_dataframes[i].to_csv("MMASH\\DataPaper\\"+user + "\\sleep_" + str(i) + ".csv", sep = ",", index = False)

#%% effective code
import pandas as pd # to analyse data
from icecream import ic # a better print


ic.disable()
def function(nb_user):
    user = "user_" + str(nb_user)
    data = pd.read_csv("MMASH\\DataPaper\\" + user + "\\Actigraph.csv", sep = ",", header = 0)
    ic(data)
    useful_data = data[['HR', 'day', 'time']]
    ic(useful_data) 
    data_sleep = pd.read_csv("MMASH\\DataPaper\\" + user + "\\sleep.csv", sep = ",", header = 0)
    useful_data_sleep = data_sleep[['In Bed Date', 'Out Bed Date', 'In Bed Time', 'Out Bed Time', 'Efficiency']]
    sleep_dataframes = [] # a list of daframe, containinf the sleep HR of each sleep period
    for index, row in useful_data_sleep.iterrows():
        hr_sleep_dataframe = pd.DataFrame(columns = ['HR', 'day', 'time'])
        #fill the hr_sleep_dataframe with the HR contained in the useful_data dataframe where the day coincide and the time is between IN BED TIME and OUT BED TIME
        for index2, row2 in useful_data.iterrows():
            if row['In Bed Date'] == row['Out Bed Date']:
                if row2['day'] == row['In Bed Date'] and row2['time'] >= row['In Bed Time'] and row2['time'] <= row['Out Bed Time']:
                    hr_sleep_dataframe = hr_sleep_dataframe.append(row2, ignore_index = True)
            else:
                if (row2['day'] == row['In Bed Date'] and row2['time'] >= row['In Bed Time']) or (row2['day'] == row['Out Bed Date'] and row2['time'] <= row['Out Bed Time']):
                    hr_sleep_dataframe = hr_sleep_dataframe.append(row2, ignore_index = True)
        sleep_dataframes.append(hr_sleep_dataframe)
        print("sleep period " + str(index) + " done")
    for i in range(len(sleep_dataframes)):
        sleep_dataframes[i].to_csv("updated_data\\"+user + "_sleep_" + str(i) + ".csv", sep = ",", index = False)
    print("user " + str(nb_user) + " done")
for i in range(1,23):
    function(i)
