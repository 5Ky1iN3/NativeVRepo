# _SET_VEHICLE_ON_GROUND_PROPERLY

--- ns: VEHICLE --- ## SET_VEHICLE_ON_GROUND_PROPERLY  // 0x49733E92263139D1 0xE14FDBA6 BOOL SET_VEHICLE_ON_GROUND_PROPERLY(Vehicle vehicle);  Sets a vehicle on the ground on all wheels.  Returns whether or not the operation was successful.  NativeDB Added Parameter 2: float p1  ## Parameters * **vehicle**:  ## Return value

### Parameters
* Vehicle vehicle
* float p1

### Return Value
* BOOL

### Notes
* AP Hash: 0x0xE14FDBA6
* Build: 811
* Sets a vehicle on the ground on all wheels.  Returns whether or not the operation was successful.

sfink: This has an additional param(Vehicle vehicle, float p1) which is always set to 5.0f in the b944 scripts.

