# Make docker ps better
alias ds='docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.State}}\t{{.Status}}\t{{.Ports}}"'

# kill running container
alias dk='docker kill'
# remove container
alias drm='docker rm'

# show images
alias dimg='docker images'
# remove image
alias drmi='docker rmi'

# Kill and remove docker container
function dkrm(){
	for container in "$@"
	do
		docker kill $container
		docker rm $container
	done
}

# remove all stopped containers:
alias drmstp='docker rm $(docker ps -a -q)'

# Clean out images (removed untagged)
alias drmiu='docker rmi $(docker images | awk "/^<none>/ {print $3}")'

# Bash into container
function dex(){
	docker exec -i -t $1 /bin/bash
}

# docker-compose commands
alias dc='docker-compose -f'
alias dcup='docker-compose -f /opt/docker-compose.yml up -d'
alias dcdown='docker-compose -f /opt/docker-compose.yml down'
alias dcstart='docker-compose -f /opt/docker-compose.yml start'
alias dcstop='docker-compose -f /opt/docker-compose.yml stop'
alias dcrestart='docker-compose -f /opt/docker-compose.yml restart'
alias dcrebuild='docker-compose -f /opt/docker-compose.yml up -d --build'
alias dclog='docker-compose -f /opt/docker-compose.yml logs --tail=50'
alias dcflog='docker-compose -f /opt/docker-compose.yml logs -f --tail=10'
alias dcpull='docker-compose -f /opt/docker-compose.yml pull'