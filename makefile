img:
	docker build . -t repeater
dev:
	#if you get "400 bad request" you need to make sure to set
	#DEBUG=1 in environment variables
	docker run --rm -it \
		-p 8080:8080 \
		-v ${shell pwd}/app/:/app/\
		repeater /bin/bash

