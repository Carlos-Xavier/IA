# Lista 2 - IA
Base de conhecimento

- "MT": "dor_de_cabeça",
    - "rules": 
        - "dor_de_cabeça": "receitar = analgésico",
        - "dor_de_cabeça E garganta_inflamada E tosse": "diagnóstico = gripe",
        - "cansaço E dor_de_cabeça": "diagnóstico = mononucleose_infecciosa",
        - "cansaço E garganta_inflamada": "diagnóstico = amigdalite",
        - "cansaço": "diagnóstico = estresse",
        - "dor_de_garganta": "garganta_inflamada",
        - "garganta_inflamada E dor_de_garganta E dor_de_ouvido": "diagnóstico = faringite_estreptocócica",
        - "privação_de_sono": "cansaço",
        - "cansaço E privação_de_sono": "diagnóstico = apneia_de_sono",
        - "dor_de_ouvido": "diagnóstico = otite",
       - "garganta_inflamada": "receitar = Anti-inflamatórios"
