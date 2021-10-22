import json
from function_projet import convertJSON
from statistic_adam import count_browser
#convertJSON("access.log")

print(count_browser("access.json"))
