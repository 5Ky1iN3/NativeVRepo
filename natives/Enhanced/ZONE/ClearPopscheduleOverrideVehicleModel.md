# _CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL

--- ns: ZONE --- ## CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL  // 0x5C0DE367AA0D911C 0x7A72A24E void CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL(int scheduleId);  Only used once in the decompiled scripts. Seems to be related to scripted vehicle generators. Modified example from "am_imp_exp.c4", line 6418: /* popSchedules[0] = ZONE::GET_ZONE_POPSCHEDULE(ZONE::GET_ZONE_AT_COORDS(891.3, 807.9, 188.1)); etc. */ STREAMING::SET_MODEL_AS_NO_LONGER_NEEDED(vehicleHash); ZONE::CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL(popSchedules[index]);  ## Parameters * **scheduleId**:

### Parameters
* int scheduleId

### Return Value
* void

### Notes
* AP Hash: 0x0x7A72A24E
* Build: 811
* Only used once in the decompiled scripts. Seems to be related to scripted vehicle generators.

Modified example from "am_imp_exp.c4", line 6418:
/* popSchedules[0] = ZONE::GET_ZONE_POPSCHEDULE(ZONE::GET_ZONE_AT_COORDS(891.3, 807.9, 188.1));
etc.
*/
STREAMING::SET_MODEL_AS_NO_LONGER_NEEDED(vehicleHash);
ZONE::CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL(popSchedules[index]);

