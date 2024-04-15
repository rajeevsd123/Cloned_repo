import pandas as pd
import matplotlib.pyplot as plt


csv_path = "Metro_Interstate_Traffic_Volume.csv"
# Import the CSV into a pandas DataFrame
Traffic_Volume_df = pd.read_csv(csv_path)
Traffic_Volume_df['date_time'] = pd.to_datetime(Traffic_Volume_df['date_time'])


#Extract day of the week
#Monday =0, Sunday =6 
Traffic_Volume_df['day_of_week'] = Traffic_Volume_df['date_time'].dt.day_of_week

#Group data by month and calculate average daily traffic
monthly_avg_traffic = Traffic_Volume_df.groupby(Traffic_Volume_df['date_time'].dt.to_period('M'))['traffic_volume'].mean()

#Separate data for weekdays and weekends
weekdays_data = Traffic_Volume_df[Traffic_Volume_df['day_of_week']<5]  #Weekdays Monday to Friday
weekends_data = Traffic_Volume_df[Traffic_Volume_df['day_of_week']>=5] #Weekends Saturday to Sunday

#Group Weekday and Weekend data  by month and calulate average daily traffic
weekday_avg_traffic = weekdays_data.groupby(weekdays_data['date_time'].dt.to_period('M'))['traffic_volume'].mean()
weekend_avg_traffic = weekends_data.groupby(weekends_data['date_time'].dt.to_period('M'))['traffic_volume'].mean()


# Plot graphs
plt.figure(figsiz=(10,6))

#Monthly average daily traffic

plt.plot(monthly_avg_traffic.index_to_timestamp(), monthly_avg_traffic, label='Monthly Average Traffic')

#Weekday average daily traffic

plt.plot(weekday_avg_traffic.index_to_timestamp(), weekday_avg_traffic, label='Weekday Average Traffic')

#Weekend average daily traffic

plt.plot(weekend_avg_traffic.index_to_timestamp(), weekend_avg_traffic, label='Weekend Average Traffic')

plt.xlabel('Date')
plt.ylabel('Traffice Volume')
plt.title('Monthyl Average Daily Traffic')

plt.legent()

plt.show()


