#Date: 12/13/2020
#Author: hrmcardle0@yahoo.com
#Description: This function represents an activity portion of a task for AWS StepFunctions.
#This script continously polls the StepFunction API for new activities for your task.
#Activities allow you to perform work on a separate server then send the response back
#to the AWS StepFunctions API

import boto3
import json
import time
import subprocess
import logging

#initialize clients and setup logger
client = boto3.client('stepfunctions')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


#converts object into extractable json values based on key
def json_values(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

#contiously loop looking for activities
logger.info("Getting Activity...")
while (1):

    #list current activities, retreive vales 
    response = client.list_activities(maxResults=123)
    activity_name = json_values(response,'name')
    activity_arn = json_values(response,'activityArn')
    
    #get task associated with activity
    #print("Availale User : {} Arn: {}", activity_name[0],activity_arn[0])
    response = client.get_activity_task(activityArn = activity_arn[0])

    #get task token to send back to StepFunctions API signalin completion
    task_token = json_values(response,'taskToken')
    tasktoken = task_token[0]
    logger.info("Task token: ",tasktoken)
    
    #retreive input
    inputs = json_values(response,'input')
    inputs = json.loads(inputs[0])
    logger.info("Inputs: {}".format(inputs))
    
    #loop through input values to echo back
    values = []
    for i in inputs :
         values.append(inputs[i]+'')
    fname = ""
    for value in values:
        fname += ' '+value
    opt = fname[1:]
    
    #format output to send back to client
    opt = ('"'+opt+'"')

    ## do our actual task work here ##
    output = subprocess.call(['./script.sh'])
    ## end task work ##
    logger.info("Work is complete. Output: {}".format(output))

    #work is complete, alert step-function that wer are finished with this activity
    response = client.send_task_success(taskToken = tasktoken, output = opt)
    logger.info(response)
    time.sleep(5)
