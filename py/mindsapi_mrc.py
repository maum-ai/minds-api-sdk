#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
import requests
import json

from mindsapi_env import API_FRONT_URL

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
MINDS_API_KEY = 'minds-api-service-client-key-expired'


class MrcClient(object):
    """ Class for Natural Language Analysis
    """

    def __init__(self, ID=None, key=None, ):
        self.version = STT_VERSION
        self.ID = ID
        self.key = key
        self.sttUrl = API_FRONT_URL + "mrc/"

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

    def RunMrc(self, question, sentence, _print=True):
        data = {
            'cmd': 'runMRC',
            'ID': self.ID,
            'key': self.key,
            'question': question,
            'sentence': sentence
        }
        r = requests.post(self.sttUrl, data=data, files=None)
        if r.status_code == 200:
            r_dict = json.loads(r.text)
            if _print:
                print(r_dict['status'] + ' : ' + r_dict['data'])
                # return only 1 data row
            return r_dict['status'], r_dict['data'][0]
        else:
            return 'Fail', str(r.status_code)


def self_test(question, sentence):
    """Self test code
    :return:
    """

    mrc = MrcClient()

    mrc.putID(MINDS_API_ID)
    print(" # ID  : " + mrc.getID())
    mrc.putKey(MINDS_API_KEY)
    print(" # Key : " +  mrc.getKey())

    status, data = mrc.RunMrc(question, sentence, _print=False)
    print("\n # RunMrc - " + status + " : " + str(data))


    pass


if __name__ == "__main__":
    self_test("데이브 존스의 직업은 뭐야?", '''주인공인 다니엘 블레이크를 연기한 데이브 존스는 코미디언이기도 하다. 그가 '나, 다니엘 블레이크를 인간으로서, 한 시민으로서 대우해 달라'고 천명하는 마지막 장면은 가슴 뭉클한 감동을 준다. 2등 상인 심사위원 대상을 받은 '단지 세상의 끝'도 12월 말로 개봉 시기를 조율 중이다. 엣나인필름 관계자는 "극장가 성수기 때 힘있게 가려고 연말 개봉을 목표로 하고 있다"며 "프랑스와 캐나다에서 먼저 개봉해야 하는 부분도 있다"고 말했다. '단지 세상의 끝'은 캐나다 출신 '칸의 총아' 자비에 돌란 감독이 2년 만에 내놓은 신작이다.''')
