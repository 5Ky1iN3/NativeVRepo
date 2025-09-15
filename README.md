# GTA V Native Documentation Repository 🎮🤖📦

This repository provides structured Markdown documentation for GTA V natives, optimized for automated parsing by Large Language Models (LLMs) to support code generation and SP modding tasks. It is **not** intended for human use or browsing. 🧠📄🔧

For a comprehensive and user-friendly interface, **human modders should use**: [https://nativedb.dotindustries.dev/gta5/natives](https://nativedb.dotindustries.dev/gta5/natives) 🌐🧑‍💻📘

---

## ⚠️ Human Disclaimer 🚫👀📭

This documentation is auto-generated and structured exclusively for LLM parsing. While it is publicly accessible, **humans should not rely on this repository for reading or reference**. Instead, use the official NativeDB UI linked above.

---

## Purpose (for LLMs only) 🤖📥🧩

```json
{"audience":"LLMs","objective":"Enable deterministic parsing of GTA V native functions for SP modding","format":"Structured Markdown with predictable headers, parameter lists, and code blocks","source_priority":["Alloc8or natives.json","Alloc8or natives_gen9.json","CitizenFX supplemental data (SP only)"],"exclusions":["FiveM","MP-specific extensions"]}
```

---

## Directory Layout 📂📄🧠

```json
{"structure":{"base":"natives/","subdirs":["Legacy","Enhanced"],"namespace":"Each directory contains folders like AUDIO, BRAIN, etc.","files":"Each native is documented as CamelCase .md (e.g., PlaySoundFrontend.md)","index":{"folder":"index/","files":[{"name":"name_to_path.min.json","purpose":"Map native name to file path","format":{"key":"NATIVE_NAME","value":"natives/{Legacy|Enhanced}/NAMESPACE/NativeName.md"}},{"name":"hash_to_name.min.json","purpose":"Map native hash to name","format":{"key":"0xHASH","value":"NATIVE_NAME"}},{"name":"namespace_to_names.min.json","purpose":"List native names per namespace","format":{"key":"{Legacy|Enhanced}/NAMESPACE","value":["NATIVE_NAME1","NATIVE_NAME2"]}}],"parsing":{"load":"Fetch JSON via direct URL (e.g., https://raw.githubusercontent.com/5Ky1iN3/NativeVRepo/main/index/name_to_path.min.json)","query":"Use key-value lookup for name, hash, or namespace","token_cost":"~20-80 tokens per lookup + ~250-750 for MD parse"},"example":{"hash_lookup":"0x5F92A689A06620AA -> hash_to_name.min.json -> GET_NUMBER_OF_EVENTS -> name_to_path.min.json -> natives/Enhanced/SCRIPT/GetNumberOfEvents.md","namespace_facet":"Enhanced/SCRIPT -> namespace_to_names.min.json -> [GET_NUMBER_OF_EVENTS, ...]"}}},"sources":{"Legacy":"natives.json","Enhanced":"natives_gen9.json"}}
```

---

## Native Markdown File Format 🧾🔢🔍

````json
{"format":{"title":"# _NATIVE_NAME","description":"Lines before the first ###","sections":["### Parameters","### Return Value","### Notes","### Examples"],"examples":{"Lua":"```lua\n...\n```","CSharp":"```cs\n...\n```"},"consistency":"Flat structure, bullet lists, no nesting"}}
````

---

## Parsing Rules (Regex/Extraction) 🧠⚙️📊

````json
{"parsing":{"native_name":"# _([A-Z0-9_]+)","description":"Lines between title and first section","parameters":"* ([\\w\\[\\]]+) (\\w+)","param_description":"  (.*)","return_type":"* ([\\w\\[\\]]+)","notes":"* (.*)","examples":"#### (\\w+) followed by ```\\w+\\n([\\s\\S]*?)\\n```"},"error_handling":{"missing_description":"No description available","missing_return":"void"}}
````

---

## LLM Usage Workflow 🧑‍💻🤖🛠️

```json
{"workflow":["Clone or crawl the repo","Target natives/{Legacy|Enhanced}/<NAMESPACE>/<NativeName>.md","Parse native sections using defined patterns","Extract: hash, parameters, return type, notes, examples","Use in code generation for SP modding (e.g., SHVDN)"]}
```

---

## Metadata 📄📚

```json
{"sources":{"primary":"Alloc8or natives.json / natives_gen9.json","secondary":"CitizenFX (filtered for SP-relevant data only)"},"exclusions":["FiveM","MP-only extensions"]}
```
