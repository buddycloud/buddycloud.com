#Search

You can query all public channels on all federated Buddycloud servers. You can also perform more specific searches for content on your local Buddycloud server. 

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

New posts are crawled and should show up in search results after a few minutes. This will return public posts.

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

Query for a specific user's posts.

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

Query for channels by metadata.

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

Query for channels by location. This search will return channels nearby to a latitude and longitude.

<aside>Channels [#Update Metadata] can optionally be tagged with a latitude and a longitude.</aside>

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
