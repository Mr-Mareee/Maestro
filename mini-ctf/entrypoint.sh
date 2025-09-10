#!/usr/bin/env bash
set -e

# Genera host keys SSH se mancanti
if [ ! -f /etc/ssh/ssh_host_rsa_key ]; then
  ssh-keygen -A
fi

# Assicurati che il DB esista (idempotente)
php /var/www/html/init_db.php >/dev/null 2>&1 || true

exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
