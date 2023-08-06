# PyMemo

Simple Python **memoization** library. Decrease your app's response time!

## Installation

```sh
pip install pymemo-cache
```

## Usage

```python
from pymemo import PyMemo


memo = PyMemo()

# Creates collections with optional expiration interval
articles_cache = memo.create_collection('articles', expiration_interval=15) # Expires after 15 seconds
comments_cache = memo.create_collection('comments', expiration_interval=60) # Expires after 60 seconds
country_list_cache = memo.create_collection('countries') # Never expires

articles_cache.set_item('article-1', {'id': 1, 'title': 'Article Example'}) # Any data type
articles_cache.get_item('article-1') # -> {'id': 1, 'title': 'Article Example'}

# After 15 seconds
articles_cache.get_item('article-1') # -> None

# Set customized expiration interval for individual items
comments_cache.set_item('comment-1', {'id': 1, 'content': 'Lorem ipsum'}, expiration_interval=120) # Expires after 120 seconds instead of 60 seconds
```
