## huge-tool-call-sim

**Author:** akiraueno
**Version:** 0.0.1
**Type:** agent-strategy

### Description
This repository is a tool call simulation plugin for debugging not responding `llm.invoke` in dify plugin.

## Usage
### install dependencies
```bash
uv sync
```

### run the script
```bash
uv run python3 -m main
```

### add dependencies
```bash
uv add <package>
```

### remove dependencies
```bash
uv remove <package>
```

### update requirements.txt
Dify plugin not use pyproject.toml but use requirements.txt to install dependencies.
```bash
uv pip compile pyproject.toml > requirements.txt
```
