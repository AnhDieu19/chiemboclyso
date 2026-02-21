# Project Rules

## 1. Project Structure
- **root/**: Configuration and entry points.
- **python/**: Main application source code.
    - `core/`: Core calculation logic.
    - `data/`: Constants and data mapping.
    - `logic/` or `interpretation/`: Business logic.
    - `templates/`: HTML templates (Jinja2).
    - `static/`: Static assets (CSS, JS, images).
- **docs/**: All project documentation.
- **archive/**: Deprecated or legacy files.

## 2. Technology Stack
- **Backend**: Python 3.x with Flask framework.
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
- **Templating**: Jinja2 (within Flask).

## 3. Coding Standards (Quy chuẩn code)
- **Language**:
    - **Variables/Functions**: Vietnamese with underscores (snake_case) or English (consistent within module).
    - **Comments**: Vietnamese (Tiếng Việt có dấu).
    - **Commits**: Vietnamese or English, clear and descriptive.
- **Formatting**:
    - Follow PEP 8 for Python.
    - 4 spaces for indentation.
- **Documentation**:
    - Every major function must have a docstring explaining inputs/outputs.
    - Keep `docs/` updated with major feature changes.

## 4. Workflow
- **Development**: Work in `python/` directory.
- **Testing**: Run local server with `python app.py` (debug mode).
- **Updates**: Update `task.md` and relevant docs when completing features.
