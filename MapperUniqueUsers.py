#!/usr/bin/env python3

# Count Unique Users Posting Tweets
# Knowing the count of unique users posting tweets is crucial for several reasons,
# especially in contexts such as social media analysis, marketing, public opinion measurement, # and platform health monitoring.

# Counting unique users posting tweets provides valuable insights into user engagement levels,
# helps tailor marketing efforts, assesses content impact, informs strategic decisions,
# and aids in regulatory compliance. 

import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    if len(columns) > 3:
        user = columns[3]  # Assuming the user ID is in the fourth column
        print(f"{user}\t1")





