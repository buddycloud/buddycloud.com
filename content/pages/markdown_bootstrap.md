Title: Test -> Convertion from Markdown-Bootstrap syntax
url: markdown_bootstrap_test
save_as: markdown_bootstrap_test.html

{@
{@[JSON GET]}
{@[JSON POST]}
{@[XML]}
@}
{{@
{{@[JSON GET]

~~~~ bash
GET /alice@examle.com/content/posts
Accept: application/json
~~~~

~~~~ javascript
200 OK
Content-Type: application/json

[
  {
    "id": "foo",
    "author": "alice@example.com",
    "updated": "2012-06-01T12:00:00Z",
    "content": "This is my newest post!",
    "media": null
  },
  {
    "id": "bar",
    "author": "alice@example.com",
    "updated": "2012-05-31T12:00:00Z",
    "content": "June starts tomorrow.",
    "media": null
  },
  {
    "id": "baz",
    "author": "alice@example.com",
    "updated": "2012-05-30T12:00:00Z",
    "content": "Feeling good today!",
    "media": [{"id": "qwe", "channel": "alice@example.com"}]
  }
]
~~~~

/@}}
{{@[JSON POST]

~~~~ javascript
POST /bob@example.com/content/posts
Authorization: Basic Ym9iQGV4YW1wbGUuY29tOmJvYg==
Content-Type: application/json

{
  "content": "Hello JSON!"
}
~~~~

~~~~ xml
201 Created
Location: http://api.example.com/bob@example.com/content/posts/bipp
~~~~

/@}}
{{@[XML]

Retrieve all posts from "alice@example.com":

~~~~ bash
GET /alice@example.com/content/posts
~~~~

~~~~ xml
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Alice's posts</title>
  <entry>
    <id>foo</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-06-01T12:00:00Z</published>
    <content>This is my newest post!</content>
  </entry>
  <entry>
    <id>bar</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-05-31T12:00:00Z</published>
    <content>June starts tomorrow.</content>
  </entry>
  <entry>
    <id>baz</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-05-30T12:00:00Z</published>
    <content>Feeling good today!</content>
    <media>
       <item id="qwe" channel="alice@example.com"/>
    </media>
  </entry>
</feed>
~~~~

Retrieve the newest post from "alice@example.com":

~~~~ bash
GET /alice@example.com/content/posts?max=1
~~~~

~~~~ xml
200 OK
Content-Type: application/atom+xml

<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Alice's posts</title>
  <entry>
    <id>foo</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-06-01T12:00:00Z</published>
    <content>This is my newest post!</content>
  </entry>
</feed>
~~~~

Get the two newest posts that are older than the one retrieved above:

~~~~ bash
GET /alice@example.com/content/posts?max=2&after=foo
~~~~

~~~~ xml
200 OK
Content-Type: application/atom+xml

<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Alice's posts</title>
  <entry>
    <id>bar</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-05-31T12:00:00Z</published>
    <content>June starts tomorrow.</content>
  </entry>
  <entry>
    <id>baz</id>
    <author>
      <name>alice@example.com</name> 
      <id>acct:alice@example.com</id>
    </author>
    <published>2012-05-30T12:00:00Z</published>
    <content>Feeling good today!</content>
  </entry>
</feed>
~~~~

Add a post to "bob@example.com":

~~~~ xml
POST /bob@example.com/content/posts
Authorization: Basic Ym9iQGV4YW1wbGUuY29tOmJvYg==
Content-Type: application/atom+xml

<entry xmlns="http://www.w3.org/2005/Atom">
  <content>Hello World!</content>
</entry>
~~~~

~~~~ xml
201 Created
Location: http://api.example.com/channels/bob@example.com/posts/item?id=buux
~~~~

Comment on the newest post of "alice@example.com":

~~~~ xml
POST /alice@example.com/content/posts
Authorization: Basic Ym9iQGV4YW1wbGUuY29tOmJvYg==
Content-Type: application/atom+xml

<entry xmlns="http://www.w3.org/2005/Atom">
  <in-reply-to ref="foo" xmlns="http://purl.org/syndication/thread/1.0"/>
  <content>And this is my newest comment ;)</content>
</entry>
~~~~

~~~~ xml
201 Created
Location: http://api.example.com/alice@example.com/content/posts/fooboo
~~~~

/@}}
@}}

