#Pagination

The API can return paginated data back to your application. This is useful when:

* building mobile applications and needing to limit the amount of data that the API sends back. 
* your app needs to retrieve new messages since it was last online.
 
## Query Parameters

The following query parameters are available:

Parameter | Description
--------- |  -----------
`max`     | The maximum number of returned entries
`before`  | Get posts before this timestamp
`after`   | Return only entries older than the entry with the specified ID
`index`   | The element's position in the result set (for example: -----) **The description is confusing but I'm not sure how to re-word it**

## Response Attributes

The following attributes are returned in a paged query response:

Parameter | Description
--------- |  -----------
`count`   | The total number of entries that the query would return
`first`   | The ID of the first item in the page
`last`    | The ID of the last item in the page
