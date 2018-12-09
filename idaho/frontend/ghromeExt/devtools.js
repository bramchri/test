/*
 ENV
 */

const API = {
        saveData: 'save-data/', // Api for saving Data
        dictionary: 'dictionary/' // Api for getting dictionary
    },
        backendAPI = 'http://37.17.34.252:3001/api/v1/', // Backend URL
        clearUrl = 'https://yourmoney.idaho.gov', // Url of site
        urlUtahScraper = clearUrl + '/SWS/properties', // Url of responses with data
        urlCheckReq = clearUrl +'/SWS/app/properties', // Url of site for check data request
        urlUtahScraperSearch = clearUrl +'/app/claim-search?lastName=', // Url for scrapper
        taskType = "NoCaptchaTaskProxyless", // Captcha solver task
        capthcaApiKey = 'f20e35cc7c16a8479141799c2dec9c82', // Captcha solver API key
        websiteKey = "6LcDpFkUAAAAAKS5hSERgXsZFgfxtYi-bYEctKzk", // Captcha site-key
        captchaUrl = "https://api.anti-captcha.com/createTask", // Api for creating captcha solver task
        getResultUrl = "https://api.anti-captcha.com/getTaskResult", // Api for result check of captcha solving
        fromID = 0, // First ID of dict word from which bot should start
        toID = 9200; // Last ID of dict what bot should proceed

const bkg = chrome.extension.getBackgroundPage(); // Extension console

let totalRequests = 0, // Counter of total requests
    gRecaptchaResponse = "", // ReCaptcha solve
    taskId = 0, // Captcha solver task ID
    doesCapthaSend = false, // State of Captcha solution sending
    botStatus = false, // State of bot
    currentURL="", // Url of current site
    handlingError=false; // ?

let dictionaryId = 1; // Word id from dict from which start scrap

let timerId = setInterval(function () {
    if (!botStatus){
        gRecaptchaResponse = "";
        if (dictionaryId<fromID || dictionaryId>toID){ // Limits, if many bots in work
            bkg.console.log('STOP');
        }else{
            taskId=0;
        doesCapthaSend = false;
        botStatus = true;
        dictionaryId++;
        bkg.console.log('\nBot level:' + dictionaryId + '\n');
        getWordFromDictionary(dictionaryId);
        }


    }else{
        bkg.console.log('\nBot not ready!\n')
    }

}, 30*1000);


async function getWordFromDictionary(dictionaryId) {
    const url = backendAPI + API.dictionary + dictionaryId + '/';
    fetch(url)
        .then(function(response) {
            return response.json();
        }).then(function (data) {
        chrome.devtools.inspectedWindow.eval('console.log("'+'Search key: ' + data.name+'"))');
        chrome.devtools.inspectedWindow.eval('window.location.href = "' + urlUtahScraperSearch + data.name+'"');
    });
}


function setTotalRequests(number) {
    let message = 'Total responses: ' + number;
    chrome.devtools.inspectedWindow.eval('console.log(unescape("' + escape(message) + '"))');
}


chrome.devtools.network.onRequestFinished.addListener(
    async function(request) {

        if (request.request.url === urlUtahScraper) {

            if (request.response.status===200){
                bkg.console.log('Sending data to backend')
                request.getContent(async function(resp){
                    const k = await fetch(
                        backendAPI+API.saveData,
                        {
                            method: 'POST',
                            body:JSON.stringify({
                                resp:resp,
                                site:clearUrl
                            }),
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            mode: 'no-cors'
                        });
                    botStatus = false;
                });

            }
            if (request.response.status===204){
                bkg.console.log('Date is null')
                botStatus = false;
            }
            if (request.response.status===400){
                dictionaryId--;
                gRecaptchaResponse = "";
                taskId=0;
                doesCapthaSend = false;
                botStatus = false;

            }

            totalRequests++;
            setTotalRequests(totalRequests);
        }else{
            if(!doesCapthaSend && request.request.url != urlCheckReq){
                doesCapthaSend = true;
                chrome.devtools.inspectedWindow.eval('document.location.href',
                    async function callback(result, isExp) {
                        if(!isExp && botStatus){
                            bkg.console.log('Before send reCaptcha')
                            currentURL = result
                            const k = await sendCaptcha(result)
                            bkg.console.log('After send and get reCaptcha:', k)
                            if (k){
                                const f = await captchaHandler();

                            }else{
                                dictionaryId--;
                                gRecaptchaResponse = "";
                                taskId=0;
                                doesCapthaSend = false;
                                botStatus = false;
                            }

                        }
                        else{
                            doesCapthaSend = false
                        }
                    })
            }
        }
    });



async function sendCaptcha(url){
    let result;
    bkg.console.log('Url for captcha:', url)
    const l = await fetch(captchaUrl, {
        method: "POST",
        body:JSON.stringify({
            "clientKey":capthcaApiKey,
            "task":
                {
                    "type":taskType,
                    "websiteURL":url,
                    "websiteKey":websiteKey
                }
        })
    }).then(async function callback(resp) {
        const k = await resp.json().then(function callback(body){
            if (body.errorId===0){
                bkg.console.log('Get task responce:', body)
                taskId=body.taskId
                result = true;
                return true
            }else{

                if(body.errorId==2){
                    bkg.console.log('Workers busy')
                }else{
                    bkg.console.log('Error id:', body.errorId)
                    bkg.console.log('ErrorDesc:', body.errorDescription)
                }
                result = false;
                return false
            }
        });
        return k;
    })
    bkg.console.log('Captcha send status:', result)
    return result

}

async function captchaHandler() {
    bkg.console.log('CAPTCHA HANDLER GResp:',gRecaptchaResponse)
    if (gRecaptchaResponse){
        setCaptcha()
    }else{
        getStatus();
        const k = await setTimeout(
            function callback(){
                captchaHandler()
            },
            15*1000
        )
    }

}

function getStatus(){
    bkg.console.log(JSON.stringify({
        "Client Key":capthcaApiKey,
        "Task ID": taskId
    }))
    fetch(getResultUrl, {
        method: "POST",
        body: JSON.stringify({
            "clientKey":capthcaApiKey,
            "taskId": taskId
        })
    }).then(function callback(resp) {
        resp.json().then(function callback(body){
            if(body.status == 'ready'){
                bkg.console.log('Ready: ', body)
                gRecaptchaResponse = body.solution.gRecaptchaResponse
            }
            return body
        });

    })

    /* Example of response
     {
     "errorId": 0,
     "status": "ready",
     "solution": {
     "gRecaptchaResponse": "03ADlfD1-M1nEy0-dsAtW2bXR_J-y08cOsxwdCnvGjbH_fz6MchH--ehtbdmJa-x6g4kNoHgYbw2YH8DSc6AmiTWFRlohxdHddDDQ9gbWWsiiA3i5O1FTfkY1faSwkol1CUS8MEhHjuT6UFn1q4W9X5juQjI5u88bp3BHEmuuqRgMK6JlPWT2lJ0CSZC-Kc-H1a83o0GZ0PVxyxf6SYfEmfaEKYQVsRKBy9EjJDX15cFn9mR_SQNBZO0k1vIwfa-WgMkOcLuSDW9cQB0HTWeUt9wzAG6ITvbg8_A"
     },
     "cost": "0.002200",
     "ip": "37.17.34.252",
     "createTime": 1542102294,
     "endTime": 1542102333,
     "solveCount": 0
     }*/
}

function setCaptcha(){

    if(botStatus){
        chrome.devtools.inspectedWindow.eval('document.querySelector("#g-recaptcha-response").value="' + gRecaptchaResponse+'"',
            function callback(result, isExept) {
                if (!isExept){
                    chrome.devtools.inspectedWindow.eval(
                        'document.querySelector("#btn-recaptcha").click()',
                        function callback(res, isExept) {
                            setTimeout(function callback() {

                                chrome.devtools.inspectedWindow.eval('document.querySelector("error").innerText',
                                    async function callback(res,isExept){
                                        if (res==="Your reCAPTCHA token has expired. Please try your search again."){
                                            gRecaptchaResponse = ""
                                            chrome.devtools.inspectedWindow.eval('document.querySelector("#g-recaptcha-response").value=""')
                                            const k = await sendCaptcha(currentURL)
                                            bkg.console.log('Repeat reCaptcha', k)
                                            if (k){
                                                const f = await captchaHandler();

                                            }
                                        }
                                    }
                                )
                            }, 10000)

                        }
                    );
                }
            }
        );
    }
}

