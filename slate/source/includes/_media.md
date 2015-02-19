#Media

File's inherit the permissions of the channel they are shared with. For example sharing files onto a private channel will mean that *only* that channel's followers can download them.

Media can be any type of file, and any file size (Buddycloud site administrators usually set about 1GB as a maximum size.)

<aside class="notice">Authentication is not required for requesting media from a public channel. Authentication is required for private channels.</aside>

###Special MediaIDs

The media `id` of `avatar` is currently reserved and used for storing a channels avatar. Uploading with the `avatar` `id` will replace the user's avatar.

## Media Metadata

```shell
#POST https://demo.buddycloud.org/api/{channelID}/media/{mediaID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -d '{ \
            "filename": "A good name for that picture of Jules", \
            "title": "A new title" \
        }' 

```

```javascript
#Unsupported Method









```

Metadata upates must include the `id`. 

The possible metadata parameters are:

Parameter        | Required   | Description
-----------------|------------|--------------------------------------------
`height`           | server-set | Height of the uploaded image or video. This is calculated by the server and not user-editable.
`width`            | server-set | Width of the uploaded image or video. This is calculated by the server and not user-editable.
`author`           | server-set | the `username` of the uploader
`shaChecksum`      | server-set | SHA1 file checksum
`uploadedDate`     | server-set | when the media was uploaded
`lastUpdatedDate`  | server-set | when the media was updated / re-uploaded
`mimeType`         | required   | The file mimetype (e.g. `image/jpeg`)
`fileName`         | required   | The uploaded filename and extension.
`entityId`         | required   | The channel where the media object was posted.
`title`            | optional   | a short title of the object
`description`      | optional   | a longer form description of the object



##List Media

```shell
#GET https://demo.buddycloud.org/api/{channelID}/media

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media \
     -X GET

#Response would be as follows:

200 OK
Content-Type: application/json

[
    {
        "id": "lETuJi8rPE4IfQrygN8rVtGx3",
        "fileName": "photo.jpg",
        "author": "juliet@buddycloud.org",
        "title": "Juliet's pic",
        "mimeType": "image/jpeg",
        "description": "Juliet's picture 1595/06/01",
        "fileExtension": "jpg",
        "shaChecksum": "bc46e5fac2f1cbb607c8b253a5af33181f161562",
        "fileSize": "60892",
        "height": "312",
        "width": "312",
        "entityId": "capulet@topics.buddycloud.org"
    }
]
```

```javascript
#Unsupported Method

























```

This returns a list of all avaliable media objects in a channel.

##Fetch Media

```shell
#Get media:
#GET https://demo.buddycloud.org/api/{channelID}/media/{mediaID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID \
     -X GET


#Or get media preview:
#GET https://demo.buddycloud.org/api/{channelID}/media/{mediaID}?maxheight=:x&maxwidth=:x

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID?maxheight=150&maxwidth=150 \
     -X GET


#Or get avatar:
#GET https://demo.buddycloud.org/api/{channelID}/avatar

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/avatar \
     -X GET
```

```javascript
#Unsupported Method


















```

This request returns a media file.

The request can also be used to return an image preview or small user avatar sized files by adding the `maxheight` and `maxwidth` parameter to the request.

If the media object belongs to a public channel, you don't need an Authorization header. Notice that if you're building a web frontend, embedding public media from the media-server means just creating an ```<img>``` tag.

Parameter        | Required   | Description
-----------------|------------|--------------------------------------------
`maxheight`      | optional   | Bound the ouput by a maximum height
`maxwidth`       | optional   | Bound the output by a maximum width

When both `maxheight` and `maxwidth` are requested the server will return a file smaller than or equal to both parameters.

##Post Media

```shell
#POST https://demo.buddycloud.org/api/{channelID}/media

curl https://demo.buddycloud.org/api/capulet@topics.buddycloud.org/media \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ \
             "data": "media data in bytes", \
             "content-type": "image/png", \
             "filename": "prom.png", \
             "title": "Juliet's prom pic", \
             "description": "Juliet's beautiful prom pic!" \
         }'

#Response would be as follows:

201 Created
Content-Type: application/json

{
    "id": "lETuJi8rPE4IfQrygN6rVtGx3",
    "fileName": "prom.png",
    "author": "juliet@buddycloud.org",
    "title": "Juliet's prom pic",
    "mimeType": "image/png",
    "description": "Juliet's beautiful prom pic!",
    "fileExtension": "png",
    "shaChecksum": "bc46e5fac2f1cbb607c8b253a5af33181f161562",
    "fileSize": 60892,
    "height": 312,
    "width": 312,
    "entityId": "capulet@topics.buddycloud.org"
}
```

```javascript
#Unsupported Method
































```

This call enables media and media-metadata uploading and modification.

Posting new media will return the object `id` and metadata.

Updating existing media with the same `id` will overwrite the existing media content.


##Delete Media
```shell
#DELETE https://demo.buddycloud.org/api/{channelID}/media/{mediaID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID \
     -x DELETE \
     -u juliet@buddycloud.org:romeo-forever





```

```javascript
#Unsupported Method









```

Removes media from the channel.

Deleting media will remove it from the requested channel. This does not remove it from other channels where it has been reshared.
