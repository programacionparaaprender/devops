print('hola mundo')
# pip install azure-cosmos
# https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started

import os
os.getcwd()


from azure.cosmos.aio import CosmosClient as cosmos_client
from azure.cosmos import PartitionKey, exceptions
import asyncio
import family



