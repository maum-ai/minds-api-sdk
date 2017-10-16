#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
import requests
import json

from mindsapi_env import *

__author__ = "Hoon Paek, Hyungjoo Lee"
__copyright__ = "Copyright 2017, The MindsAPI Project"
__credits__ = []
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Hoon Paek, Hyungjoo Lee"
__email__ = "mindsapi@mindslab.ai"
__status__ = "Development"      # Prototype / Development / Production

STT_VERSION = "0.1.0"
MINDS_API_ID  = 'minds-api-service-client-id'
MINDS_API_KEY = 'minds-api-service-client-key'


class NlaClient(object):
    """ Class for Natural Language Analysis
    """

    def __init__(self, ID=None, key=None, level=None, keyword_level=None):
        self.version = STT_VERSION
        self.ID = ID
        self.key = key
        self.level = level
        self.keyword_level = keyword_level
        self.sttUrl = API_FRONT_URL + "nla/"

    def __version__(self):
        return self.version

    def putID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def putKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def putNlaModel(self, level=0, keyword_level=0):
        self.level = level
        self.keyword_level = keyword_level

    def getNlaModel(self):
        return self.level, self.keyword_level

    def RunNla(self, sentence, _print=True):
        """Request NLA (Natural Language Analysis) with input sentence.
        :param sentence:
        :param _print:
        :return:
        """
        data = {'cmd': 'runNLA', 'ID': self.ID, 'key': self.key,
                'level': self.level, 'keyword_level': self.keyword_level,
                'sentence': sentence}
        r = requests.post(self.sttUrl, data=data, files=None)
        if r.status_code == 200:
            r_dict = json.loads(r.text)
            if _print:
                print(r_dict['status'] + ' : ' + r_dict['data'])
            return r_dict['status'], r_dict['data']
        else:
            return 'Fail', str(r.status_code)


def self_test(sentence, level=0, keyword_level=0):
    """Self test code
    :return:
    """

    nla = NlaClient()

    nla.putID(MINDS_API_ID)
    print(" # ID  : " + nla.getID())
    nla.putKey(MINDS_API_KEY)
    print(" # Key : " +  nla.getKey())

    nla.putNlaModel(level=level, keyword_level=keyword_level)
    nlaModel = nla.getNlaModel()
    print("\n # NLA Model: {}, {}".format(nlaModel[0], nlaModel[1]))
    status, data = nla.RunNla(sentence, _print=False)

    print("\n # RunNla - " + status + " : " + data)
    pass


if __name__ == "__main__":
    self_test('마인즈 API 서비스 테스트 입니다', level=0, keyword_level=0)
