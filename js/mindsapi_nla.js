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
    url: 'https://api.maum.ai/api/nla/',
    method:'POST',
    encoding:'utf-8',
    headers: headers,
    formData:{
        'ID': 'client-id',
        'key': 'client-key',
        'level': 0,
        'keyword_level': 0,
        'sampling': 8000,
        'cmd': 'runNLA',
        'sentence': '마인즈 API 서비스 테스트 입니다'
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
