# Simple-AI

This AI is still in the development stage, don't expect more from this module. AI intents come from google scrape

## Table of Contents

- [Simple-AI](#Simple-AI)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [For Node.js](#for-nodejs)

## Usage

#### For Node.js

Install using:

```shell
npm install simple-ai --save
```

### WARNING

this module require python library
Install pyhton require: 
```shell
pip install bs4 sklearn nltk numpy requests
```

Get the response:

```javascript
var simpleAI = require("simple-ai");

simpleAI("kapan indonsia merdeka", function(response){
  console.log(response)
})
// -> question translate to english even so a response
On 7 September 1944, Japanese Prime Minister Kuniaki Koiso promised independence for the 'East Indies' "later on" (di kemudian hari). The authorities in Java then allowed the flying of the Indonesian flag at Jawa Hokokai buildings. Rear-admiral Maeda provided official funds for tours around the archipelago by Sukarno and Hatta, and in October 1944, established a Free Indonesia Dormitory to prepare youth leaders for an independent Indonesia. With the war situation becoming increasingly dire, in March 1945 the Japanese announced the formation of an Investigating Committee for Preparatory Work for Independence (BPUPK), comprising members of the older political generation, including Sukarno and Hatta. Chaired by Rajiman Wediodiningrat, in two sessions in May and June, it decided on the basis for an independent nation and produced a draft constitution. Meanwhile, the younger activists, known as the pemuda, wanted much more overt moves towards independence than the older generation were willing to risk, resulting in a split between the generations.
```