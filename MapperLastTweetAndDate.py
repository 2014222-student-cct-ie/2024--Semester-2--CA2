#!/usr/bin/env python3

# By capturing the last tweet and date for each unique key (which could be interpreted as a user ID or a session ID), the process helps in tracking when a user last tweeted.
# Helps in understanding user engagement patterns and identifying active and inactive users.
# Helps in understanding what types of content are being posted at specific times.
# Helps in further analysis to the final tweets to assess sentiment trends or shifts over time.

import sys

# Process each line from the standard input
for line in sys.stdin:
    # Clean up the line and split by comma
    fields = line.strip().split(",")
    fields_count = len(fields)

    # Check the number of elements in the split line
    if fields_count == 6:
        # Unpack all fields directly if they match the expected count
        num, tweet_id, date, query, username, tweet = fields
        output = f"{num},{date},{tweet}"
    elif fields_count > 6:
        # Extract fields directly using indices; concatenate extra tweet parts
        num = fields[0]
        date = fields[2]
        tweet = ' '.join(fields[5:])  # Join the rest of the fields as part of the tweet
        output = f"{num},{date},{tweet}"

    # Print the formatted output
    print(output)

