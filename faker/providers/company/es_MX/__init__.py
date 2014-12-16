# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}}-{{last_name}}',
        '{{company_prefix}} {{last_name}}-{{last_name}}',
        '{{company_prefix}} {{last_name}} y {{last_name}}',
        '{{company_prefix}} {{last_name}}, {{last_name}} y {{last_name}}',
        '{{last_name}}-{{last_name}} {{company_suffix}}',
        '{{last_name}}, {{last_name}} y {{last_name}}',
        '{{last_name}} y {{last_name}} {{company_suffix}}'
    )

    catch_phrase_words = (
        (
           "habilidad", "acceso", "adaptador", "algoritmo", "alianza",
           "analista", "aplicación", "enfoque", "arquitectura",
           "archivo", "inteligencia artificial", "array", "actitud",
           "medición", "gestión presupuestaria", "capacidad", "desafío",
           "circuito", "colaboración", "complejidad", "concepto",
           "conglomeración", "contingencia", "núcleo", "fidelidad",
           "base de datos", "data-warehouse", "definición", "emulación",
           "codificar", "encriptar", "extranet", "firmware",
           "flexibilidad", "focus group", "previsión", "base de trabajo",
           "función", "funcionalidad", "Interfaz Gráfica", "groupware",
           "Interfaz gráfico de usuario", "hardware", "Soporte", "jerarquía",
           "conjunto", "implementación", "infraestructura", "iniciativa",
           "instalación", "conjunto de instrucciones", "interfaz",
           "intranet", "base del conocimiento", "red de area local",
           "aprovechar", "matrices", "metodologías", "middleware",
           "migración", "modelo", "moderador", "monitorizar",
           "arquitectura abierta", "sistema abierto", "orquestar",
           "paradigma", "paralelismo", "política", "portal",
           "estructura de precios", "proceso de mejora",
           "producto", "productividad", "proyecto", "proyección",
           "protocolo", "línea segura", "software", "solución",
           "estandardización", "estrategia", "estructura", "éxito",
           "superestructura", "soporte", "sinergia", "mediante",
           "marco de tiempo", "caja de herramientas", "utilización",
           "website", "fuerza de trabajo"),
        (
            "24 horas", "24/7", "3ra generación", "4ta generación",
            "5ta generación", "6ta generación", "analizada",
            "asimétrica", "asíncrona", "monitorizada por red",
            "bidireccional", "bifurcada", "generada por el cliente",
            "cliente servidor", "coherente", "cohesiva", "compuesto",
            "sensible al contexto", "basado en el contexto",
            "basado en contenido", "dedicada",
            "generado por la demanda", "didactica", "direccional",
            "discreta", "dinámica", "potenciada", "acompasada",
            "ejecutiva", "explícita", "tolerante a fallos",
            "innovadora", "amplio ábanico", "global", "heurística",
            "alto nivel", "holística", "homogénea", "híbrida",
            "incremental", "intangible", "interactiva", "intermedia",
            "local", "logística", "maximizada", "metódica",
            "misión crítica", "móbil", "modular", "motivadora",
            "multimedia", "multiestado", "multitarea", "nacional",
            "basado en necesidades", "neutral", "nueva generación",
            "no-volátil", "orientado a objetos", "óptima", "optimizada",
            "radical", "tiempo real", "recíproca", "regional",
            "escalable", "secundaria", "orientada a soluciones",
            "estable", "estatica", "sistemática", "sistémica",
            "tangible", "terciaria", "transicional", "uniforme",
            "valor añadido", "vía web", "defectos cero", "tolerancia cero"
        ),
        (
            'adaptivo', 'avanzado', 'asimilado', 'automatizado',
            'balanceado', 'enfocado al negocio',
            'centralizado', 'clonado', 'compatible', 'configurable',
            'multiplataforma', 'enfocado al cliente', 'personalizable',
            'descentralizado', 'digitizado', 'distribuido', 'diverso',
            'mejorado', 'en toda la empresa', 'ergonómico', 'exclusivo',
            'expandido', 'extendido', 'cara a cara', 'enfocado',
            'de primera línea', 'totalmente configurable',
            'basado en funcionalidad', 'fundamental', 'horizontal',
            'implementado', 'innovador', 'integrado', 'intuitivo',
            'inverso', 'administrado', 'mandatorio', 'monitoreado',
            'multicanal', 'multilateral', 'multi-capas', 'en red',
            'basado en objetos', 'de arquitectura abierta',
            'Open-source', 'operativo', 'optimizado', 'opcional',
            'orgánico', 'organizado', 'perseverante', 'persistente',
            'polarizado', 'preventivo', 'proactivo', 'enfocado a ganancias',
            'programable', 'progresivo', 'llave pública',
            'enfocado a la calidad', 'reactivo', 'realineado',
            're-contextualizado', 'reducido', 'con ingeniería inversa',
            'de tamaño adecuado', 'robusto', 'seguro', 'compartible',
            'sincronizado', 'orientado a equipos', 'total',
            'universal', 'actualizable', 'centrado al usuario',
            'versátil', 'virtual', 'visionario',
        )
    )

    bsWords = (
        (
            'implementa', 'utiliza', 'integrata', 'optimiza',
            'evoluciona', 'transforma', 'abraza', 'habilia',
            'orquesta', 'reinventa', 'agrega', 'mejora', 'incentiviza',
            'modifica', 'empondera', 'monetiza', 'fortalece',
            'facilita', 'synergiza',  'crear marca', 'crece',
            'sintetiza', 'entrega', 'mezcla', 'incuba', 'compromete',
            'maximiza', 'inmediata', 'visualiza', 'inova',
            'escala', 'libera', 'maneja', 'extiende', 'revoluciona',
            'genera', 'explota', 'transición', 'itera', 'cultiva',
            'redefine', 'recontextualiza',
        ),
        (
            'synergías', 'paradigmas', 'marcados', 'socios',
            'infraestructuras', 'plataformas', 'iniciativas',
            'chanales', 'communidades', 'ROI', 'soluciones',
            'portales', 'nichos', 'tecnologías', 'contenido',
            'cadena de producción', 'convergencia', 'relaciones',
            'architecturas', 'interfaces', 'comercio electrónico',
            'sistemas', 'ancho de banda', 'modelos', 'entregables',
            'usuarios', 'esquemas', 'redes', 'aplicaciones', 'métricas',
            'funcionalidades', 'experiencias', 'servicios web',
            'metodologías'
        ),
        (
            'valor agregado', 'verticales', 'proactivas', 'robustas',
            'revolucionarias', 'escalables', 'de punta', 'innovadoras',
            'intuitivas', 'estratégicas', 'e-business', 'de misión crítica',
            'uno-a-uno', '24/7', 'end-to-end', 'globales', 'B2B', 'B2C',
            'granulares', 'sin fricciones', 'virtuales', 'virales',
            'dinámicas', '24/365', 'magnéticas', 'listo para la web',
            'interactivas', 'dot-com', 'sexi', 'en tiempo real',
            'eficientes', 'front-end', 'distribuidas', 'extensibles',
            'llave en mano', 'de clase mundial', 'open-source',
            'plataforma cruzada', 'de paquete', 'empresariales',
            'integrado', 'impacto total', 'inalámbrica', 'transparentes',
            'de siguiente generación', 'lo último', 'centrado al usuario',
            'visionarias', 'personalizado', 'ubicuas', 'plug-and-play',
            'colaborativas', 'holísticas', 'ricas'
        ),
    )

    company_preffixes = ('Despacho', 'Grupo', 'Corporativo', 'Club',
                         'Industrias', 'Laboratorios', 'Proyectos')

    company_suffixes = ('A.C.', 'S.A.', 'S.A. de C.V.', 'S.C.',
        'S. R.L. de C.V.','e Hijos', 'y Asociados')

    def company_prefix(self):
        """
        Ejemplo: Grupo
        """
        return self.random_element(self.company_preffixes)

    def catch_phrase(self):
        """
        :example 'Robust full-range hub'
        """
        result = []
        for word_list in self.catch_phrase_words:
            result.append(self.random_element(word_list))

        return " ".join(result)

    def bs(self):
        """
        :example 'integrate extensible convergence'
        """
        result = []
        for word_list in self.bsWords:
            result.append(self.random_element(word_list))

        return " ".join(result)
