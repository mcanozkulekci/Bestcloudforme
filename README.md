# Bestcloudforme cases documentation


## Installation
```bash
git clone https://github.com/mcanozkulekci/Bestcloudforme.git
```

## Building Image
```bash
$ sudo docker build -t <IMAGE NAME> .
```

## Running Container
Here, if you run the image, you need to add your specific Webhook URL into <DUMMY WHOOK> part of the command. For example : --env URL_WHOOK = "http://webhook.site/...etc"
```bash
$ sudo docker run --name <CONTAINER NAME> --env URL_WHOOK=<DUMMY WHOOK> -p <DESIRED PORT>:5000 -d <IMAGE NAME>
```


## For POST Request into Webhook.site

```
curl --header "Content-Type: application/json" --request POST --data '<JSON DATA>' http://localhost:<DESIRED PORT>/alert
```
In our example, I will send my name and surname as json data like below:
```
curl --header "Content-Type: application/json" --request POST --data '{"firstname":"mehmetcan","lastname":"ozkulekci"}' http://localhost:<DESIRED PORT>/alert
```
## Deployment

Ingress Controller is an application that runs in a Kubernetes cluster and configures an HTTP load balancer according to Ingress Resources. It uses Nginx. The load balancer can be a software load balancer running in the cluster or a hardware or cloud load balancer running externally. Different load balancers require different Ingress Controller implementations.

In GKE, an Ingress object defines rules for routing HTTP(S) traffic to applications running in a cluster.

When you create an Ingress object, the GKE Ingress controller creates a Google Cloud HTTP(S) Load Balancer and configures it according to the information in the Ingress and its associated Services.

Since Google Cloud is a paid service, I have chosen 90-day, $300 Free Trial. Then I deployed my app using Google Cloud Kubernetes Engine. I created a Kubernetes cluster which has a name "flask-cluster".You can see details below.

Name | Location | Number of Nodes | Total vCPUs | Total memory | 
--- | --- | --- | --- |--- 
flask-cluster | europe-central2-b | 3 | 6 | 12GB | 289 | 285 | 287 | 287 | 272 | 276 | 269


##
In order to manipulate Google Cloud, I used my Google Cloud SDK of my Ubuntu Operating System's Terminal.

```
gcloud config set project trying-mcan-1
```

## Important Note
In the replication-set.yaml file, URL_WHOOK environment variable is defined. You might need to change its value for personal usage.

For deploying our app to Google Cloud Kubernetes Engine, executing of the following commands are required.

```
kubectl create -f ./kubernetes/load-balancer.yaml
kubectl create -f ./kubernetes/replication-set.yaml
kubectl create -f ./kubernetes/ingress-gke.yaml

```
## Accessing Final Website
http://34.116.205.106:5000/whoami?firstname=Mehmetcan&lastname=Ozkulekci
