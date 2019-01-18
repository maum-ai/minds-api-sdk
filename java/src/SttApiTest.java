import java.io.BufferedReader;
import java.io.File;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.apache.commons.httpclient.HttpStatus;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;


public class SttApiTest {
	public static String unicodeConvert(String str) {
        StringBuilder sb = new StringBuilder();
        char ch;
        int len = str.length();
        for (int i = 0; i < len; i++) {
            ch = str.charAt(i);
            if (ch == '\\' && str.charAt(i+1) == 'u') {
                sb.append((char) Integer.parseInt(str.substring(i+2, i+6), 16));
                i+=5;
                continue;
            }
            sb.append(ch);
        }

        return sb.toString();
    }
	
	public static void main(String[] args) {
        CloseableHttpClient httpClient = HttpClientBuilder.create().build(); //Use this instead 

        try {
            String url = "https://api.maum.ai/api/" + "stt/";
            
            String path = SttApiTest.class.getResource("").getPath();//current file's absolute path
            String filePath = path + "hello-16k.wav";
            File file = new File(filePath);
            FileBody fb = new FileBody(file);
            
            HttpEntity entity = MultipartEntityBuilder
                .create()
                .addTextBody("ID", "client-id")
                .addTextBody("key", "client-key")
                .addTextBody("cmd", "runFileStt")
                .addTextBody("lang", "kor")
                .addTextBody("sampling", "16000")
                .addTextBody("level", "baseline")
                .addPart("file", fb)
                .build();
        
            HttpPost request = new HttpPost(url);
            request.setEntity(entity);
            HttpResponse response = httpClient.execute(request);
        
            //handle response here...
            HttpEntity result = response.getEntity();

            InputStream inputStream = result.getContent();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
            if(response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
            	throw new Exception(response.getStatusLine().getReasonPhrase());
            }
            StringBuilder builder = new StringBuilder();
            String s;
            while(true) {
            	s = reader.readLine();
            	if(s == null || s.length() == 0)
            		break;
            	builder.append(s);
            }
            reader.close();
            inputStream.close();
            System.out.println(builder.toString());
            
            String resultString = builder.toString();
            System.out.println(unicodeConvert(resultString));
        }catch (Exception ex) {
        
            //handle exception here
        	System.out.println(ex.toString());
        
        } finally {
        	System.out.println("=== end ===");
        }
    }
}
