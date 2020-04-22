import time
import pandas as pd
import numpy as np
import collections as co

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#change the user input 'month' from string to integer in order to filter for a certain month
def month_string_to_number(string):
    m = {
        'january': 1,
        'febuary': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october':10,
        'november':11,
        'december':12
        }
    s = string.lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

#change the user input 'day' from string to integer in order to filter for a certain day in the dataframe
def day_string_to_number(string):
    m = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
        }
    s = string.lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a day')

#user prompt to display the first five rows of the dataframe
def display_data(df):
    see_data = ''
    n = 0
    m = 5
    try:
        while see_data != 'no':
            see_data = input('do you want to see the (next) five lines of raw data? answer \'yes\' or \'no\': ')
            if see_data == 'yes':
                print(df.loc[n:m,:])
                n += 5
                m += 5
    except ValueError as e:
            print("ValueError occurred: {}".format(e))

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =''
    print('Hello! Let\'s explore some US bikeshare data!\nPlease note to provide your input in lower case letters.')
    while city not in {'chicago','new york city','washington'}:
        city = input('Please enter one of the cities chicago, new york city, or washington: ')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in {'all','january','february','march','april','may','june','july','august','september','october','november','december'}:
        month = input('Please enter a month or \'all\' if you don\'t want to specify the month: ')
        month = month.lower()

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    while day not in {'all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'}:
        day = input('Please enter a day of the week or \'all\' if you don\'t want to specify the day: ')
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
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    if month == 'all':
        print('month: all')
    else:
        print('month: ' + str(month))
        df = df.loc[df['month'] == month_string_to_number(month)]
    if day == 'all':
        print('day: all')
    else:
        print('day: ' + day)
        df = df.loc[df['day'] == day_string_to_number(day)]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_counter = co.Counter(df['month'])
    most_common_month = month_counter.most_common(1)
    print('most common month (e.g. 1=january, 6=june) with number of occurences: ')
    print(most_common_month)
    print('')

    # TO DO: display the most common day of week
    day_counter = co.Counter(df['day'])
    most_common_day = day_counter.most_common(1)
    print('most common day of the week (e.g. 0=monday, 6=sunday) with number of occurences: ')
    print(most_common_day)
    print('')

    # TO DO: display the most common start hour
    hour_counter = co.Counter(df['hour'])
    most_common_hour = hour_counter.most_common(1)
    print('most common hour (24h) with number of occurences: ')
    print(most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_counter = co.Counter(df['Start Station'])
    most_common_start = start_counter.most_common(1)
    print('most common start station with number of occurences: ')
    print(most_common_start)
    print('')

    # TO DO: display most commonly used end station
    end_counter = co.Counter(df['End Station'])
    most_common_end = end_counter.most_common(1)
    print('most common end station with number of occurences: ')
    print(most_common_end)
    print('')

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' >>> ' + df['End Station']
    start_end_counter = co.Counter(df['Station Combination'])
    most_common_start_end = start_end_counter.most_common(1)
    print('most common start/end combination with number of occurences: ')
    print(most_common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('total travel time in hours: ')
    print(total_trip_duration//3600)
    print('')
    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('mean travel time in minutes: ')
    print(mean_trip_duration//60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #exception if the dataframe filtered by the user is empty
    try:
        # TO DO: Display counts of user types
        df['User Type'] = df['User Type'].fillna('not specified')
        user_type_count = df.groupby(['User Type'])['User Type'].count()
        print('counts of user types: ')
        print(user_type_count)
        print('')
        # TO DO: Display counts of gender
        df['Gender'] = df['Gender'].fillna('not specified')
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print('counts of gender: ')
        print(gender_count)
        print('')

        # TO DO: Display earliest, most recent, and most common year of birth
        most_early = df['Birth Year'].min()
        print('earliest year of birth: ')
        print(int(most_early))
        print('')

        most_recent = df['Birth Year'].max()
        print('most recent year of birth: ')
        print(int(most_recent))
        print('')

        birth_year_counter = co.Counter(df['Birth Year'].dropna())
        most_common_birth_year = birth_year_counter.most_common(1)
        print('most common birth year with number of occurences: ')
        print(most_common_birth_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except ValueError as e:
            print("ValueError occurred: {}".format(e))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
