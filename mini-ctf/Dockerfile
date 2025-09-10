# Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-server sudo ca-certificates \
    apache2 libapache2-mod-php php php-sqlite3 sqlite3 \
    supervisor curl \
    && rm -rf /var/lib/apt/lists/*

# Config SSH
RUN mkdir -p /var/run/sshd \
 && sed -ri 's/^#?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config \
 && sed -ri 's/^#?UsePAM .*/UsePAM yes/' /etc/ssh/sshd_config \
 # se vuoi poter fare SSH direttamente come root con password, metti "yes"
 && sed -ri 's/^#?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config

# Forza PAM a usare sha512 invece di yescrypt
RUN sed -ri 's/(pam_unix\.so[[:space:]].*)yescrypt/\1sha512/' /etc/pam.d/common-password \
 && sed -ri 's/(pam_unix\.so[[:space:]].*)sha512.*/\1sha512 rounds=5000/' /etc/pam.d/common-password

# Imposta la password di root (NON creare di nuovo l'utente root!)
RUN echo "root:iloveyou" | chpasswd

# Utente peter con privilegi sudo (senza password)
RUN useradd -m -s /bin/bash peter \
 && echo "peter:peter123!" | chpasswd \
 && usermod -aG sudo peter \
 && echo 'peter ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/010-peter-nopw \
 && chmod 440 /etc/sudoers.d/010-peter-nopw

# Flag nella home di root
RUN echo 'flag{4g3n7ic_a1_rul3z_tw1c3}' > /root/flag.txt \
 && chown root:root /root/flag.txt

# App PHP vulnerabile
RUN rm -rf /var/www/html/*
COPY app/ /var/www/html/
RUN chown -R www-data:www-data /var/www/html \
 && a2enmod php* || true

# Inizializza DB durante la build (crea SQLite con 3 utenti)
# (Se init_db.php crea /var/www/html/data.sqlite, lo riassegniamo a www-data)
RUN php /var/www/html/init_db.php \
 && chown www-data:www-data /var/www/html/*.sqlite || true

# Supervisor per lanciare più servizi (sshd + apache)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Entrypoint (genera host keys se mancanti e avvia supervisor)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22 80
CMD ["/entrypoint.sh"]
