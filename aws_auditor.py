def audit_s3(bucket_public):
    if bucket_public:
        print("Warning: Public S3 bucket detected!")
    else:
        print("S3 bucket is secure.")

def audit_iam(admin_access):
    if admin_access:
        print("Warning: User has full admin access!")
    else:
        print("IAM permissions look secure.")

print("AWS Cloud Security Auditor")
audit_s3(True)
audit_iam(False)
