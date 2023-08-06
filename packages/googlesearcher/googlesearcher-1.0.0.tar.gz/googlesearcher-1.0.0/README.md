## Usage:

```
from googlesearcher import *
results = Google.search(query, num="10")
for result in results:
    print(result.link)
    print(result.title)
    print(result.domain)

```
