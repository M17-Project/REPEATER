img:
	docker build . -t repeater
dev:
	#if you get "400 bad request" you need to make sure to set
	#DEBUG=1 in environment variables
	docker run --rm -it \
		-p 8080:8080 \
		-v ${shell pwd}/app/:/app/\
		repeater /bin/bash

fly:
	flyctl deploy --local-only


#dboverride:
	#run following on host
	#flyctl proxy 5432 -a repeater-db
	#socat TCP-LISTEN:5433,fork TCP:localhost:5432
	#you need the socat port redirection because flyctl proxy won't
	#listen on anything except 127.0.0.1, but you need it to allow
	#for connections from the docker container.

	#then you can run make dev,
	#set DATABASE_URL with correct username and password
	#and do anything with the database you need to
