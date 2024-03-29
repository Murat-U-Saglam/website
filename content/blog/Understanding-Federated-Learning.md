---
title: "Understanding Federated Learning"
date: 2023-09-14T10:15:57+01:00
tags: ["FL"]
---

# What is Federated learning (FL)

FL aims to train NN via utilising locally trained models and aggregating a global model. This can be done via a variety of networking paradigms most notably centralised and decentralised aggregation.

1. **Setup and Initialisation:**

   - Establish a central server (if centralised) and multiple client devices or nodes.
   - Define the machine learning model architecture and hyperparameter.

2. **Data Partitioning:**

   - Each client retains control of its data locally, ensuring data privacy.
   - Clients perform initial preprocessing and data partitioning (e.g. splitting datasets into mini-batches).

3. **Communication Setup:**

   - Establish secure communication channels between clients and the central server (if centralised).
   - Ensure encryption and authentication mechanisms to protect data in transit.

4. **Model Initiation:**

   - The central server initiates by sending an initial model (often pre-trained) to all clients.

4.5. **Model Initiation - Decentralised**

- local models train on local dataset rather than fine tuning data the initial global model.

5. **Local Model Training:**

   - Clients perform local model training on their respective datasets using the received model.
   - Training can include multiple epochs, gradient descent, and other optimisation techniques. (Having consistency across all client models saves headaches and within a decentralised approach it's extremely difficult to aggregate different model architectures.)

6. **Model Updates:**

   - After local training, clients compute model updates (gradients) based on their data.
   - These updates are sent securely to the central server or selected peers(decentralised).

7. **Aggregation at the Central Server:**

   - The central server aggregates the received model updates, typically using techniques like Federated Averaging.
   - It updates the global model with the aggregated gradients.

7.5. **Aggregation Mechanism - Decentralised training:**

- Decentralised training requires a consensus mechanism which can aggregate local models in clusters
- Use consensus algorithms (e.g. Federated Byzantine Agreement) to agree on a global model.
- Ensure that all clients eventually converge to a similar model.

8. **Iterative Process:**

   - Steps 5-7 are repeated iteratively for a predefined number of rounds or until convergence.
   - The model's performance improves with each round as it learns from diverse data sources.

9. **Model Evaluation and Deployment:**

   - The final global model is evaluated for performance.
   - Once satisfactory, the model can be deployed for inference tasks.

### Sharing biases

You may of noticed there is no mentioning of sharing biases, this is due to the following reasons:

**Data Distribution Variability**: In FL, clients have different datasets, which can vary significantly in terms of data distribution, characteristics, and biases. Sharing bias terms directly across clients could lead to models that do not work well to all data sources. Local biases allow models to adapt to the idiosyncrasies of each client's data but doesn't convey the same benefits to global models.

**Privacy and Security**: Federated Learning is designed to maintain data privacy and security. Sharing bias terms could potentially reveal sensitive information about a client's data ([Gradient-Based Inference Attack]({{< ref "/blog/Attacking-ML-Models.md" >}})). By keeping biases local, it ensures that no client can access or infer another client's bias information.

**Model Flexibility**: Local biases enable each client to fine-tune the model according to its specific data. This increases the flexibility of the model and its ability to capture client-specific patterns and nuances. Sharing biases would limit this adaptability.

**Reduced Communication Overhead**: Sharing bias terms in addition to model weights would increase the communication overhead in Federated Learning, especially in scenarios with a large number of clients. Minimising the data exchanged between clients and the central server is a key efficiency concern.
