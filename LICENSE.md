# License for GTA V NativeVRepo 📄🔐

This license governs usage of the GTA V Native Repository, including all generated Markdown files and the `generate_natives.py` script. This repository is built from Alloc8or’s `gta5-nativedb-data` (natives.json / natives\_gen9.json) with optional fallback content from CitizenFX. ⚖️🛠️🗂️

---

## Overview 🧾📘📎

The Repository is provided **free for personal, non-commercial use**, with credit attribution to **5kY1iN3**. It is intended to serve as a public utility for GTA V Single Player (SP) modding workflows, especially ScriptHook (SHV) and ScriptHookVDotNet (SHVDN) development. 🧑‍💻🔧🎮

---

## License Terms ✅📜🚫

### Permitted Use

You may:

* Use, copy, and modify the Repository for **personal, non-commercial purposes**
* Use the provided script (`generate_natives.py`) to regenerate or update documentation from source data
* Include this Repository in open-source modding projects with proper attribution

### Attribution

You must:

* Provide visible credit to **5kY1iN3** when using or redistributing the Repository or derivative works
* Example: *"GTA V Native Documentation sourced from 5kY1iN3's Repository (https://github.com/5Ky1iN3/NativeVRepo)"*
* Include this credit in READMEs, mod documentation, or tool UIs

### Prohibited Use

You may **NOT**:

* Use the Repository or script for **commercial or monetary purposes** (e.g., selling mods, paid software, monetized platforms)
* Rebrand or claim ownership of this Repository or its contents
* Distribute any derivative work without proper attribution

### Distribution

You may:

* Share the Repository or modified versions freely for **non-commercial purposes**, as long as:

  * This license is included
  * Attribution is preserved
  * Changes are clearly indicated

### Source Data Notice

This Repository is built using data from:

* Alloc8or's `gta5-nativedb-data` (`natives.json`, `natives_gen9.json`)
* CitizenFX’s native documentation ([https://github.com/citizenfx/natives](https://github.com/citizenfx/natives))

Users are responsible for ensuring compliance with these upstream licenses:

* **Alloc8or data**: No explicit license; assumed usable for non-commercial open documentation purposes with attribution
* **CitizenFX data**: Typically licensed under permissive terms (MIT-like), filtered for SP relevance

### Maintenance

* This project is maintained on a best-effort basis by **5kY1iN3**
* The script (`generate_natives.py`) is included to allow independent regeneration if updates become unavailable
* The script requires **Python 3.6+** and has **no external dependencies**

### No Warranty

This Repository is provided **"as is"** without warranty of any kind. **5kY1iN3** is not responsible for:

* Errors, omissions, or inaccuracies in native data
* Compatibility issues with GTA V builds
* Any damages resulting from use of this Repository or script

### Termination

This license terminates automatically if you:

* Violate any of its terms (e.g., commercial use, failure to credit)
* Distribute modified versions without proper license and attribution

Upon termination, you must cease using and distributing all Repository contents.

---

## Usage Instructions 📘🛠️

### How to Use

1. **Clone or Download**:

   * Visit `https://github.com/5Ky1iN3/NativeVRepo`
   * Use `git clone` or GitHub's download tools

2. **Browse Documentation**:

   * Navigate to `natives/Legacy/` or `natives/Enhanced/`
   * Explore by namespace (e.g., `SCRIPT/`, `AUDIO/`)
   * Open individual `.md` files for per-native documentation

3. **Regenerate Documentation**:

   * Run `generate_natives.py`
   * Requires Python 3.6+; no external dependencies
   * Fetches and reformats data from Alloc8or and CitizenFX

4. **Use in Modding**:

   * Reference native hashes, parameter types, return values, and usage examples
   * Suitable for ScriptHook (SHV), ScriptHookVDotNet (SHVDN), Lua scripting, or documentation tooling

---

## Contact & Contributions ✉️🤝📂

For feedback, bug reports, or contributions:
* Ensure any contributions comply with this license and credit structure

Thank you for supporting the GTA V modding community! 🎮🧰📚
