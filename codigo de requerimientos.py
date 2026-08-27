"""
==============================================================
Evaluador de Requerimientos
Ingeniería de Requerimientos
==============================================================
Evalúa si un requisito de software cumple con los 6 criterios
de calidad SMART-V:

    S - Específico     (Specific)
    M - Medible         (Measurable)
    A - Alcanzable      (Achievable)
    R - Relevante       (Relevant)
    I - Identificable   (Identifiable)
    V - Verificable     (Verifiable)

"""

import re

# ---------------------------------------------------------

PALABRAS_VAGAS = [
    "rápido", "lento", "fácil", "difícil", "bueno", "malo",
    "aceptable", "adecuado", "robusto", "eficiente", "seguro",
    "amigable", "intuitivo", "flexible",
]

TERMINOS_IRREALES = [
    "nunca", "siempre", "100%", "cero errores", "perfecto",
    "ilimitado", "ningún error", "en cualquier caso",
]

ROLES_NEGOCIO = [
    "cliente", "usuario", "docente", "administrador", "coordinador",
    "gerente", "operador", "auditor", "estudiante", "vendedor",
]

PROPOSITOS = [
    "para", "permite", "con el fin de", "debido a", "ya que",
    "porque", "con el objetivo de",
]

PALABRAS_CLAVE_VERIFICABLE = [
    "cuando", "si ", "debe", "máximo", "mínimo",
    "menos de", "más de", "al menos", "exactamente",
]

# ---------------------------------------------------------

def es_especifico(req: str) -> bool:
    """Específico: no contiene palabras vagas ni ambiguas."""
    texto = req.lower()
    encontradas = [p for p in PALABRAS_VAGAS if p in texto]
    return len(encontradas) == 0


# ---------------------------------------------------------
def es_medible(req: str) -> bool:
    """Medible: contiene al menos un número o porcentaje."""
    tiene_numero = bool(re.search(r"\d+", req))
    tiene_porcentaje = "%" in req
    return tiene_numero or tiene_porcentaje


# ---------------------------------------------------------
def es_alcanzable(req: str) -> bool:
    """Alcanzable: no promete absolutismos ni métricas imposibles."""
    texto = req.lower()
    imposibles = [t for t in TERMINOS_IRREALES if t in texto]
    return len(imposibles) == 0


# ---------------------------------------------------------
def es_relevante(req: str) -> bool:
    """Relevante: identifica un actor del negocio o una justificación."""
    texto = req.lower()
    menciona_rol = any(rol in texto for rol in ROLES_NEGOCIO)
    menciona_proposito = any(p in texto for p in PROPOSITOS)
    return menciona_rol or menciona_proposito


# ---------------------------------------------------------
def tiene_id(req: str) -> bool:
    """Identificable: comienza con un ID tipo REQ-001, REQ-AUTH-003, etc."""
    return bool(re.match(r"^REQ(-[A-Z]+)?-\d{3}", req.strip()))


# ---------------------------------------------------------
def es_verificable(req: str) -> bool:
    """Verificable: menciona una condición o criterio concreto de prueba."""
    texto = req.lower()
    return any(p in texto for p in PALABRAS_CLAVE_VERIFICABLE)


# ---------------------------------------------------------
def evaluar_requisito(req: str) -> dict:
    """Evalúa un requisito contra los 6 criterios SMART-V y da un puntaje."""
    resultado = {
        "texto": req,
        "Específico": es_especifico(req),
        "Medible": es_medible(req),
        "Alcanzable": es_alcanzable(req),
        "Relevante": es_relevante(req),
        "Identificable": tiene_id(req),
        "Verificable": es_verificable(req),
    }
    resultado["puntaje"] = sum(
        1 for clave, valor in resultado.items()
        if clave not in ("texto", "puntaje") and valor is True
    )
    return resultado


# ---------------------------------------------------------
def imprimir_reporte(resultado: dict) -> None:
    criterios = ["Específico", "Medible", "Alcanzable",
                 "Relevante", "Identificable", "Verificable"]

    print("\n--- RESULTADO DE LA EVALUACIÓN ---")
    for criterio in criterios:
        estado = "✅ Cumple" if resultado[criterio] else "❌ No cumple"
        print(f"  • {criterio}: {estado}")

    puntaje = resultado["puntaje"]
    print(f"  • Puntaje: {puntaje}")

    if puntaje == 6:
        print(f" VEREDICTO: ¡EXCELENTE REQUISITO! ({puntaje}/6)")
    elif puntaje >= 4:
        print(f" VEREDICTO: REQUISITO ACEPTABLE ({puntaje}/6) - Revisa los criterios en rojo.")
    else:
        print(f" VEREDICTO: REQUISITO DEFICIENTE ({puntaje}/6) - Debes reestructurarlo.")


# ---------------------------------------------------------
def main():
    while True:
        entrada = input("\nEscribe tu requisito: ").strip()

        if entrada.lower() in ("salir", "fin", "exit"):
            print("\nSesión finalizada. ¡Éxitos con tus requisitos!")
            break

        if not entrada:
            continue

        resultado = evaluar_requisito(entrada)
        imprimir_reporte(resultado)


if __name__ == "__main__":
    main()