# SpamWatch API Python Wrapper
# Basic Usage
```python
import spamwatch
token = 'A_LONG_TOKEN_HERE'
client = spamwatch.Client(token)
ban = client.get_ban(777000)
print(ban.reason)
```
