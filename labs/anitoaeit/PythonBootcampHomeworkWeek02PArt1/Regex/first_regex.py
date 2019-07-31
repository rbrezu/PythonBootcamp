import re


emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

desired_output = [('zuck26', 'facebook', 'com'),
                  ('page33', 'google', 'com'),
                  ('jeff42', 'amazon', 'com')]

print(re.findall('(\w+)@(\w+)\.(\w+)', emails))