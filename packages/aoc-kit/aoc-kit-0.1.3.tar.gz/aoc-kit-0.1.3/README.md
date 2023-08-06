# Advent Of Code kit

A supportive lib for advent of code challenges.


## Getting started

Make sure to add `AOC_TOKEN` to your .env file.
(You can find the token in your cookies when browsing on advendofcode.com)

## Example

```
from aockit import get_input

def process(data):
    return 'implement me'

data = get_input(2015, 1)
result = process(data)
print(result)
```
