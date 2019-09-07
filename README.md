# simple-chat
#### Implementation of a simple chat with socket library.
Server start two theards. one for send broadcast message and one for listen.
if there is a client that receive a broadcast message it open a tcp connection that they can chat.
chat continue until one of them enter "end"
