from __future__ import absolute_import
from celery import chain
from proj.tasks import split, run


def main():
    chain(split.s() | run.s())()

if __name__ == '__main__':
    main()