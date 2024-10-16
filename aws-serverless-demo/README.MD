1. Install AWS CLI 
2. AWS Configure access from CLI to your AWS account (This will autorize boto3)
```bash
aws configure
```
3. Write your Lambda
4. Create a Dockerfile
5. Build your docker

6. 
```bash
docker build -t <repository_name>:<tag> .
```

7. Test your docker
```bash
docker run -p 9000:8080 <repository_name>:<tag>
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

8. Push the Docker image to ECR (upload_to_ecr.py)
9. Create approriate IAM role for the Lambda (and Policy if needed)
10. Create the Lambda function with the image in ECR and the IAM role
11. Invoke the Lambda function using boto3 or using the requests package in python.


GUI Nie bylo widac!!!

