# Important
Tinyurl : basics
Instagram,
Twitter, Twitter TOP TRENDING, Twitter Newsfeed, Twitter search
# Facebook Newsfeed
# Facebook Messenger/Whatsapp
1. Common features:
1) Support one-on-one conversation between users...
2) Keep track of online/offline statuses
3) ME - Sent/Delivered/Read(Seen)
4) Persistent storage of chat history (whats app or snap might be 24hours)
5) Group chats (Whats app)
6) Push notification (notify users of new messages when they are offline?)
7) ME - Send images, audio... Not yet. One at a time

Non functional requirements:
1) ME - Read and write heavy
2) Real time with minimum latency
3) Highly consistent (should see same chat history on all their device)
4) High availability is desirable, tolerate lower availability in exchange of consistency

2. Capacity. Idk if we should focus on this...
500 million DAU, 40 messages daily, 20 billion messages a day
Storage: ...
Bandwith: ... 25mb/s incoming and outgoing (how to estimate this)
Can you give me an estimation on how its going to be used?

3. High Level
... see drawing ...

4. Detailed Component Design
*Try on one server first*
  1. Receive incoming message, deliver outgoing message
  2. Store and retrieve messages from the database
  3. Keep a record of which user is online/has gone offline?

A. Message Handling...
1) Pull model. User long-poll for new things
2) Push model. Keep an open connection with server (web sockets). Server can just notify if there is an open connection.

First approach: Waste a lot of resource, not very efficient. Serve might not respond immediately even if constantly requested.
Long polling... (web sockets) - only respond when theres something new.

How can the server keep track of opened connection? How does it know how to redirect?
Server -> hash table. Key would be uid, value is the connection object.

What happen when the server receives a message for user who has gone offline?
Gone offline -> no open connection. Retry sending...?

Let say modern server can handle 50k CONCURRENT connections...? wtf
Then we need 10k of such servers.

How do we know which server holds what to which user?
Gateway. User A -> Gateway -> route to appropriate server

How should the server process a deliver message?
Upon getting the message:
  - Store the message in DB
  DB design for message... (mysql)
  - Send message to receiver
  - Send ack to sender

How does the messenger maintain sequencing of the messages?
Timestamp with each message. Client side can render?

B. Storing and Retrieving Messages from DB
Cache last 30 messages for a particular user.
Inactive user: Retrieve (long...) -> cache -> Every new one also update cache

User sends small incremental messages (chat system)
Storage needs: 1) huge number of small message insertions, sequential data

Wide-column database soln : Cassandra, BigTable, HBase...

C. Managing User's Status
Broadcast system.
- Client starts app. Pull Current status of all users in their friend's list (Maybe not all but only last 30 users chatted with)
**Come back to this**

5. Fault Tolerance
What happened when a chat server fails...
No failovers. Just let users reconnect if the connection is lost.


Like twitter, store multiple copies of user messages.



Yelp : Nearby friends

Consistent Hashing.



Misc:
  - Typeahead (ala Google)
  - API Rate Limiter

Messaging

Image Service/Storage

Newsfeed Generation

Gateway




Small Features:
- Following, talk about DB


Make sure everyone is following along.
Do you guys have any question about me doing this?
