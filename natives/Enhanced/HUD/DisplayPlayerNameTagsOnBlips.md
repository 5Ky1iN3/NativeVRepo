# _DISPLAY_PLAYER_NAME_TAGS_ON_BLIPS

--- ns: HUD aliases: ["0x82CEDC33687E1F50"] --- ## DISPLAY_PLAYER_NAME_TAGS_ON_BLIPS  // 0x82CEDC33687E1F50 0x2F28F0A6 void DISPLAY_PLAYER_NAME_TAGS_ON_BLIPS(BOOL toggle);  Toggles whether or not name labels are shown on the expanded minimap next to player blips, like in GTA:O. Doesn't need to be called every frame. Preview: https://i.imgur.com/DfqKWfJ.png Make sure to call SET_BLIP_CATEGORY with index 7 for this to work on the desired blip.  ## Parameters * **toggle**: the toggle boolean

### Parameters
* BOOL toggle

### Return Value
* void

### Notes
* AP Hash: 0x0x2F28F0A6
* Build: 811
* Toggles whether or not name labels are shown on the expanded minimap next to player blips, like in GTA:O.
Doesn't need to be called every frame.
Preview: https://i.imgur.com/DfqKWfJ.png

Make sure to call SET_BLIP_CATEGORY with index 7 for this to work on the desired blip.

