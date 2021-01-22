# Using AWS Step Functions Task Activities in Python

This example written in Python demonstrates how to use AWS step functions to perform a task on multiple entitries in an array. Instead of using lambda functions, it uses a task activity, where a Python script continously polls the step functions for input. Once it receives this input, it generates a token for that task, performs a task (such as running a script), then sends the token back to the script signaling task completion. 

## **Solution Overview**
