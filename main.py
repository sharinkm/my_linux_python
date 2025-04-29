import re

# Define log pattern
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\] "(?P<method>[A-Z]+) (?P<url>[^ ]+) HTTP/[^"]+" (?P<status>\d{3})'
)

# Open and parse the log file
with open('access.log', 'r') as log:
    for line in log:
        match = log_pattern.search(line)
        if match:
            status = int(match.group('status'))
            if 400 <= status < 600:  # Only 4xx and 5xx errors
                ip = match.group('ip')
                method = match.group('method').lower()
                url = match.group('url')
                print(f"{ip},{method},{url},{status}")

