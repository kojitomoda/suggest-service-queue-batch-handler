from typing import Dict, Any, TypedDict, List

class SQSMessageAttributes(TypedDict):
    ApproximateReceiveCount: str
    SentTimestamp: str
    SenderId: str
    ApproximateFirstReceiveTimestamp: str

class SQSMessage(TypedDict):
    messageId: str
    receiptHandle: str
    body: str
    attributes: SQSMessageAttributes
    messageAttributes: Dict[str, Any]
    md5OfBody: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str

class SQSEvent(TypedDict):
    Records: List[SQSMessage]