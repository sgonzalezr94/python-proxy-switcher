from typing import List, Union


class ProxySwitcher(object):
    def __init__(self, proxies: List[str], ports: Union[List, None] = None):
        """
        Initialize the object with a list of string of proxies and ports if provided.If ports are not defined,
        the http request will always try to use the conventional 8080 port.
        :param proxies: list of proxies
        :param ports: optional list of ports
        """
        if not proxies:
            print(
                "Provided proxy list is empty, try populating it before instanciating the object."
            )
            return

        if ports is not None:
            assert len(proxies) == len(ports)
            self.ports = ports
        else:
            self.ports = [8080] * len(proxies)

        self.proxies = proxies
        self.n_proxy = len(self.proxies)
        self.current = 0
