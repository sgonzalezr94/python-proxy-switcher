from typing import List, Union
import numpy as np
import os


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
            self.ports = [8080] * len(
                proxies
            )  # We asign this common port to every single proxy we use.

        self.proxies = proxies
        self.n_proxy = len(self.proxies)
        self.current = 0

    def __str__(self):
        return "Proxies: " + str(self.proxies)

    def set_proxy(self, mode: str = "rr", verbose: bool = True):
        """
        Set proxies based on the proxy list for HTTP and HTTPS requests.
        :param mode: 'rr' and 'rand', If 'rr' selects iteratively each proxy, commonly called RoundRobin.
                      if 'rand' choses a random proxy from the list.
        :param verbose: Proxy verbosity for each existing combination of proxy+port.
        """
        if mode == "rr":
            proxy = self.proxies[self.current]
            port = self.ports[self.current]

            self.current += 1
            if self.current % self.n_proxy == 0:
                self.current = 0
        else:
            idx = np.random.randint(self.n_proxy)
            proxy = self.proxies[idx]
            port = self.ports[idx]

        os.environ["HTTP_PROXY"] = "http://" + str(proxy) + ":" + str(port)
        os.environ["HTTPS_PROXY"] = "https://" + str(proxy) + ":" + str(port)

        if verbose:
            print("Set proxy " + str(proxy) + " at port " + str(port))

    def reset(self):
        """
        Unset Proxie HTTP and HTTPS variables.
        """
        del os.environ["HTTP_PROXY"]
        del os.environ["HTTPS_PROXY"]
