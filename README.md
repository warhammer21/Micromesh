# MicroMesh Project

## Overview

MicroMesh is a project aimed at understanding and debugging connectivity issues between microservices in a Kubernetes cluster. This project covers fundamental networking concepts, allowing for hands-on experimentation with various network configurations and scenarios.

## Setup Instructions

1. **Environment Setup:**
   - Ensure you have a Kubernetes cluster running (e.g., using Minikube or a cloud provider).
   - Install `kubectl` and ensure it's configured to access your cluster.

2. **Deploying Microservices:**
   - Create deployment YAML files for the Flask API and PostgreSQL database.
   - Apply the configurations using `kubectl apply -f <file>.yaml`.

3. **Service Configuration:**
   - Create a LoadBalancer service for the Flask API to expose it externally.
   - Ensure the service selector matches the labels used in the Flask deployment.

## Tests Conducted

Throughout the project, we conducted various tests to simulate network issues and understand their implications. The following scenarios were implemented:

1. **Network Policy Denies Traffic:**
   - **Action:** Created a Network Policy to deny ingress traffic to the Flask API.
   - **Expected Outcome:** The Flask API was isolated from external traffic, simulating an environment where no requests could reach it.

2. **Service Selector Mismatch:**
   - **Action:** Modified the Flask service YAML to use a non-existent label.
   - **Expected Outcome:** The LoadBalancer service could not route traffic to the Flask pods, leading to connection errors.

3. **DNS Resolution Issues:**
   - **Action:** Simulated a DNS resolution failure by modifying the CoreDNS configuration.
   - **Expected Outcome:** The Flask API logs indicated it could not resolve the database hostname, demonstrating the importance of DNS in microservices communication.

4. **Testing Egress Traffic:**
   - **Action:** Experimented with Network Policies to control egress traffic from the database.
   - **Expected Outcome:** Determined how to restrict or allow outbound traffic based on policy settings.

5. **Load Balancer Functionality:**
   - **Action:** Verified that the LoadBalancer service could expose the Flask API externally and handle incoming requests.
   - **Expected Outcome:** Successful connectivity to the Flask API from external clients.

6. **Service Discovery Validation:**
   - **Action:** Ensured that all services could resolve each other using their DNS names.
   - **Expected Outcome:** Confirmed that the Flask API could successfully connect to the PostgreSQL database using its DNS name.

7. **Resource Monitoring:**
   - **Action:** Monitored resource usage and connectivity status of pods and services.
   - **Expected Outcome:** Gained insights into how network policies and configurations impacted resource utilization.

8. **Network Policy Testing:**
   - **Action:** Applied and removed various Network Policies to observe their effects on service communication.
   - **Expected Outcome:** Enhanced understanding of how Kubernetes network policies can secure or disrupt traffic flow.

## Conclusion

The MicroMesh project provided a hands-on approach to understanding Kubernetes networking fundamentals. By simulating and debugging various connectivity issues, we gained practical insights into microservices communication, DNS resolution, and network policies. 

## Future Work

Future iterations of the project may explore more advanced networking concepts, such as service meshes, traffic shaping, and load testing in a microservices architecture.

