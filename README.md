# Kubernetes HPA Autoscaling Approach based on PID Control Algorithm

This is a Kubernetes HPA auto-scaling algorithm project based on the PID controller design. 
The project consists of two main parts: the algorithm execution and the microservice configuration for testing.

## Folder Structure

```plaintext
├── Algorithm
│   ├── Code
│   ├── importantData
│   ├── src
│   ├── README.md
├── Demo-MicroService
│   ├── release
│   ├── README.md
├── README.md
```

## Algorithm folder
This folder contains code practices for implementing and executing PIDC-HPA. You can find detailed instructions in the README.md file.

- Code: contains the code for PIDC-HPA.
- importantData: Contains the authentication file format required to run the code.
- src: Implementation of each component of the PIDC-HPA algorithm.

## Demo-MicroService Folder
This folder contains the YAML configuration files of the MicroService for testing. You can find detailed instructions in the README.md file.

- release: yaml file for configuration.
