# _IS_REPLAY_RECORDING

No description available.

### Return Value
* BOOL

### Notes
* Build: 811
* Checks if you're recording, returns TRUE when you start recording (F1) or turn on action replay (F2)

mov al, cs:g_bIsRecordingGameplay // byte_141DD0CD0 in b944
retn

