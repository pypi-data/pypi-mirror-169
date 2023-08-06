# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     slsWriter
   Description :
   Author :       liaozhaoyan
   date：          2022/9/28
-------------------------------------------------
   Change Activity:
                   2022/9/28:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

from .Writer import Cwriter


class CslsWriter(Cwriter):
    def __init__(self, endpoint,
                 project, metricStore, auth):
        url = "https://%s.%s/prometheus/%s/%s/api/v1/write" % (project, endpoint, project, metricStore)
        super(CslsWriter, self).__init__(url, auth)


if __name__ == "__main__":
    pass
