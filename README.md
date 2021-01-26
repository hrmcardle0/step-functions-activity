# Using AWS Step Functions Task Activities in Python

This example written in Python demonstrates how to use AWS step functions to perform a task on multiple entitries in an array. Instead of using lambda functions, it uses a task activity, where a Python script continously polls the step functions for input. Once it receives this input, it generates a token for that task, performs a task (such as running a script), then sends the token back to the script signaling task completion. 

Activities can be used when you want to have a 3rd party non-AWS resource complete the task instead of relying on AWS services. They are commonly used in place of lambda functions lambda has a finite run time and limited memory allocation. 

Step Functions have a ton of different use cases and help to visualize the workflow of an application. 

## **Solution Overview**

![Solution Diargram](https://raw.ithubusercontent.com/hrmcardle0/step-functions-activity/main/diagram.png)