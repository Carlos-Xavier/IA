flag = None
vars = {
    "dor_de_cabeça": None,
    "garganta_inflamada": None,
    "tosse": None,
    "cansaço": None,
    "dor_de_ouvido": None,
    "privação_de_sono": None,
    "dor_de_garganta": None
}


rules = [ 
    "dor_de_cabeça", 
    "dor_de_cabeça E garganta_inflamada E tosse", 
    "cansaço E dor_de_cabeça",
    "cansaço E garganta_inflamada",
    "cansaço",
    "dor_de_garganta",
    "garganta_inflamada E dor_de_garganta E dor_de_ouvido",
    "privação_de_sono",
    "cansaço E privação_de_sono",
    "dor_de_ouvido",
    "garganta_inflamada",
]


questions = {
    "dor_de_cabeça": ["Você está com dor de cabeça?\nSim ou Não\n",flag],
    "dor_de_ouvido": ["Você está com dor de ouvido?\nSim ou Não\n",flag],
    "tosse": ["Você está com tosse ?\nSim ou não\n",flag],
    "dor_de_garganta": ["Você está com dor de garganta?\nSim ou Não\n",flag],
    "privação_de_sono": ["Você está com problemas para dormir?\nSim ou Não\n",flag]
}
