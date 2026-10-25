# Opervia Skill

Flujo compartido para que asistentes de IA validen y desarrollen tickets de la API de Service Compliance con evidencia, Git Flow y commits convencionales.

## Instalación rápida

Clona este repositorio privado y ejecuta el instalador desde su raíz:

```bash
python3 install.py
```

En Windows también puedes usar:

```powershell
py install.py
```

La detección automática instala la skill en los agentes encontrados. También puedes indicar uno o varios agentes sin responder preguntas:

```bash
python3 install.py --agent codex
python3 install.py --agent claude --agent cursor
python3 install.py --agent all
```

| Agente | Destino de usuario | Invocación habitual |
| --- | --- | --- |
| Codex | `~/.codex/skills/opervia` | `$opervia` |
| Claude Code | `~/.claude/skills/opervia` | `/opervia` |
| Cursor | `~/.cursor/skills/opervia` | Skill desde el agente |
| Compatible con Agent Skills | `~/.agents/skills/opervia` | Depende del agente |

Si el agente no está en la lista, pásale directamente esta instrucción:

> Instala la skill ubicada en `<ruta-del-repo>/skills/opervia` como una skill de usuario llamada `opervia`.

El instalador no solicita credenciales ni modifica repositorios de proyecto. Para actualizar, haz `git pull` en este repositorio y ejecuta el mismo comando otra vez. Usa `--dry-run` para ver los destinos sin escribir.

## Uso

Abre el repositorio de la API con tu agente y proporciona el ticket:

```text
$opervia Quiero realizar BACK-LOGNT-01. Valida si está listo, implementa únicamente lo habilitado y crea commits separados por avance verificable.
```

En Claude Code usa `/opervia` en lugar de `$opervia`.

La fuente canónica está en [`skills/opervia`](skills/opervia). No edites directamente la copia instalada: actualiza este repositorio y reinstala.

## Desarrollo

```bash
python3 -m unittest discover -s tests -v
```

La skill es un paquete Markdown portable y no depende de herramientas de validación en tiempo de uso.
