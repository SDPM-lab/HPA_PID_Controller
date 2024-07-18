## QuickStart

### Requirements: 
- Python (3.7+ required)
- Kubernetes Cluster with Kubectl (requires 1.26+)

### Additional Required Installation Components:
- Metric Server
- Sidecar
- Prometheus

### GCP dependencies
- google-api-core 2.19.0
- Google-auth 2.29.0
- Google Cloud Containers 2.45.0
- googleapis-common-protos 1.63.0

### How to Use

1. Enter the Load Generator Container and run the Locust file.

   ```sh
   locust -f locust.py
   ```
   After execution, enter the UI and enter the Frontend URL and compression force.
   
2. Run the Python file for AutoScaling.

   ```sh
   QuickUpSlowDown.py
   ```