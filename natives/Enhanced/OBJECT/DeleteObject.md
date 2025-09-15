# _DELETE_OBJECT

--- ns: OBJECT --- ## DELETE_OBJECT  // 0x539E0AE3E6634B9F 0xD6EF9DA7 void DELETE_OBJECT(Object* object);  Deletes the specified object.  **Note**: If for some reason the entity won't delete, you might want to check if the object is a mission entity.  NativeDB Introduced: v323  ## Parameters * **object**: The object you want to delete.  ## Examples local playerPed = PlayerPedId() local playerCoords = GetEntityCoords(playerPed) local objectHash = GetHashKey("v_ret_gc_chair03")  local object = GetClosestObjectOfType(playerCoords, 10.0, objectHash, true, false, false) if object == 0 then return end  -- If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object. if IsEntityAMissionEntity(object) then SetEntityAsMissionEntity(object, false, true) end  DeleteObject(object)  const playerPed = PlayerPedId(); const playerCoords = GetEntityCoords(playerPed, false); const objectHash = GetHashKey("v_ret_gc_chair03");  const object = GetClosestObjectOfType(playerCoords[0], playerCoords[1], playerCoords[2], 10.0, objectHash, true, false, false); if (object === 0) return;  // If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object. if (IsEntityAMissionEntity(object)) { SetEntityAsMissionEntity(object, false, true); }  DeleteObject(object);  using static CitizenFX.Core.Native.API;  int playerPed = PlayerPedId(); Vector3 playerCoords = GetEntityCoords(playerPed, false); uint objectHash = Game.GenerateHashASCII("v_ret_gc_chair03");  int prop = GetClosestObjectOfType(playerCoords.X, playerCoords.Y, playerCoords.Z, 10.0f, objectHash, true, false, false); if (prop == 0) return; // If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object. if (IsEntityAMissionEntity(prop)) { SetEntityAsMissionEntity(prop, false, true); }  DeleteObject(ref prop);

### Parameters
* Object* object

### Return Value
* void

### Notes
* AP Hash: 0x0xD6EF9DA7
* Build: 811
* Deletes the specified object, then sets the handle pointed to by the pointer to NULL.

