## virtial environment set-up
```
python -m venv deploy-aws-cdk-env
```
```
deploy-aws-cdk-env/Script/activate
```
```
pip install aws-cdk.core
```
```
pip install constructs
```
### Vertify CDK Version
```
cdk --version
```
### Initializating CDK Project
```
cdk init --language python
```

### Initializing deployment
```
.\source.bat
```
```
pip install -r requirements.txt
```
```
cdk synthesize
```
### Bootstrap with Default Profile and deploy
```
cdk bootstrap
```
```
cdk deploy
```

### Bootstrap with Specific Profile and Deploy
```
cdk bootstrap your_profile
```
```
cdk deploy your_profile
```