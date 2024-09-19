import time
import pandas as pd
import numpy as np

# start original project >>>
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # <<< end original project
    
    # start my code here:
    while True:
        city = input("\nWould you like to filter by Chicago, New York City, or Washington? Please input here:\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city selection! Please choose Chicago, New York City, or Washington.")
    # <<< end my code
    
    # start original project >>>
    # TO DO: get user input for month (all, january, february, ... , june)
    # <<< end original project
    
    # start my code here:
    while True:
        month = input("\nWould you like to filter by January, February, March, April, May, June, or all? Please input here:\n").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month selection! Please choose January, February, March, April, May, June, or all.")
    # <<< end my code
    
    # start original project >>>
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # <<< end original project
    
    # start my code here:
    while True:
        day = input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday or all? Please input here:\n").lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print("Invalid day name! Please choose a valid day or all.")
    # <<< end my code
    
    # start original project >>>
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
    # <<< end original project
    
    # start my code here:
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    # <<< end my code
    
    # start original project >>>
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # <<< end original project
    
    # start my code here:
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
    # <<< end my code
    
    # start original project >>>
    # TO DO: display the most common day of week
    # <<< end original project
    
    # start my code here:
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)
    # <<< end my code
    
    # start original project >>>
    # TO DO: display the most common start hour
    # <<< end original project
    
    # start my code here:
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)
    # <<< end my code
    
    # start original project >>>
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # <<< end original project
    
    # start my code here:
    start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', start_station)
    # <<< end my code
    
    # start original project >>>
    # TO DO: display most commonly used end station
    # <<< end original project
    
    # start my code here:
    end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', end_station)
    # <<< end my code
    
    # start original project >>>
    # TO DO: display most frequent combination of start station and end station trip
    # <<< end original project
    
    # start my code here:
    df['start_end_combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_combination = df['start_end_combination'].mode()[0]
    print('Most Common Start-End Station Combination:', common_start_end_combination)
    # <<< end my code
    
    # start original project >>>
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # <<< end original project
    
    # start my code here:
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # <<< end my code
    
    # start original project >>>
    # TO DO: display mean travel time
    # <<< end original project
    
    # start my code here:
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    # <<< end my code
    
    # start original project >>>
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # <<< end original project
    
    # start my code here:
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)
    # <<< end my code
    
    # start original project >>>
    # TO DO: Display counts of gender
    # <<< end original project
    
    # start my code here:
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_counts)
    else:
        print('\nNo gender data available.')
    # <<< end my code
    
    # start original project >>>
    # TO DO: Display earliest, most recent, and most common year of birth
    # <<< end original project
    
    # start my code here:
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('\nNo birth year data available.')
    # <<< end my code
    
    # start original project >>>
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    while True:
        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no:\n").lower()
        
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
        elif view_data == 'no':
            break
        else:
            print("Invalid input! Please enter yes or no.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)
            
        restart = input('\nRestart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
# <<< end original project