#Search

There are two search services on Buddycloud:
- *Local search* that references content on your buddycloud site.
- *Remote search* that [crawls public channels](https://github.com/buddycloud/channel-directory) on all buddycloud sites for channel content and channel metadata.

Local search 
???Lloyd - what does this do???

Search type      | Local search | Buddycloud-wide search
-----------------|--------------|------------------------
Channel content  | avaliable for open and closed channels on local Buddycloud site | only posts in an open channel but on all Buddycloud sites
Post author  | yes | no
Channel metadata | yes | yes
Location / Nearby | no  | yes

##Search by Content
```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

This enables searching for new posts. New posts are crawled and should show up in search results after a few minutes.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Search by Author
```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```
You can query by a user's BuddycloudID to return a list of their posts.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`


##Search by Metadata

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

This query will return channels matching the requested metadata. 

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Search by Location

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

Channels can optionally be tagged with a latitude and a longitude. This search will return channels nearby to a latitude and longitude.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
