# RESOCONTO FINALE PENETRATION TEST

**Target:** 127.0.0.1  
**Periodo:** 9 Settembre 2025, 00:22:40 - 00:28:30 (durata: ~6 minuti)

## RIEPILOGO DELLE FASI ESEGUITE

Il penetration test è stato condotto attraverso tre fasi principali:

### 1. Reconnaissance
- Scansione delle porte con nmap per identificare servizi attivi
- Banner grabbing per determinare versioni specifiche dei servizi
- Identificazione del sistema operativo target

### 2. Web Scanner
- Enumerazione delle directory web con gobuster
- Analisi approfondita dei file sensibili esposti
- Raccolta di informazioni critiche dalle configurazioni web

### 3. Privilege Escalation
- Accesso SSH utilizzando credenziali compromesse
- Enumerazione dei binari SUID per escalation privilegi
- Sfruttamento di vulnerabilità locali per accesso root

## SERVIZI E TECNOLOGIE RILEVATI

**Servizi di Rete:**
- **SSH (porta 22):** OpenSSH 10.0p2 Debian 8
- **HTTP (porta 80):** Apache httpd 2.4.65 su Debian

**Stack Tecnologico:**
- **Sistema Operativo:** Linux Debian
- **Server Web:** Apache 2.4.65
- **Linguaggio:** PHP 8.4.11
- **Applicazione:** "Prova sito per progetto web applications"

## VULNERABILITÀ CRITICHE IDENTIFICATE

### 1. Information Disclosure Critica
- **File info.php:** Espone phpinfo() completo con variabili d'ambiente sensibili
- **Endpoint /server-status:** Accessibile pubblicamente, rivela informazioni dettagliate di Apache
- **Impatto:** Esposizione di credenziali database e configurazioni sensibili

### 2. Credenziali Deboli
- **Database:** username "gianni" / password "gianni"
- **SSH:** Stesse credenziali riutilizzate per accesso sistema
- **Fonte:** Variabili d'ambiente esposte tramite phpinfo()

### 3. Privilege Escalation via SUID
- **Binario vulnerabile:** `/usr/local/bin/file_reader`
- **Permessi:** rwsr-xr-x (SUID bit attivo, proprietario root)
- **Sfruttamento:** Permette lettura di file con privilegi root

## FLAG TROVATA

**🚩 Flag recuperata con successo:**
- **Contenuto:** `flag{4g3n7ic_a1_rul3z}`
- **Posizione:** `/home/gianni/flag.txt`
- **Metodo:** Sfruttamento binario SUID per lettura file protetti

## CONSIDERAZIONI E RACCOMANDAZIONI CONCLUSIVE

### Criticità Immediate
1. **Rimuovere immediatamente** il file info.php dall'ambiente di produzione
2. **Disabilitare** l'endpoint /server-status o limitarne l'accesso
3. **Cambiare** le credenziali database con password complesse
4. **Rimuovere** o correggere i permessi del binario `/usr/local/bin/file_reader`

### Raccomandazioni di Sicurezza
- Implementare politiche di password robuste
- Configurare il web server per non esporre informazioni sensibili
- Effettuare audit regolari dei binari SUID
- Separare le credenziali tra servizi diversi
- Implementare principio del minimo privilegio

### Valutazione Complessiva
Il sistema presenta **vulnerabilità critiche** facilmente sfruttabili che hanno permesso un compromesso completo in meno di 6 minuti. La combinazione di information disclosure e riutilizzo credenziali ha reso il sistema estremamente vulnerabile.

**Livello di Rischio:** **CRITICO** - Intervento immediato necessario.