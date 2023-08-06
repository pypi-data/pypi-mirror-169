from dataclasses import dataclass

from tvmbase.exceptions import UnknownNetworkException
from tvmbase.utils.singleton import SingletonMeta


@dataclass(frozen=True, slots=True)
class Network:
    endpoints: list[str]
    everlive_domain: str
    everscan_domain: str


class NetworkFactory(metaclass=SingletonMeta):

    def __init__(self, evercloud_key: str):
        self.evercloud_key = evercloud_key
        self.custom_networks: dict[str, Network] = dict()

    def mainnet(self) -> Network:
        return Network(
            [f'https://mainnet.evercloud.dev/{self.evercloud_key}/graphql'],
            'ever.live',
            'everscan.io',
        )

    def devnet(self) -> Network:
        return Network(
            [f'https://devnet.evercloud.dev/{self.evercloud_key}/graphql'],
            'ever.live',
            'everscan.io',
        )

    def from_name(self, name: str) -> Network:
        name = name.lower()
        match name:
            case 'main' | 'mainnet':
                return self.mainnet()
            case 'dev' | 'devnet':
                return self.devnet()
        if name in self.custom_networks:
            return self.custom_networks.get(name)
        raise UnknownNetworkException(name)

    def add_custom(self, name: str, network: Network):
        self.custom_networks[name] = network

    def get_all(self) -> list[Network]:
        return [self.mainnet(), self.devnet()] + list(self.custom_networks.values())
