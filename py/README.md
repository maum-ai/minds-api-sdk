# Python SDK for Minds API

- Make sure you have mindsapi.py, mindsapi_env.py, and __ init __.py in the same folder.

- Use python 2.7 or python 3.5.

- Import the speech recognition class by Minds API service.
```python
import mindsapi
```

- Create an instance of file-based STT(Speech-To-Text) client class, SttFileClient.
```python
stt = mindsapi.SttFileClient()
```

- Set your ID.
```python
    stt.putID('your Minds API ID')
    print("\n # ID  : " + stt.getID())
```

- Set your key.
```python
    stt.putKey('your Minds API key')
    print("\n # Key : " +  stt.getKey())
```

- Get all the available STT models supported.
```python
    status, data = stt.CheckAvailableSttModels(_print=False)
    print("\n # Response : {}".format(status))
    if status == 'Success':
        print(" > The number of available STT models : {:d}".format(len(data['sttModels'])))
        print(json.dumps(data, indent=4, sort_keys=True))
    else:
        print(" > " + data)
        return
```
- Use the file-based STT service with audio file whose format is "wav" or "mp3".
```python
    stt.putSttModel(lang='kor', level='baseline', sampling='8000')
    sttModel = stt.getSttModel()
    print("\n # STT Model: {}-{}-{}".format(sttModel[1], sttModel[0], sttModel[2]))
    status, data = stt.RunFileStt(filename, _print=False)
    print("\n # RunFileStt - " + status + " : " + data)
```

* Test audio files are provided in [here](https://github.com/mindslab-ai/Minds_API_SDK/tree/master/audio).
