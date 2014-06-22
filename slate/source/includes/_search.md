#Search

You can search for authors, metadata, channels, and channel content.

There are two search services on Buddycloud that are tuned for different needs,
- *Local search:* finds content on your own Buddycloud domain.
- *Buddycloud-wide search:* finds channels, posts and metadata from open channels using the [Buddycloud crawler](https://github.com/buddycloud/channel-directory).

Local search 
???Lloyd - could you pleae write a quick description of this???

Search type      | Local search | Buddycloud-wide search
-----------------|--------------|------------------------
Channel content  | open and private channels | open channels
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
