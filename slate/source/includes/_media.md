#Media

The media server helps you add media sharing to channels. Users can upload a file to a channel and this is then shared with the followers of that channel. Only users that follow this channel can access the media. 

Media can be any type of file, and any file size (Buddycloud site administrators usually set about 10GB as a maximum size.)

<aside class="notice">Authentication is not required for requesting media from a public channel. Authentication is required for private channels.</aside>

Media Metadata

Parameter        | Required   | Description
-----------------|------------|--------------------------------------------
height           | server-set | Height of the uploaded image or video. This is calculated by the server and not editable.
width            | server-set | Hidth of the uploaded image or video. This is calculated by the server and not editable.
author           | server-set | the ID of the uploader
shaChecksum      | server-set | SHA1 file checksum
uploadedDate     | server-set | when the media was uploaded
lastUpdatedDate  | server-set | when the media was updated
mimeType         | required   | The file mimetype (??? for example???)
fileName         | required   | The uploaded filename and extension.
entityId         | required   | The channel where the media object was posted.
title            | optional   | a short title of the object
description      | optional   | a longer form description of the object

##List Objects

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media \
     -X GET
```
```shell
200 OK
Content-Type: application/json

{{
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
}}
```

```javascript```
???
???
```

This returns a list of all avaliable media objects in a channel.

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name/media`

##Fetch Object

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID \
     -X GET

-OR- (get media preview)

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/media/$MEDIA_ID?maxheight=150&maxwidth=150 \
     -X GET

-OR- (get avatar)

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/avatar \
     -X GET
```

```javascript```
???
???
```

This request returns a media file.

The request can also be used to return an image preview or small user avatar sized files.

Parameter        | Required   | Description
-----------------|------------|--------------------------------------------
maxheight        | optional   | Bound the ouput by a maximum height
maxwidth         | optional   | Bound the output by a maximum width

When both `maxheight` and `maxwidth` are requested the server will return a file smaller than or equal to both parameters.

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name/media/:media-id?maxheight=:x&maxwidth=:x`

##Post Media

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

Enables media file and metadata uploading and modification. 

Posting new media will return the object `id` and metadata.

Updating existing media with the same `id` will overwrite the existing media content.


### HTTP Request
`POST https://demo.buddycloud.org/api/channel@topics.domain.com/media`

##Special MediaIDs
 
 
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

The media `id` of `avatar` is currently reserved and used for storing a channels avatar.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Media Metadata

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

Metadata upates must include the `id`. 

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Delete Media
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

Deleting media will remove it from the requested channel. This does not remove it from other channels where it has been reshared.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
