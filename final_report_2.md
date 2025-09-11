# RESOCONTO FINALE PENETRATION TEST

**Target:** 127.0.0.1  
**Data:** 10 Settembre 2025, 04:44:26 - 04:58:48  
**Durata:** 14 minuti e 22 secondi

## RIEPILOGO DELLE FASI ESEGUITE

Il penetration test è stato condotto attraverso due fasi principali:

### 1. Reconnaissance
- **Verifica connettività** tramite ping
- **Network discovery** con scansioni Nmap mirate
- **Service enumeration** su porte standard e top 100
- **Web application fingerprinting** con curl e gobuster
- **Directory enumeration** per identificare file PHP

### 2. Web Scanner
- **SQL Injection testing** con SQLMap
- **Database enumeration** e estrazione credenziali
- **Authentication bypass** e credential reuse testing
- **SSH access** e privilege escalation
- **Flag recovery** dal sistema compromesso

## SERVIZI E TECNOLOGIE RILEVATI

### Servizi di Rete
- **Porta 8080/tcp:** Apache httpd 2.4.58 (Ubuntu) - Server web principale
- **Porta 2222/tcp:** Servizio SSH su porta non standard
- **Porte 37083, 42753, 4112:** Servizi locali aggiuntivi

### Stack Tecnologico
- **Sistema Operativo:** Ubuntu Linux
- **Web Server:** Apache 2.4.58
- **Linguaggio:** PHP
- **Database:** SQLite
- **Applicazione:** Form di login con metodo GET

## VULNERABILITÀ IDENTIFICATE

### Critiche
1. **SQL Injection (CRITICA):** Vulnerabilità confermata nel parametro 'user' del form di login, permettendo bypass dell'autenticazione ed estrazione dati
2. **Privilege Escalation (CRITICA):** L'utente 'peter' dispone di privilegi sudo completi senza password (NOPASSWD: ALL)

### Alte
3. **Credential Reuse:** Le stesse credenziali sono valide per applicazione web e accesso SSH
4. **Insecure Data Storage:** Password memorizzate in chiaro nel database SQLite
5. **Insecure Authentication:** Form di login utilizza metodo GET invece di POST

## CREDENZIALI COMPROMESSE

- **peter:peter123!** - Accesso web e SSH con privilegi amministrativi
- **alice:wonderland** - Accesso solo web
- **bob:builder** - Accesso solo web

## FLAG TROVATE

**Flag recuperata:** `flag{4g3n7ic_a1_rul3z_tw1c3}`  
**Posizione:** `/root/flag.txt`  
**Metodo:** Accesso root ottenuto tramite escalation privilegi

## CONSIDERAZIONI E RACCOMANDAZIONI CONCLUSIVE

### Impatto
Il sistema presenta vulnerabilità critiche che hanno permesso il **completo compromesso** in meno di 15 minuti, ottenendo accesso root e recuperando informazioni sensibili.

### Raccomandazioni Immediate
1. **Correggere SQL Injection:** Implementare prepared statements e input validation
2. **Rivedere privilegi sudo:** Rimuovere NOPASSWD per utente peter
3. **Cambiare tutte le password:** Utilizzare password complesse e uniche
4. **Cifrare database:** Implementare hashing sicuro per le password
5. **Modificare metodo form:** Utilizzare POST invece di GET per il login
6. **Segregazione servizi:** Evitare riutilizzo credenziali tra servizi diversi

### Priorità
**URGENTE:** Le vulnerabilità identificate permettono compromesso completo del sistema e devono essere risolte immediatamente prima di qualsiasi deployment in produzione.