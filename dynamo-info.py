import boto3
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Recipe-Manager')
numRecipes = table.item_count
print(f"You have {numRecipes} saved recipes.")

response = table.get_item(
    Key={
        'recipe-name': 'Spaghetti',
        #'last_name': 'Doe'
    }
)
item = response['Item']
cook_time = item['cook-time']
print(cook_time)