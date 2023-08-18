import boto3

client = boto3.client('ecr')

response = client.create_repository(repositoryName="my-test-repo")
repo_url = response['repository']['repositoryUri']
print(repo_url)