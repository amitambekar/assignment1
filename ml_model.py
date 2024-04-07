# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
import boto3
import os
from models import Tenant, ProjectMetadata

TARGET_COLUMN = os.getenv('TARGET_COLUMN')
FILEPATH = os.getenv('FILEPATH')
BUCKET = os.getenv('BUCKET')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')


def upload_to_s3(bucket, filename, file_body):
    client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    return client.put_object(Bucket=bucket, Key=filename,Body=file_body)


def modify_data(filepath):
    data = pd.read_csv(filepath) 
    data.index = data['cars']
    del data['cars']
    return data


def run_model(filepath):
    # Step 2: Load Data
    data = modify_data(filepath)
    # Step 3: Prepare Data
    X = data.drop(columns=[TARGET_COLUMN])  
    y = data[TARGET_COLUMN]
    
    # Step 4: Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 5: Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 6: Evaluate model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    columns = X.columns.tolist()
    return model, mse, columns


def save_model(model, filename):
    return upload_to_s3(BUCKET, filename, file_body=pickle.dumps(model))


def create_model():
    model_filename = "model.save"
    model, mse, columns = run_model(filepath=FILEPATH)
    save_model(model=model, filename=model_filename)

    tenant_dict = {"columns": columns}
    tenant_resource = Tenant(**tenant_dict)
    tenant_resource.save()
    metadata = {
        "tenant_id": tenant_resource.id,
        "file_location": FILEPATH,
        "s3_uploaded_model_location": BUCKET + "/" + model_filename,
        "model_evalution_result": mse
    }

    project_metadata_resource = ProjectMetadata(**metadata)
    project_metadata_resource.save()
    return project_metadata_resource.id

# run()
# # Step 6: Evaluate Model
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(f'Mean Squared Error: {mse}')