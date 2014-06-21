#Pagination

You can request paginated data back from the API. This is useful when building mobile applications and needing to limit the amount of data that the API sends back. Or to simply sync up from the most recent message in an application's cache.
    
## Query Parameters

The following query parameters are avaliable

Parameter | Description
--------- |  -----------
max       | The maximum number of returned entries
before    | Get posts before this timestamp
first     | ??? is this a date and what format???
last      | ??? is this a date and what format???
after     | Return only entries older than the entry with the specified ID.
index     | The element's (for example, a post) position in the result set