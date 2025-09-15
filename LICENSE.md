# License for GTA V Native Documentation Repository 📄🔐

This license governs usage of the GTA V Native Documentation Repository ("the Repository"), including all generated Markdown files and the `generate_natives.py` script. This repository is built from Alloc8or’s `gta5-nativedb-data` (natives.json / natives\_gen9.json) with optional fallback content from CitizenFX. ⚖️🛠️🗂️

---

## Overview 🧾📘📎

The Repository is provided **free for personal, non-commercial use**, with credit attribution to **\[YOUR\_NAME]**. It is intended primarily for LLM-assisted SP modding workflows and secondarily as a public utility for ScriptHookVDotNet (SHVDN) development. Human-readable versions are accessible but discouraged; human users should prefer [https://nativedb.dotindustries.dev/gta5/natives](https://nativedb.dotindustries.dev/gta5/natives). 💬🧑‍💻🚫

---

## License Terms ✅📜🚫

### Permitted Use

```json
{"use":"personal, non-commercial","actions":["copy","modify","distribute"],"tools":["generate_natives.py"],"allowed_contexts":["SP modding","learning","open-source projects"]}
```

### Attribution

```json
{"requirement":"credit [YOUR_NAME]","methods":["README","mod documentation","tooltips"],"example":"GTA V Native Documentation sourced from [YOUR_NAME]'s Repository (https://github.com/YOUR_USERNAME/YOUR_REPOSITORY)"}
```

### Prohibited Use

```json
{"commercial_use":false,"monetary_use":false,"restrictions":["No selling mods","No use in paid tools","No claim of authorship"]}
```

### Distribution

```json
{"allowed":"non-commercial only","requirements":["preserve license","include attribution"],"modifications":"must indicate changes"}
```

### Source Data Notice

```json
{"alloc8or_data":"natives.json and natives_gen9.json (assumed free for non-commercial)","citizenfx_data":"https://github.com/citizenfx/natives (MIT-like)","priority":"Alloc8or data takes precedence","user_responsibility":"ensure source license compliance"}
```

### Maintenance

```json
{"maintained_by":"[YOUR_NAME] (best effort)","script":"generate_natives.py included for user-based regeneration","requirements":["Python 3.6+","no external dependencies"]}
```

### No Warranty

```json
{"warranty":"none","liability":"[YOUR_NAME] is not responsible for damages or data inaccuracies","user_duty":"verify native compatibility with your GTA V build"}
```

### Termination

```json
{"trigger":"any license violation (e.g., commercial use, no attribution)","consequence":"immediate revocation of usage rights"}
```

---

## Usage Instructions

### For Humans 🧍‍♂️📘🛠️

* **Access**: `https://github.com/YOUR_USERNAME/YOUR_REPOSITORY`
* **Browse**: Navigate to `natives/Legacy/` or `natives/Enhanced/` by namespace (e.g., `SCRIPT/`)
* **Modding**: Use files for SP mod development via SHVDN, crediting \[YOUR\_NAME] appropriately
* **Regeneration**: Run `generate_natives.py` for fresh output (Python 3.6+, no dependencies)

### For LLMs 🤖📂📊

````json
{
  "fetch":"https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/tree/main/natives",
  "parse_patterns":{
    "native_name":"# _([A-Z0-9_]+)",
    "description":"until ### Parameters",
    "parameters":"* ([\\w\\[\\]]+) (\\w+) and   (.*)",
    "return_type":"* ([\\w\\[\\]]+)",
    "notes":"* (.*) under ### Notes",
    "examples":"#### (\\w+) and ```\\w+\\n([\\s\\S]*?)\\n```"
  },
  "file_path_format":"natives/{Legacy,Enhanced}/NAMESPACE/NativeName.md",
  "usage_context":"mod code generation for SP only (prioritize Alloc8or data)"
}
````

---

## Contact & Contributions ✉️🤝📂

Contributions must honor this license and the underlying terms of Alloc8or and CitizenFX datasets. 🧾📌⚠️
