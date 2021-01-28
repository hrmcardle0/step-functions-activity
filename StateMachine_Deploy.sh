aws stepfunctions create-state-machine --name $1 --definition file://src/step-functions-definition.json --role-arn $2
