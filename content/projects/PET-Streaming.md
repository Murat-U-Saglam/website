---
title: "PET Streaming"
date: 2023-08-15T10:45:36+01:00
tags: [FL]
---

## What is PET-Streaming

The aim of this project is to provide privacy enchanging technology. Current goals are

#### Input

Take a stream of cloud data

#### Process

Anonymise the data

Check if the data within the stream and does appropiate validation - (Does not store) (Catalogue - is verifiied against a list of data assets and data controls)

#### Output

Send the anonymise data to the end user.

### Usecase

The aim is to be able to to take PII data, and provide an api to the dataowner to enable the utilisation of the data by any organisation that they deem fit, without having to worry about the misuse of PII and the end user can ensure the data integrity

Developments to POC

- Work with json, CSV or anything else
- create an access control panel
- Audit record of changes - Store locally back to dataowner
- Have a key management system

Second iteration

- Create file based interface from storage
- Create a different json implementation with stream data
- This will require a message broker
- Sync all changes to the audit recorder
- Fuzzy search for PII identifiers in the key of the data

At all stages

- Data Platform End user should have anonymised data
- psedo anonymised data
- identifiable data
- no PII
