import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
	
	"""
    	Asks user to specify a city, month, and day to analyze.

    	Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
   	 """
	print('Hello! Let\'s explore some US bikeshare data!')
    	# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
	city = input("enter the name of the city among <chicago> , <new york city> or <washington>: ")
	city = city.lower()
	while city not in ['chicago','new york city','washington']:
        	print("please enter a valid city among <chicago> , <new york city>, <washington>: ")
        	city = input("enter the name of the city")
        	city = city.lower()
    	# get user input for month (all, january, february, ... , june)
	month = input(" enter the name of the month among 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december' or 'all': ")
	month = month.lower()
	while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 					'december', 'all']:
        	print("please enter a valid month name among 'january', 			   				'february','march','april','may','june','july','august','september','october','november','december' or 'all': ")
        	month = input("enter the name of the month")
        	month = month.lower()

    	# get user input for day of week (all, monday, tuesday, ... sunday)
	
	day = input(" enter the day of the week among 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', or 'all :" )
	day = day.lower()
	while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        	print(" please enter a valid day of the week among 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'or 				all: ")
        	day = input("enter the name of the day of the week")
        	day = day.lower()
        		
	print('-'*40)
	return city, month, day


def load_data(city, month, day):
	"""
	    Loads data for the specified city and filters by month and day if applicable.

	    Args:
		(str) city - name of the city to analyze
		(str) month - name of the month to filter by, or "all" to apply no month filter
		(str) day - name of the day of week to filter by, or "all" to apply no day filter
	    Returns:
		df - Pandas DataFrame containing city data filtered by month and day
	"""
	df = pd.read_csv(CITY_DATA[city])
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['Month'] = df['Start Time'].dt.month_name()
	df['Month'] = df['Month'].map(lambda x:x.lower())
	df['day_of_week'] = df['Start Time'].dt.day_name().map(lambda x:x.lower())
	df['Hour'] = df['Start Time'].dt.hour	
	
	if month != 'all':
	
        	month = month
    
        	# filter by month to create the new dataframe
        	df = df.loc[df['Month'] == month]

	# filter by day of week if applicable
	if day != 'all':
    		# filter by day of week to create the new dataframe
    		df = df.loc[df['day_of_week']== day]
	
	return df


def time_stats(df):
	"""Displays statistics on the most frequent times of travel."""

	print('\nCalculating The Most Frequent Times of Travel...\n')
	start_time = time.time()

	# display the most common month
	popular_month = df["Month"].value_counts()
	print("\nMost common Month is: {}".format(popular_month.index[0]))	

	# display the most common day of week
	popular_day = df["day_of_week"].value_counts()
	print("\nMost common day of the week is: {}".format(popular_day.index[0]))

	# display the most common start hour
	popular_hour = df["Hour"].value_counts()
	print("\nMost common hour of the day is: {}\n".format(popular_hour.index[0]))	

	print("\nThis took %s seconds." % (time.time() - start_time))
	
	print('-'*40)


def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""

	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()

	# display most commonly used start station
	df['Start Station'] = df['Start Station'].map(lambda x:x.lower())
	df['End Station'] = df['End Station'].map(lambda x:x.lower())

	popular_start_station = df["Start Station"].value_counts()
	print("\nMost common Start Station is: {}".format(popular_start_station.index[0].title()))
	# display most commonly used end station
	popular_end_station = df["End Station"].value_counts()
	print("\nMost common End Station is: {}".format(popular_end_station.index[0].title()))

	# display most frequent combination of start station and end station trip
	df['Start End Combo'] = df['Start Station'] +"-" + df['End Station']

	popular_combo_station = df["Start End Combo"].value_counts()
	print("\nMost common Combo Station is: {}\n".format(popular_combo_station.index[0].title()))

	print("\nThis took %s seconds." % (time.time() - start_time))
	
	print('-'*40)


def trip_duration_stats(df):
	"""Displays statistics on the total and average trip duration."""

	print('\nCalculating Trip Duration...\n')
	start_time = time.time()

	# display total travel time
	print("\nTotal Travel Time is: {:.4f} Days".format(df['Trip Duration'].sum()/3600/24))

	# display mean travel time
	print("\nAverage Travel Time is: {:.4f} Minutes\n".format(df['Trip Duration'].mean()/60))

	print("\nThis took %s seconds." % (time.time() - start_time))
	
	print('-'*40)


def user_stats(df,city):
	"""Displays statistics on bikeshare users."""

	print('\nCalculating User Stats...\n')
	start_time = time.time()

	# Display counts of user types
	print("\nCount of each user type is:\n{}\n".format(df['User Type'].value_counts()))

	# Display counts of gender
	if (city == 'chicago' or city == 'new york city'):
		
        	popular_gender = df["Gender"].value_counts()
		# Display earliest, most recent, and most common year of birth

        	print("\nCount of each Gender type is:\n{}\n".format(popular_gender))
        	min_birth_year = min(df['Birth Year'])
        	print("\nOldest Rider was born in {:.0f}".format(min_birth_year))
        	print("\nYoungest Rider was born in {:.0f}".format(max(df['Birth Year'])))
        	print("\nMost common year of birth for riders is: {:.0f}".format(df['Birth Year'].value_counts().index[0]))
        	
	print("\nThis took %s seconds." % (time.time() - start_time))
	
	print('-'*40)


def main():
	while True:
	        city, month, day = get_filters()
	        df = load_data(city, month, day)

	        time_stats(df)
	        station_stats(df)
	        trip_duration_stats(df)
	        user_stats(df,city)
	        
	        raw_data = input("/nDo you want to see raw trip data? Enter <Yes> or <No>: ")
	        raw_data =raw_data.lower()
	        present_count = 0
	        while (raw_data == 'yes'):
	        	if (present_count + 5 >= df.shape[0]):
	        		print(df.iloc[list(range(present_count,df.shape[0]-1,1))])
	        		print("\n End of file reached hence quitting!!!\n")
	        		break
	        	else:
	        		print(df.iloc[list(range(present_count,present_count+5,1))])
	        		present_count += 5
	        		raw_data = input("Do you want to see raw trip data? Enter <Yes> or <No>")
	        		raw_data = raw_data.lower()

	        
	        restart = input('\nWould you like to restart? Enter yes or no.\n')
	        if restart.lower() != 'yes':
	            break


if __name__ == "__main__":
	main()
