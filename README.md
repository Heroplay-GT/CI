# Calculadora simple — CI demo

Proyecto de ejemplo (Python) para demostrar un pipeline de calidad (lint, build, tests y cobertura) en GitHub Actions.

Contenido
- `app.py` — implementación simple de funciones de calculadora.
- `test_app.py` — tests pytest para `app.py`.
- `.github/workflows/ci-quality.yml` — workflow de CI (lint, build, tests, cobertura).
- `requirements.txt`, `pyproject.toml` — dependencias y configuración de build.

Cómo ejecutar localmente
1. Instala dependencias (Windows PowerShell):
```powershell
py -3 -m pip install --upgrade pip
py -3 -m pip install -r requirements.txt
```
2. Ejecuta tests:
```powershell
py -3 -m pytest -q
```

Generar captura (run fallido y exitoso)
1. Para capturar un run fallido en GitHub Actions: se ha incluido un test temporal `tests/test_ci_fail.py` en la rama `main` cuando se pidió generar un fallo. Si quieres repetir el proceso manualmente:
   - Añade un test que falle en `tests/` (p.ej. `assert False`) y push a `main`.
   - Abre la pestaña Actions → selecciona el workflow `CI Quality Pipeline` → toma la captura del paso/ejecución fallida.
2. Para capturar el run exitoso: elimina o corrige el test fallido, commitea y pushea de nuevo; espera a que GitHub Actions termine y toma la captura de la ejecución verde.

Capturas y logs locales
- He colocado dos capturas de ejemplo (salidas de pytest) en `captures_temp/`:
  - `captures_temp/fail_run.txt` (run fallido localmente)
  - `captures_temp/success_run.txt` (run exitoso localmente)

Limpieza de logs
- Si quieres que elimine los archivos de logs del repositorio, puedo archivarlos (ZIP) y borrar los ficheros del repo. Pide "archivar" o "borrar" y lo hago.

Contacto
- Si necesitas que haga push del commit correctivo (remover el test fallido) dímelo y lo ejecuto cuando confirmes que tomaste la captura del run fallido.
