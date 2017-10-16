//POST
var request = require('request');
var fs = require('fs');
var FormData = require('form-data');

// 헤더 부분
var headers = {
    'User-Agent':   'Super Agent/0.0.1',
    'enctype-type': 'multipart/form-data'
};

// 요청 세부 내용
var options = {
    url: 'https://mindsapi.mindslab.ai/api/stt/',
    method:'POST',
    encoding:'utf-8',
    headers: headers,
    formData:{
        'ID': 'minds-api-service-client-id',
        'key': 'minds-api-service-client-key',
        'lang': 'kor',
        'level': 'baseline',
        'sampling': 8000,
        'cmd': 'runFileStt',
        'file': [fs.createReadStream('../audio/hello-8k.wav')]
    }
};

// 요청 시작 받은값은 body
var req = request(options, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        console.log(unicodeToChar(body).replace(/\\n/g, ". "));
    }
});


function unicodeToChar(text) {
    return text.replace(/\\u[\dA-F]{4}/gi,
        function (match) {
            return String.fromCharCode(parseInt(match.replace(/\\u/g, ''), 16));
        });
}
