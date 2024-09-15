value = ((({ "batters": { "batter": [ { "batter": [ { "batter": [{ "type": "Regular" }] }] }] } }).get("batters", {}).get("batter", [{}])[0].get("batter", [{}])[0].get("batter", [{}])[0].get("type", None)))

print(value)  # Output: Regular
