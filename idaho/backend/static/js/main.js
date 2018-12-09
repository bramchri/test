const siteKey = '6LflR2kUAAAAAJsy97ypHgWdFQ-wROMNIMaCDMvU'
const anticaptchURL = 'https://api.anti-captcha.com/createTask'
const captchaApiKey = 'f20e35cc7c16a8479141799c2dec9c82'
var taskID = 0

$(document).ready(function() {

    getWordsDictionary();
});

function getWordsDictionary() {
    $.ajax({
        url: '/api/v1/dictionary/',
        dataType: 'json',
        success: function(data) {
            startUtahScraper(data);
        }
    });
}

function startUtahScraper(wordsDictionary) {
    $('#run-utah-scraper').on('click', function () {

        console.log('Start UtahScraper');
        $('#content').on("DOMSubtreeModified", function (event) {
            console.log('event happend', event)
        });

        var urlUtahScraper = 'https://mycash.utah.gov/app/claim-search?lastName=';

        var count = 0,
            stopLoad = 2;

        for(var key in wordsDictionary) {
            count++;
            if (count == stopLoad) {
                return;
            }


            var url = urlUtahScraper + key,
                iframe = '<iframe src="' + url + '" style="width:100%;height:400px;"></iframe>';
            // contentHtml = $('#content').html();
            $('#content').html(iframe);

        }

        setTimeout(function () {

        }, 5000)

    });
}


function antiCaptcha(url){
    $.ajax({
        url:anticaptchURL,
        dataType: 'json',
        data:{
            "clientKey":captchaApiKey,
            "task":
                {
                    "type":"NoCaptchaTask",
                    "websiteURL":url,
                    "websiteKey":siteKey,
                    "proxyType":"http",
                    "proxyAddress":"118.172.201.131",
                    "proxyPort":58215,
                    "userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
                }
        },
        success: function result(response) {
            var elem = $('#g-recaptcha-response')
            console.log(elem, response)

        }
    })
}