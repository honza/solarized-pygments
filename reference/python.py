# Example code, do not run :)

import os
from datetime import datetime


counter = 123


def greet(name=None):
    if not name:
        print 'Who are you?'
    else:
        print 'Hello, %s' % name


class SuperObject(object):
    """
    Awesome super object
    """

    @property
    def name(self):
        return self.name

    def sort(self):
        try:
            self.sort()
        except KeyError:
            pass


if __name__ == '__main__':
    o = SuperObject()
