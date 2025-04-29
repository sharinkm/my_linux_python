# Write a script or one-liner to:

# Extract the IP address, HTTP method, URL, and status code.

# Normalize HTTP method to lowercase.

# Filter only requests that resulted in client or server errors (4xx or 5xx status codes).

# Output in CSV format: ip,method,url,status

# Example output: 10.0.0.5,post,/login,403

#!/bin/bash
# Check if the input file is provided


grep '"[A-Z]\+ [^"]\+" [45][0-9][0-9]' access.log | \
  sed -E 's/^([0-9\.]+).*\] "([A-Z]+) ([^ ]+) HTTP\/[^"]+" ([0-9]{3}).*/\1,\2,\3,\4/' | \
  awk -F',' '{ printf "%s,%s,%s,%s\n", $1, tolower($2), $3, $4 }'

