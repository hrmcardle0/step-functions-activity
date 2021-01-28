activity_name="$1_activity"
$activity_arn = aws stepfunctions create-activity --name $activity_name | jq '.activityArn' | sed 's/"//g'
echo "Activity ARN: $activity_arn"