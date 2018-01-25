# JAVA Client sample

- java 1.8
- apache http libraries

```
unicodeConvert
```
This method is for response string unicode convert.  
Just focus on http post request send and receive response.  





**SttApiTest.java**
```java
          File file = new File(filePath);
          FileBody fb = new FileBody(file);

          HttpEntity entity = MultipartEntityBuilder
              .create()
              .addTextBody("ID", "minds-api-service-client-id")
              .addTextBody("key", "minds-api-service-client-key-expired")
              .addTextBody("cmd", "runFileStt")
              .addTextBody("lang", "kor")
              .addTextBody("sampling", "16000")
              .addTextBody("level", "baseline")
              .addPart("file", fb)
              .build();

          HttpPost request = new HttpPost(url);
          request.setEntity(entity);
          HttpResponse response = httpClient.execute(request);
```
