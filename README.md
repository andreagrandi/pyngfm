# pyngfm

PyngFM is a Python implementation of Ping.fm API. Ping.fm is a simple service that allow you to update multiple social networks with a single post.

## Documentation

### Methods

* **PyngFM.system_services()** - Description: return a complete list of supported services.

* **PyngFM.user_key()** - Description: Will exchange a mobile application key for a functional application key. This is for mobile apps that would offer an easier way of authenticating users. Parameters: mobile_key - Mobile application key. (Users can be prompted to get their key here: http://ping.fm/key/)

* **PyngFM.user_validate()** - Description: Validates the given user's application key.

* **PyngFM.user_services()** - Description: Returns a list of services the particular user has set up through Ping.fm.

* **PyngFM.user_triggers()** - Description: Returns a user’s custom triggers.

* **PyngFM.user_latest()** - Description: Returns the last 25 messages a user has posted through Ping.fm. Parameters: limit - Limit the results returned, default is 25 (optional). order - Which direction to order the returned results by date, default is DESC (optional) 

* **PyngFM.user_post()** - Description: Posts a message to the user’s Ping.fm services. Parameters: 
post_method - Posting method. Either "default", "blog", "microblog" or "status."
body - Message body
title - Title of the posted message. This will only appear if the specified service supports a title field. Otherwise, it will be discarded. Title is required for "blog" post method (optional)
service - A single service to post to. This used to support multiple services separated by a comma. Posting to multiple services has been deprecated as of June 2008. Posting to a single service is still functional (optional).
location - The user's current location (optional).
media - base64 encoded media data (optional).
encoding - Set to "base64" to have the API decode before posting. Useful when posting unicode or non URL encoded data. If set, "title", "body" and "location" parameters are expected to be base64 encoded (optional).
exclude - comma separated values of service IDs (IDs returned from user.services, user.triggers, user.latest and system.services) to exclude from the post (optional).
debug - Set this value to "1" to avoid posting test data (optional).
checksum - Set this variable to pass a data checksum to confirm that the posted data reaches the API server. Please read the section titled "Payload Checksums" above (optional).

* **PyngFM.user_tpost()**
Description: Posts a message to the user’s Ping.fm services using one of their custom triggers. Parameters: 
trigger - Custom trigger the user has defined from the Ping.fm website.
body - Message body
title - Title of the posted message. This will be required if the custom trigger is set up with the "blog" method. If so, and the title is not present, an error will be returned (optional).
location - The user's current location (optional).
media - base64 encoded media data (optional).
encoding - Set to "base64" to have the API decode before posting. Useful when posting unicode or non URL encoded data. If set, "title", "body" and "location" parameters are expected to be base64 encoded (optional).
exclude - comma separated values of service IDs (IDs returned from user.services, user.triggers, user.latest and system.services) to exclude from the post (optional).
debug - Set this value to "1" to avoid posting test data (optional).
checksum - Set this variable to pass a data checksum to confirm that the posted data reaches the API server. Please read the section titled "Payload Checksums" above (optional).
Code Examples

## Posting a message to Ping.fm

```
from pyngfm import PyngFM

pfm = PyngFM()

pfm.setApiKey('****************************')
pfm.setUserAppKey('*************************************************')

pfm.user_post('status','testing Ping.FM Python API :)')
```
