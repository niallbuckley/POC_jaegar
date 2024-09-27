# Define variables for the services
SERVICE_A_NAME = service-a
SERVICE_B_NAME = service-b
DOCKER_TAG = latest

# Build the Docker images
.PHONY: build
build: build-service-a build-service-b

build-service-a:
	docker build -t $(SERVICE_A_NAME):$(DOCKER_TAG) -f service-a/Dockerfile .

build-service-b:
	docker build -t $(SERVICE_B_NAME):$(DOCKER_TAG) -f service-b/Dockerfile .

# Push the Docker images (Optional if needed in the future)
.PHONY: push
push: push-service-a push-service-b

push-service-a:
	docker push $(SERVICE_A_NAME):$(DOCKER_TAG)

push-service-b:
	docker push $(SERVICE_B_NAME):$(DOCKER_TAG)

# Deploy to Kubernetes
.PHONY: deploy
deploy: deploy-service-a deploy-service-b

deploy-service-a:
	kubectl apply -f service-a.yaml

deploy-service-b:
	kubectl apply -f service-b.yaml

# Clean up resources
.PHONY: clean
clean:
	kubectl delete -f service-a.yaml
	kubectl delete -f service-b.yaml

