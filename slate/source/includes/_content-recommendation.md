#Content Recommendation

You can increase user engagement in your app by using the results of the recommended, similar and popular channel query.

This is useful if a user has just started using your buddycloud App. You can now show them popular channels across all Buddycloud enabled sites, or limit the scope to just popular channels on your Buddycloud site.

Based on what channels a user follows, the recommendation service will then suggest other channels that they might be interested in.

It is also possible to query for similar channels to a channel. For example, querying for similar channels to football@example.com might return, worldcup@example.org and fifa-scandal@other-domain.com.

<aside>Federated Buddycloud sites are crawled for a list of channels and followers. The crawler builds a social graph that can then be queried.</aside>


##Recommend Channels

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

Returns a list of recommended channels based on the channels that the user already follows.

### HTTP Request
`POST https://demo.buddycloud.org/api/????` 

##Similar Channels

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

Returns a list of channels similar to the queried channel.

### HTTP Request
`POST https://demo.buddycloud.org/api/????` 

##Popular Channels
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

Returns a list of popular channels ???@abmar: how do we calculate popularity??? both on the local buddycloud domain, or across all buddycloud sites.

### HTTP Request
`POST https://demo.buddycloud.org/api/????` 
