# My CDK App

This is a sample AWS CDK application written in Python. This project demonstrates how to define and deploy AWS resources using the AWS Cloud Development Kit (CDK).

## Project Structure

```
my-cdk-app
├── my_cdk_app
│   ├── __init__.py
│   └── my_cdk_app_stack.py
├── app.py
├── cdk.json
├── requirements.txt
├── README.md
└── tests
    ├── __init__.py
    └── test_my_cdk_app.py
```

## Setup Instructions

1. **Install AWS CDK**: Make sure you have the AWS CDK installed. You can install it globally using npm:

   ```
   npm install -g aws-cdk
   ```

2. **Install Python Dependencies**: Navigate to the project directory and install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. **Bootstrap your AWS environment** (if you haven't already):

   ```
   cdk bootstrap
   ```

## Usage

To deploy the stack, run the following command:

```
cdk deploy
```

To synthesize the CloudFormation template, use:

```
cdk synth
```

## Running Tests

To run the unit tests for the CDK stack, use:

```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.