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
{"structure":{"base":"natives/","subdirs":["Legacy","Enhanced"],"namespace":"Each directory contains folders like AUDIO, BRAIN, etc.","files":"Each native is documented as CamelCase .md (e.g., PlaySoundFrontend.md)"},"sources":{"Legacy":"natives.json","Enhanced":"natives_gen9.json"}}
```

---

## Native Markdown File Format 🧾🔢🔍

````json
{"format":{"title":"# _NATIVE_NAME","description":"Lines before the first ###","sections":["### Parameters","### Return Value","### Notes","### Examples"],"examples":{"Lua":"```lua\n...\n```","CSharp":"```cs\n...\n```"},"consistency":"Flat structure, bullet lists, no nesting"}}
````

---

## Parsing Rules (Regex/Extraction) 🧠⚙️📊

````json
{"parsing":{"native_name":"# _([A-Z0-9_]+)","description":"Lines between title and first section","parameters":"* ([\\w\\[\\]]+) (\\w+)","return_type":"* ([\\w\\[\\]]+)","notes":"* (.*)","examples":"#### (\\w+) followed by ```\\w+\\n([\\s\\S]*?)\\n```"},"error_handling":{"missing_description":"No description available","missing_return":"void"}}
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
