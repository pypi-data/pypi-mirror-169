class option_key_values:
    """triple element mapping of {option:key} and {key:value}, the value should be bool"""

    def __init__(self, option_key={}, keys={}) -> None:
        # assert()
        self.oks = option_key
        self.kos = {v: k for k, v in self.oks.items()}
        self.set_by_keys(keys)
        # self.kvs = {key: True if key in options else False for option, key in self.oks.items()}
        pass

    def value_by_key(self, key):
        return self.kvs[key]

    def value_by_option(self, option):
        return self.kvs[self.oks[option]]

    def set_by_keys(self, keys):
        self.kvs = {key: True if key in keys else False for option, key in self.oks.items()}
        # print(self.kvs)
        return self

    def set_by_option(self, option, value):
        key = self.oks[option]
        self.kvs[key] = value
        # print(self.kvs)
        return self

    def toggle_by_key(self, key):
        if key in self.kvs.keys():
            self.kvs[key] = not self.kvs[key]
            return True
        return False

    def __str__(self) -> str:
        return ", ".join([":".join([option, key, self.kvs[key].__str__()]) for option, key in self.oks.items()])


if __name__ == "__main__":
    import logging

    # initialize Log
    logging.basicConfig(format="%(asctime)s - %(levelname)s[%(process)d,%(thread)d] - %(message)s", level=logging.DEBUG)

    okv = option_key_values(
        {
            "show_a": "a",
            "show_b": "b",
            "show_c": "c",
            "show_d": "d",
        },
        {
            "a",
            "c",
        },
    )
    logging.debug(f"{okv.__str__()=}")

    for k in okv.kvs:
        logging.debug(f"{k=},{okv.value_by_key(k)=}")

    for o in okv.oks:
        logging.debug(f"{o=},{okv.value_by_option(o)=}")

    for k in (
        ("a"),
        ("b", "c"),
        ("d", "c"),
        ("d", "c", "c", "b"),
    ):
        logging.debug(f"{k=},{okv.set_by_keys(k).__str__()=}")

    for o in okv.oks:
        logging.debug(f"{o=},{okv.set_by_option(o,True).__str__()=}")

    # for k in okv.kvs:
    for k in ["a",'e']:
        logging.debug(f"{k=},{okv.toggle_by_key(k)=},{okv.__str__()=}")
