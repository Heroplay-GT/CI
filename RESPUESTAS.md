# RESPUESTAS — Tarea CI

1) ¿Qué es CI y CD (breve)?
- CI (Integración Continua): automatizar la ejecución de build/linter/tests y generar artefactos cuando se hacen cambios en el repo.
- CD (Entrega/Despliegue Continuo): procesos que despliegan automáticamente artefactos a entornos (staging/producción) tras pasar la pipeline.

2) Herramientas elegidas y por qué
- GitHub Actions: integración nativa en el repositorio y gratis para pipelines básicos.
- pytest + pytest-cov: testing y cobertura sencilla, ampliamente usada en Python.
- flake8: linter ligero para mantener estilo PEP8.
- build/setuptools/wheel: generar paquete distribuible.

3) Threshold de cobertura
- Se configuró `--cov-fail-under=80` en el workflow — objetivo mínimo 80% de cobertura.

4) Cómo reproducir localmente
- Instala deps: `py -3 -m pip install -r requirements.txt`
- Ejecuta tests: `py -3 -m pytest -q`
- Para simular el workflow localmente usa `act` (requiere Docker). Documentación en README.

5) Evidencia de runs
- Captura de run fallido: provista por el push que añadió `tests/test_ci_fail.py`.
- Captura de run exitoso: se obtiene al eliminar/armonizar el test fallido y pushear la corrección.

6) Notas finales y recomendaciones
- He dejado pasos de diagnóstico temporales en el workflow (subida de artefactos de logs) para ayudar al debugging; se pueden quitar si se desea comportamiento estricto (fallar el job cuando algo falla).
- Si quieres que archive y elimine los logs (`act_local_run*.txt`, `act_success*.txt`), puedo hacerlo y actualizar este archivo con la ruta del archivo ZIP.
