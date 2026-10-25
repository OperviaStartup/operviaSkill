# Opervia Skill

Skill compartida para desarrollar tickets de la API de **Opervia Service Compliance** con Codex, Claude Code, Cursor y otros agentes compatibles.

La skill ayuda al equipo a:

- encontrar y validar el ticket solicitado;
- comprobar criterios de aceptación y dependencias;
- evitar inventar endpoints, reglas o funcionalidades;
- respetar la arquitectura Java/Spring del proyecto;
- trabajar con Git Flow y Conventional Commits;
- implementar, probar y revisar avances verificables;
- distinguir trabajo local, integrado, desplegado y realmente validado.

## Instalar

Requisitos: Git y Python 3.

```bash
git clone git@github.com:OperviaStartup/operviaSkill.git
cd operviaSkill
python3 install.py
```

En Windows:

```powershell
git clone git@github.com:OperviaStartup/operviaSkill.git
cd operviaSkill
py install.py
```

El instalador detecta los agentes disponibles. También puedes elegirlos explícitamente:

```bash
python3 install.py --agent codex
python3 install.py --agent claude --agent cursor
python3 install.py --agent all
```

| Agente | Invocación | Carpeta de instalación |
| --- | --- | --- |
| Codex | `$opervia` | `~/.codex/skills/opervia` |
| Claude Code | `/opervia` | `~/.claude/skills/opervia` |
| Cursor | Seleccionar o mencionar `opervia` | `~/.cursor/skills/opervia` |
| Otros Agent Skills | Según el agente | `~/.agents/skills/opervia` |

Para revisar qué se instalará sin modificar archivos:

```bash
python3 install.py --agent all --dry-run
```

También puedes abrir este repositorio con tu agente y pedirle:

```text
Instala como skill de usuario la skill ubicada en skills/opervia.
```

## Usar la skill

Abre el repositorio `serviceComplianceAPI` con el agente. Después invoca la skill y proporciona el identificador exacto del ticket.

### Validar si un ticket está listo

```text
$opervia Revisa BACK-LOGNT-01 y dime si está listo para desarrollarse. Valida sus dependencias contra el código actual.
```

La respuesta clasificará el ticket como:

- `READY`: se puede desarrollar;
- `PARTIAL`: existen avances independientes que sí pueden realizarse;
- `BLOCKED`: falta una dependencia o decisión necesaria;
- `INSUFFICIENT`: el ticket no tiene información suficiente o es contradictorio.

### Implementar un ticket

```text
$opervia Implementa BACK-LOGNT-01. Trabaja solo los criterios habilitados, ejecuta las pruebas y crea commits separados por avances verificables.
```

### Continuar trabajo incompleto

```text
$opervia Continúa BACK-LOGNT-01. Revisa primero la rama, los commits, el ticket y las pruebas actuales; no confíes en avances antiguos sin verificarlos.
```

### Revisar cambios antes de integrar

```text
$opervia Revisa los cambios de BACK-LOGNT-01 contra sus criterios de aceptación. Señala errores, pruebas faltantes y riesgos de integración.
```

### Consultar bloqueos del sprint

```text
$opervia Revisa los tickets que tengo asignados en el sprint actual e indica cuáles están listos, parciales o bloqueados. No implementes nada.
```

En Claude Code reemplaza `$opervia` por `/opervia`.

## Formato de tickets

La skill busca primero tickets versionados en la API:

```text
docs/sprints/<sprint>/tickets/<ticket-id>.md
```

Cada ticket debe indicar objetivo, alcance, criterios de aceptación, dependencias, contratos afectados y verificación requerida. Puedes copiar la [plantilla incluida](skills/opervia/assets/ticket-template.md).

Si el ticket no existe o sus datos esenciales están incompletos, la skill no inventará la información necesaria para implementarlo.

## Git utilizado por la skill

El flujo esperado es:

```text
main <- develop <- feature/<ticket>-<descripcion>
```

Según el trabajo también puede utilizar ramas `fix/`, `docs/` o `chore/`. Los commits siguen esta estructura:

```text
feat(obligations): add recurring obligation definition

Refs: BACK-LOGNT-01
```

Solicitar commits locales no autoriza automáticamente `push`, creación de pull requests, merge ni despliegue.

## Actualizar

```bash
git pull
python3 install.py
```

El instalador actualiza solamente copias administradas por este proyecto y evita sobrescribir una skill ajena con el mismo nombre.

## Estructura del repositorio

```text
operaviaSkill/
├── install.py
├── skills/opervia/
│   ├── SKILL.md
│   ├── assets/ticket-template.md
│   └── references/
└── tests/test_installer.py
```

La fuente oficial es [`skills/opervia`](skills/opervia). Para comprobar el instalador:

```bash
python3 -m unittest discover -s tests -v
```
