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
 # RESPUESTAS — Parcial CI/CD

 Abajo respondo las partes del enunciado con lenguaje directo y orientado a entrega.

 Parte 1 — Estrategia

 - Diferencia CI vs CD (en una línea):
	 - CI (Integración Continua): cada cambio en el repo dispara comprobaciones automáticas (lint, build, tests) para detectar errores cuanto antes.
	 - CD (Entrega/Despliegue Continuo): después de que la pipeline pasa, los artefactos se despliegan o ponen a disposición en un entorno (staging/producción).

 - Decisiones para este trabajo:
	 - Lenguaje: Python (rápido de montar y suficiente para el enunciado).
	 - Linter: flake8 (ligero y estándar en proyectos Python).
	 - Cobertura: pytest + pytest-cov (fácil de integrar en Actions y generar informes legibles).

 - Umbral de cobertura propuesto: 80%
	 - Justificación: está dentro del rango 70–90% pedido; es lo bastante alto para exigir tests útiles sin ser excesivamente estricto en un proyecto pequeño.

 Parte 2 — Workflow (resumen)

 - El workflow usado está en `.github/workflows/ci-quality.yml` y realiza, en orden: checkout, configurar Python, instalar dependencias, ejecutar flake8, build (python -m build) y pytest con `--cov` validando `--cov-fail-under=80`.
 - Idea clave: si flake8, build o pytest fallan, el job debe detenerse y marcarse como fallido. Durante la fase de depuración añadimos pasos que suben logs para inspección; la versión final debería ser estricta (no ignorar errores).

 Parte 3 — Uso de `act` (ejecución local)

 - ¿Qué es `act`?: una herramienta que emula GitHub Actions en tu máquina usando Docker; permite probar workflows sin push al repositorio.
 - Requisitos: Docker en funcionamiento; tener `act` instalado (binario o gestor de paquetes).
 - Comando práctico: `act -j quality-check -P ubuntu-latest=nektos/act-environments-ubuntu:18.04` (ver README para variantes y opciones).

 Parte 4 — Logs y capturas (cómo identificar fallos)

 - Linter (flake8): los errores indican fichero, línea y código de error (ej. `F401` o `E302`). Si aparece salida de flake8 con errores, el paso falla.
 - Tests (pytest): busca `FAILED` o `ERROR` y la sección final con el resumen (`n failed, m passed`). Un fallo en tests devuelve exit code != 0.
 - Cobertura: si el porcentaje resultante cae por debajo del umbral (`--cov-fail-under`), pytest devuelve error y el job falla; el reporte HTML (`htmlcov/`) muestra líneas sin cobertura.

 - Diferencia práctica entre run fallido y run exitoso:
	 - Fallido: Actions marca un paso en rojo; los logs muestran la causa (assert, excepción, error de flake8 o cobertura insuficiente).
	 - Exitoso: todos los pasos terminan con código 0; pytest muestra `X passed` y la cobertura cumple el umbral.

 Parte 5 — IA y ética (resumen práctico)

 - Dos métodos razonables para detectar código asistido por IA:
	 1) Heurísticas estilísticas y métricas (consistencia perfecta de formato, uso de patrones poco naturales).
	 2) Herramientas de detección que comparan probabilidades/token patterns frente a modelos de lenguaje entrenados.

 - Por qué no hay 100% de certeza:
	 - Los métodos ofrecen probabilidades; código simple puede coincidir con lo que un humano escribiría y los detectores generan falsos positivos/negativos.



