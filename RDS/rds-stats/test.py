
import json



sample = {u'DBInstances': [{u'PubliclyAccessible': False, u'MasterUsername': 'dmansfieldlab2', u'MonitoringInterval': 0, u'LicenseModel': 'general-public-license', u'VpcSecurityGroups': [{u'Status': 'active', u'VpcSecurityGroupId': 'sg-0eb8ee99469dcb85f'}], u'InstanceCreateTime': datetime.datetime(2018, 9, 24, 21, 34, 1, 71000, tzinfo=tzutc()), u'CopyTagsToSnapshot': True, u'OptionGroupMemberships': [{u'Status': 'in-sync', u'OptionGroupName': 'default:mysql-5-7'}], u'PendingModifiedValues': {}, u'Engine': 'mysql', u'MultiAZ': False, u'LatestRestorableTime': datetime.datetime(2018, 9, 26, 21, 50, tzinfo=tzutc()), u'DBSecurityGroups': [], u'DBParameterGroups': [{u'DBParameterGroupName': 'default.mysql5.7', u'ParameterApplyStatus': 'in-sync'}], u'PerformanceInsightsEnabled': False, u'AutoMinorVersionUpgrade': True, u'PreferredBackupWindow': '06:20-06:50', u'DBSubnetGroup': {u'Subnets': [{u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-d327eded', u'SubnetAvailabilityZone': {u'Name': 'us-east-1e'}}, {u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-01532b0e', u'SubnetAvailabilityZone': {u'Name': 'us-east-1f'}}, {u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-6aad2044', u'SubnetAvailabilityZone': {u'Name': 'us-east-1a'}}, {u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-e296c0a8', u'SubnetAvailabilityZone': {u'Name': 'us-east-1b'}}, {u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-32b4376e', u'SubnetAvailabilityZone': {u'Name': 'us-east-1c'}}, {u'SubnetStatus': 'Active', u'SubnetIdentifier': 'subnet-fc880e9b', u'SubnetAvailabilityZone': {u'Name': 'us-east-1d'}}], u'DBSubnetGroupName': 'default', u'VpcId': 'vpc-73b46609', u'DBSubnetGroupDescription': 'default', u'SubnetGroupStatus': 'Complete'}, u'ReadReplicaDBInstanceIdentifiers': [], u'AllocatedStorage': 20, u'DBInstanceArn': 'arn:aws:rds:us-east-1:753955134882:db:dmansfieldlab2', u'BackupRetentionPeriod': 7, u'DBName': 'dmansfieldlab2', u'PreferredMaintenanceWindow': 'sun:07:58-sun:08:28', u'Endpoint': {u'HostedZoneId': 'Z2R2ITUGPM61AM', u'Port': 3306, u'Address': 'dmansfieldlab2.czekuou2uqdd.us-east-1.rds.amazonaws.com'}, u'DBInstanceStatus': 'available', u'IAMDatabaseAuthenticationEnabled': False, u'EngineVersion': '5.7.22', u'AvailabilityZone': 'us-east-1f', u'DomainMemberships': [], u'StorageType': 'gp2', u'DbiResourceId': 'db-7PKXEJ3CY2FRNKZ6NUJJR4L37Q', u'CACertificateIdentifier': 'rds-ca-2015', u'StorageEncrypted': False, u'DBInstanceClass': 'db.t2.micro', u'DbInstancePort': 0, u'DBInstanceIdentifier': 'dmansfieldlab2'}], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '06fc5da6-e82c-4dd3-bf26-8b1d345a587a', 'HTTPHeaders': {'x-amzn-requestid': '06fc5da6-e82c-4dd3-bf26-8b1d345a587a', 'content-type': 'text/xml', 'content-length': '5124', 'vary': 'Accept-Encoding', 'date': 'Wed, 26 Sep 2018 21:56:50 GMT'}}}

with open('result.json', 'w') as fp:
    json.dump(sample, fp)
