# nextcloud maintenance mode commands
alias ncmaintmodeon='docker exec --user abc nextcloud php /config/www/nextcloud/occ maintenance:mode --on'
alias ncmaintmodeoff='docker exec --user abc nextcloud php /config/www/nextcloud/occ maintenance:mode --off'