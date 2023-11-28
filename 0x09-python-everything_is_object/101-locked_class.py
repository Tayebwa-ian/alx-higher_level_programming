#!/usr/bin/python3
"""
    Locked Class Mdule
    """


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes,
    except if the
    new instance attribute is called first_name.
    """
    def __setattr__(self, name, value):
        """ Allow creation of 'first_name' attribute
        By overriding the __setattr__method

        Raises:
          AtttributeError: if the instance does not have first_name attribute
        """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(
                "[AttributeError] 'LockedClass' object has no attribute '{}'"
                .format(name))
