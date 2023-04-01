const google = require("google-it")
const translate = require('translate-google')
const {PythonShell} = require('python-shell')
const scrape = require('scrape-it');
const { JSDOM } = require("jsdom");

async function simpleAI(text, callback){
    if(text){
        text = await translate(text, {to: "en"})
        var search = (await google({"no-display": true, query: text}))
        var bodys = ""
        try {
            for (var g of search) {
                let link = g.link
                let body = (await scrape(link)).body
                
                if(!bodys.length) bodys = body
                else{
                    let doc1 = bodys.split(/<body>|<\/body>/g)[1]
                    var { document: doc0 } = (new JSDOM(bodys)).window

                    body = doc0.createElement('div')
                    body.innerHTML = doc1
                    doc0.body.appendChild(body)

                    bodys = doc0.querySelector('*').innerHTML
                }
            }

            let shell = new PythonShell('parse.py', {mode: 'text'})
            shell.send(encodeURIComponent(bodys))
            shell.send(text)
            shell.on('message', function (message) {
                callback(message)
                return shell.end()
            });
        } catch (e) {
            throw e
        }
        
    }
}

module.exports = simpleAI
