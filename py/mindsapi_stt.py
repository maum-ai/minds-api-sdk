#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import requests
import json
import os
import time
import sys
import argparse
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
MINDS_API_KEY = 'minds-api-service-client-key'


class SttFileClient(object):
    """Class for file-based STT client
    """

    def __init__(self, ID=None, key=None, lang=None, level=None, sampling=None):
        self.version = STT_VERSION
        self.ID = ID
        self.key = key
        self.lang = lang
        self.level = level
        self.sampling = sampling
        self.sttUrl = API_FRONT_URL + "stt/"
        self.detailSttUrl = API_FRONT_URL + "detail_stt/"

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

    def putSttModel(self, lang=None, level=None, sampling=None):
        self.lang = lang
        self.level = level
        self.sampling = sampling

    def getSttModel(self):
        return self.lang, self.level, self.sampling

    def CheckAvailableSttModels(self, _print=True):
        """Check available STT models from Minds API service.
        :param _print:
        :return:
        """
        data = {'cmd': 'getSttModels', 'ID': self.ID, 'key': self.key}
        files = {}
        r = requests.post(self.sttUrl, files=files, data=data)
        # r = requests.post(self.detailSttUrl, files=files, data=data)

        if r.status_code == 200:
            r_dict = json.loads(r.text)
            status = r_dict['status']
            if status == 'Success':
                data = json.loads(r_dict['data'])
            else:
                data = r_dict['data']
            if _print:
                print(json.dumps(data, indent=4, sort_keys=True))
            return status, data
        else:
            return 'Fail', 'Error code : ' + str(r.status_code)

    def RunFileStt(self, audioFilename, _print=True):
        """Request file-based STT to Minds API service.
        :param audioFilename:
        :param _print:
        :return:
        """
        if not os.path.isfile(audioFilename):
            return 'Fail', 'File not found'

        data = {'cmd': 'runFileStt', 'lang': self.lang, 'sampling': self.sampling, 'level': self.level, 'ID': self.ID,
                'key': self.key}
        files = {'file': open(audioFilename, 'rb')}
        r = requests.post(self.sttUrl, data=data, files=files)
        if r.status_code == 200:
            r_dict = json.loads(r.text)
            print(r.text)
            if _print:
                print(r_dict['status'] + ' : ' + r_dict['data'])
            return r_dict['status'], r_dict['data']
        else:
            return 'Fail', str(r.status_code)


def self_test(args):
    """Self test code
    :return:
    """
    start_time = time.time()

    stt = SttFileClient()

    stt.putID(MINDS_API_ID)
    print(" # ID  : " + stt.getID())
    stt.putKey(MINDS_API_KEY)
    print(" # Key : " + stt.getKey())

#    status, data = stt.CheckAvailableSttModels(_print=False)
#    print("\n # Response : {}".format(status))
#    if status == 'Success':
#        print(" > The number of available STT models : {:d}".format(len(data['sttModels'])))
#        print(json.dumps(data, indent=4, sort_keys=True))
#    else:
#        print(" > " + data)
#        return

    attrModel = args.model.split('-')
    stt.putSttModel(lang=attrModel[1], level=attrModel[0], sampling=attrModel[2])
    sttModel = stt.getSttModel()
    print("\n # STT Model: {}-{}-{}".format(sttModel[1], sttModel[0], sttModel[2]))

    status, data = stt.RunFileStt(args.file, _print=False)
    print('status : ', status)
    # print("\n # RunFileStt - " + status + " : " + data)
    print("--- %s sec ---" % (time.time() - start_time))


def parse_arguments(argv):
    """
    Parse arguments.

    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Audio Filename")
    parser.add_argument("--model", required=True, help="STT Model Name")
    return parser.parse_args(argv)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.extend(['--file', '../audio/weather-8k.pcm'])
        sys.argv.extend(['--model', 'baseline-kor-8000'])
        # self_test('../audio/201711723923_Addr.wav', 'address-kor-8000')
        # self_test('../audio/mp3-samples/test.mp3', 'baseline-kor-16000')
        # self_test('../audio/test_stt.mp3', 'mindsedu_t-eng-8000')
        # self_test('../audio/eng_8K/101_001.wav', 'mindsedu_t-eng-8000')
        # self_test('../audio/20181012_080942_From9450_To01031599308_s.wav', 'mindsedu_s-eng-8000')
        # self_test('../audio/mp3-samples/aekukka.mp3', 'baseline-kor-16000')
        # self_test('../audio/eng_16K/101_001.wav', 'readntalk-eng-16000')
        # self_test('../audio/hello-16k.wav', 'baseline-kor-16000')
        # self_test('../audio/헬로-16k.wav', 'baseline-eng-16000')

    self_test(parse_arguments(sys.argv[1:]))
