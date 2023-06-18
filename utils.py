from enum import EnumMeta


class ContainsEnumMeta(EnumMeta):
    def name_of(cls, item, prefix=''):
        return cls(item).name if cls.__contains__(item) else f'{prefix}0x{item:02X}'

    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True
