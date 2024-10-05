### To install
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install cassandra bitnami/cassandra


Cassandra deploys a secret to kubectl. To get the secret simply tun command:
`kubectl get secret <cassandra-secret-name> -o yaml `


You also need to create a keyspace in the cassandra database 

log in to cassandra: 
Get password: 
`kubectl get secret cassandra -o jsonpath="{.data.cassandra-password}" -n jaeger-namespace | base64 --decode`

Create keyspace:
`CREATE KEYSPACE IF NOT EXISTS jaeger_v1_test WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };`

Verify:
`DESCRIBE KEYSPACES;`


### Using Docker

## Service-c
docker build -f service-c/Dockerfile -t service-c .
docker run -d --name service-c --network jaeger-network -p 5000:5000 service-c

## All-in-one jaeger
docker run -d --name jaeger --network jaeger-network  -e COLLECTOR_ZIPKIN_HTTP_PORT=9411   -p 5775:5775/udp   -p 6831:6831/udp   -p 6832:6832/udp   -p 5778:5778   -p 16686:16686   -p 14268:14268   -p 9411:9411   jaegertracing/all-in-one:1.6.0

## Test
curl 'http://localhost:5000/service-c'
