import boto3

def check_connectivity():
    print("Connecting to AWS via Python...")
    # This will use the IAM Role if run on EC2
    s3 = boto3.client('s3')
    try:
        buckets = s3.list_buckets()
        print(f"Connection Successful! Found {len(buckets['Buckets'])} buckets.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_connectivity()