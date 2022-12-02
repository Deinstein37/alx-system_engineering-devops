0x19. Postmortem

Postmortem Report  

1.	Issue Summary:

On November 30th, 2022 at about 14:45 GMT: Website is unresponsive with a returned response code status 500 when trying to access the site through the browser or CURL command with GET method to IP address. 100% of the users internal or external were unable to access the webpage, it was not loading. At about 17:35 GMT, the root cause was discovered —One of the PHP file’s extension was spelled “.phpp”. At about 18:15 GMT deployed automated fixed using Puppet.


