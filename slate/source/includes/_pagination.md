#Pagination

You can request paginated data back from the API. This is useful when building mobile applications and needing to limit the amount of data that the API sends back. Or to simply sync up from the most recent message in an application's cache.
    
## Query Parameters

The following query parameters are available

Parameter | Description
--------- |  -----------
max       | The maximum number of returned entries
before    | Get posts before this timestamp
after     | Return only entries older than the entry with the specified ID.
index     | The element's (for example, a post) position in the result set

## Response Attibutes

The following attributes are returned in a paged query response

Parameter | Description
--------- |  -----------
count     | The total number of entries that the query would return
first     | The ID of the first item in the page
last      | The ID of the last item in the page
