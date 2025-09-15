# __NET_GAMESERVER_FLAG_FOR_SESSION_RESTART

No description available.

### Return Value
* BOOL

### Notes
* Build: 812
* Instructs the transaction session manager to perform a session restart as soon as possible.
This is different from NET_GAMESERVER_START_SESSION_RESTART which, despite its name, does not actually restart the session (it only requests fresh inventory and/or balance data from the server).
Returns true if it was possible to set the flag.

