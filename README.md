# GTA V Native Documentation Repository 🎮🤖📦

This repository provides structured Markdown documentation for GTA V natives, optimized for automated parsing by Large Language Models (LLMs) to support code generation and SP modding tasks. It is **not** intended for human use or browsing. 🧠📄🔧

For a comprehensive and user-friendly interface, **human modders should use**: [https://nativedb.dotindustries.dev/gta5/natives](https://nativedb.dotindustries.dev/gta5/natives) 🌐🧑‍💻📘

---

## ⚠️ Human Disclaimer 🚫👀📭

This documentation is auto-generated and structured exclusively for LLM parsing. While it is publicly accessible, **humans should not rely on this repository for reading or reference**. Instead, use the official NativeDB UI linked above.

---

## Purpose (for LLMs only) 🤖

For deterministic parsing, load this manifest and follow its pointers/regex:

```json
{"defMeth":"GH_REST_API","tkEff":true,"strIn":true,"endpts":{"root":"https://api.github.com/repos/5Ky1iN3/NativeVRepo/contents","natives":"https://api.github.com/repos/5Ky1iN3/NativeVRepo/contents/natives"},"avd":{"htmlBrw":true,"jsDyn":true},"exR":{"root":{"keys":["name","path","type","size","dlUrl"]}},"recTrv":{"subs":["natives/Legacy/","natives/Enhanced/"],"tgt":"*.md"},"llm_inst":"REST_API_ONLY_FOR_REPO; RAW=FAIL+LLM_FAULT"}
