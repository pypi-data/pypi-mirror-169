from dataclasses import dataclass

@dataclass
class Config:
    queue_name: str
    rpc_queue_name: str
    rpc_exchange_name: str