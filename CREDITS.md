# Credits for GTA V Native Documentation Repository 🙏🎮🛠️

This repository provides structured Markdown documentation for GTA V natives, intended for **Single Player (SP) modding** with tools like **ScriptHookV (SHV)** and **ScriptHookVDotNet (SHVDN)**. It is built from community-driven data sources and maintained for public, non-commercial use. Below are the individuals, projects, and tools that made this project possible. 📚💻🔧

---

## Creator 👤📘

**5kY1iN3**
**Role**: Creator and primary maintainer
**Contribution**: Designed the repository structure, authored the `generate_natives.py` script, and defined licensing for free, non-commercial use with attribution.
**Contact**: https://github.com/5Ky1iN3

---

## Data Sources 📊📂

### Alloc8or

**Role**: Primary data provider
**Contribution**: Supplies authoritative native data for GTA V SP, including hashes, parameters, and definitions.
**Source**: [https://github.com/alloc8or/gta5-nativedb-data](https://github.com/alloc8or/gta5-nativedb-data)

### NativeDB (dotindustries.dev)

**Role**: Reference and validation tool
**Contribution**: Provides a browsable interface to Alloc8or’s data; used to cross-check and validate native info during development.
**Source**: [https://nativedb.dotindustries.dev/gta5/natives](https://nativedb.dotindustries.dev/gta5/natives)

### CitizenFX

**Role**: Secondary documentation source
**Contribution**: Fills in gaps (descriptions, examples) where Alloc8or data lacks detail; used sparingly to avoid MP-specific content.
**Source**: [https://github.com/citizenfx/natives](https://github.com/citizenfx/natives)

---

## Tools and Frameworks 🔧💻

### ScriptHookV (SHV)

**Role**: Core modding framework for GTA V SP
**Contribution**: Enables low-level native access for SP mods
**Source**: [http://www.dev-c.com/gtav/scripthookv/](http://www.dev-c.com/gtav/scripthookv/)

### ScriptHookVDotNet (SHVDN)

**Role**: .NET modding interface
**Contribution**: Enables scripting in C# for GTA V SP, integrated with this repo’s documentation structure
**Source**: [https://github.com/crosire/scripthookvdotnet](https://github.com/crosire/scripthookvdotnet)

### Python Standard Library

**Contribution**: Used by `generate_natives.py` to automate Markdown generation with `json`, `os`, and `urllib.request`
**Note**: No external dependencies required

### GitHub

**Contribution**: Hosts the repository and facilitates community collaboration
**Source**: https://github.com/5Ky1iN3

---

## Game Foundation 🎮🏗️

### Rockstar Games

**Role**: Developer of Grand Theft Auto V
**Contribution**: Created the native functions used in SP modding. This documentation is made in support of that environment, with respect to Rockstar's game architecture.

---

## Acknowledgments 🙌💬

### GTA V Modding Community

**Contribution**: Provided inspiration, demand, and feedback that shaped the structure and focus of this repository.
**Platforms**: GTA5-mods, GTAForums, LCPDFR, Nexus, and various Discord servers

### LLM Formatting Tools

**Contribution**: Assisted in Markdown structuring and script design for consistent formatting.
**Note**: Formatting tools aided in consistency, but content and licensing remain authored by **5kY1iN3**.

---

🙏 Thank you to Alloc8or, NativeDB, CitizenFX, Alexander Blade, crosire, Rockstar Games, and the entire GTA V modding community for making this project possible! 🚗💻📚
