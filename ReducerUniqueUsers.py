#!/usr/bin/env python3

# Count Unique Users Posting Tweets
# Count Unique Users Posting Tweets
# Knowing the count of unique users posting tweets is crucial for several reasons,
# especially in contexts such as social media analysis, marketing, public opinion measurement, # and platform health monitoring.

# Counting unique users posting tweets provides valuable insights into user engagement levels,
# helps tailor marketing efforts, assesses content impact, informs strategic decisions,
# and aids in regulatory compliance.

import sys

current_user = None
user_set = set()

for line in sys.stdin:
    line = line.strip()
    user, _ = line.split('\t', 1)

    if user not in user_set:
        user_set.add(user)

print(f'Unique Users\t{len(user_set)}')




