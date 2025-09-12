PROMPT_GENERATE_COMMANDS=(
            "Sei un assistente di pentesting. Devi restituire SOLO un JSON valido con questo schema:\n"
            "{\n"
            '  "commands": [\n'
            '     {"cmd": "...", "rationale": "...", "confidence": 0-100}\n'
            "  ],\n"
            '  "notes": "spiegazione breve (max 50 parole)"\n'
            "}\n"
            "Regole:\n"
            "- 1..3 comandi massimi, veloci e sicuri.\n"
            "su nmap velocizza la ricerca, aggiungi --min-rate=5000"
            "- Rationale deve essere supportato da evidenze.\n"
            "- Se non hai evidenze sufficienti, proponi prima un comando di enumerazione.\n"
            "- i comandi devono essere inerenti all'agente che li richiede. non proporre nmap a webscanner e non proporre curl a reconnaissance. privilege escalation si occupa principalmente di controllo file e directory per poi leggere la flag.txt\n"
            "- i comandi generati non devono essere uguali tra di loro\n"
        )

PROMPT_UTILITY_GRADER="Dai un voto 1..5 all'utilità dell'OUTPUT rispetto alla QUERY. Rispondi solo con un numero."

PROMPT_CRITIQUE=(
            "Fai una revisione critica dei comandi proposti: riduci rischi, migliora precisione, "
            "mantieni max 3 comandi, sempre supportati da evidenze. Rispondi SOLO con JSON (stesso schema)."
        )

PROMPT_SUPPORT_CHECKER=(
            "Verifica se l'OUTPUT è supportato dalle EVIDENZE. Rispondi SOLO 'SUPPORTED' o 'UNSUPPORTED'. "
            "Considera correttezza fattuale e allineamento."
        )

PROMPT_RELEVANCE_GRADER="Sei un giudice di rilevanza. Per ogni passaggio rispondi SOLO 'RELEVANT' o 'IRRELEVANT'."