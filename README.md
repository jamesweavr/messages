Using Whats App's ability to export messages, I was able to parse and decode the message data and metadata to determine different aspects of th data. The form of the expoerted data is largley unparseable so regex are created to better split into data vs metadata. Once the text file has been cleaned to better parse, the metadata is collected into two dictionaries that correspond to who sent the text message. Within each dictionary is a date and a counter for the number of texts sent that day. Finally the actual text messages are parsed by individual words, after cleaning them of any non alphanumeric characters.

I completed this project because I missed a friend and wanted to calculate the amount of time we spent texting when we were apart.

**All chat before message at "9/21/18, 04:33" is in Denmark Time Zone
