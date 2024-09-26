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
