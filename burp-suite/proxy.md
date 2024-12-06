# Burp Suite Proxy

It enables the capture of requests and responses between the user and the target web server. This intercepted traffic can be manipulated, sent to other tools for further processing, or explicitly allowed to continue to its destination.

Intercepting requests is the way that you force the [FoxyProxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-basic/) to actually push the request to Burp Suite before pushing it to the server. This will allow you to capture structure of the API calls so that they can be forwarded to other modules for inspection or attacking.


Once you have installed Burp it's important to allow browser to run in Sandbox environments if you're in an environment that is isolated. You enable this by going to the Settings Gear > Tools > Burps Browser and then there's a checkbox to enable the Browser to run in SBX envs.

## Scoping
This is what THM recommends is probably the most important part of Proxy especially when you have a scope of work for a PenTest. You must use the Scoping capability to ensure that you only proxy and forward specific target sites so that you're not overwhelmed with the sheer number of requests that could happen on busy sites.

To do this you go to the Target Tab and in the left hand side you will see a list of sites/URLs that you can choose from. Pick the one that's relevant to you you and right click on it and then select "Add to scope". Once you do that you'll need to also add a condition to the Scoping rules by going to the Proxy settings and in the "Request Interception Rules" tab you add new rule that meets the following criteria:
Operator = AND
Match Type = URL
Relationship = Is in target scope