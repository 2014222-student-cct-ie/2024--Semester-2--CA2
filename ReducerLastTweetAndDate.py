#!/usr/bin/env python3


# Last tweet and date for each unique key (which could be interpreted as a user ID or a session ID),
# the process helps in tracking when a user last tweeted.
# Helps in understanding user engagement patterns and identifying active and inactive users.
# Helps in understanding what types of content are being posted at specific times.
# Helps in further analysis to the final tweets to assess sentiment trends or shifts over time.

import sys

# Initialize variables to hold tweet data, old key for comparison, and date.
current_tweet = None
previous_key = None
current_date = None

# Process each line from standard input.

for line in sys.stdin:
    # Strip the line of leading/trailing whitespace and split by comma.
    parts = line.strip().split(",")
    
    # Ensure the line has exactly three parts: key, date, and tweet.
    if len(parts) != 3:
        
        # Skip lines that do not have exactly three parts.
        continue

    key, date, tweet = parts

    # When encountering a new key, output the previous key and its associated data.
    if previous_key and previous_key != key:
        print(f"{previous_key},{current_date},{current_tweet}")
        
        # Reset the data for the new key.
        current_tweet = tweet
        current_date = date
    else:
        # Update the tweet and date for the current key.
        current_tweet = tweet
        current_date = date

    # Update the previous key to be the current key.
    previous_key = key

# Output the last processed key's data.
if previous_key:
    print(f"{previous_key},{current_date},{current_tweet}")


