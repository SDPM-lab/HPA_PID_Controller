
## Introduction
This example microservice is an example from GCP, the detailed application is linked [here](https://github.com/GoogleCloudPlatform/microservices-demo
).

Here is the basic application architecture, later you need to install the related monitoring suite to use, you can implement it in the public cloud or local clusters

## Quickstart on Kubernetes 
1. Ensure Requirements:
   - A Kubernetes Cluster (install with Kubeadm)
   - Shell environments: `git`, and `kubectl`.
   - Clone Repo
2. Create Namespace:
   ```sh
   kubectl create namespace onlineshop
   ```
3. Deploy Online Boutique to the cluster.

   ```sh
   kubectl apply -f ./Demo-MicroService/release/kubernetes-manifests.yaml -n onlineshop
   ```
4. Access the web frontend in a browser using the frontend's external IP.

   ```sh
   echo -n "http://" && kubectl get svc frontend-external -n onlineshop -o json | jq -r '.status.loadBalancer.ingress[0].ip'
   ```
   
5. Delete the Project.

   ```sh
   kubectl delete ns onlineshop
   ```

## Quickstart on Cloud (GKE for example )

1. Ensure you have ready requirements:
   - [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).
   - Shell environment : `gcloud`, `git`, and `kubectl`.
   - Clone the Repo

2. Confirm the services have been enabled for your project.

   ```sh
   gcloud services list --enabled --project=${PROJECT_ID}
   ```

3. Create a GKE cluster and get the credentials for it.

   ```sh
    export PROJECT_ID=${PROJECT_ID}
    export CLUSTER=${CLUSTER}
    export ZONE=northamerica-northeast1-a
    export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format='get(projectNumber)')
    gcloud services enable container.googleapis.com
    gcloud container clusters create ${CLUSTER} \
        --zone ${ZONE} \
        --machine-type=e2-standard-4 \
        --workload-pool ${PROJECT_ID}.svc.id.goog \
        --enable-dataplane-v2 \
   ```

   Creating the cluster may take a few minutes.

4. Deploy Online Boutique to the cluster.

   ```sh
   kubectl create namespace onlineshop
   kubectl apply -f ./Demo-MicroService/release/kubernetes-manifests.yaml -n onlineshop
   ```

5. Wait for the pods to be ready.

   ```sh
   kubectl get pods
   ```

   After a few minutes, you should see the Pods in a `Running` state:

   ```
   NAME                                     READY   STATUS    RESTARTS   AGE
   adservice-76bdd69666-ckc5j               1/1     Running   0          2m58s
   cartservice-66d497c6b7-dp5jr             1/1     Running   0          2m59s
   checkoutservice-666c784bd6-4jd22         1/1     Running   0          3m1s
   currencyservice-5d5d496984-4jmd7         1/1     Running   0          2m59s
   emailservice-667457d9d6-75jcq            1/1     Running   0          3m2s
   frontend-6b8d69b9fb-wjqdg                1/1     Running   0          3m1s
   loadgenerator-665b5cd444-gwqdq           1/1     Running   0          3m
   paymentservice-68596d6dd6-bf6bv          1/1     Running   0          3m
   productcatalogservice-557d474574-888kr   1/1     Running   0          3m
   recommendationservice-69c56b74d4-7z8r5   1/1     Running   0          3m1s
   redis-cart-5f59546cdd-5jnqf              1/1     Running   0          2m58s
   shippingservice-6ccc89f8fd-v686r         1/1     Running   0          2m58s
   ```

6. Access the web frontend in a browser using the frontend's external IP.

   ```sh
   echo -n "http://" && kubectl get svc frontend-external -n onlineshop -o json | jq -r '.status.loadBalancer.ingress[0].ip'
   ```

   Visit `http://EXTERNAL_IP` in a web browser to access your instance of Online Boutique.

7. After done with it, delete the GKE cluster.

   ```sh
   gcloud container clusters delete online-boutique \
     --project=${PROJECT_ID} --region=${REGION}
   ```


Deleting the cluster may take a few minutes.
