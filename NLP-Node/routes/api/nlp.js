// ROUTER INITIALIZATION
const router = require("express").Router();
const axios = require("axios");

// English NLP API
router.post('/en', async (request, response) => {
    if (!request.body.messages) {
        return response.status(400).json({ errorMessage: "Bad Request, 400" });
    }
    var englishNLPData = { "messages" : request.body.messages }
    await axios({
        method: 'post',
        url: 'http://localhost:30080/nlp/en',
        data: englishNLPData,
        })
        .then((res) => {
            //handle success
            return response.status(200).json(res.data);
        })
        .catch((err) => {
            //handle error
            return response.status(500).json({ errorMessage: "Internal Server Error, 500" });
        });
})

// Korean NLP API
router.post('/ko', async (request, response) => {
    if (!request.body.messages) {
        return response.status(400).json({ errorMessage: "Bad Request, 400" });
    }
    var koreanNLPData = { "messages" : request.body.messages }
    await axios({
        method: 'post',
        url: 'http://localhost:30080/nlp/ko',
        data: koreanNLPData,
        })
        .then((res) => {
            //handle success
            return response.status(200).json(res.data);
        })
        .catch((err) => {
            //handle error
            return response.status(500).json({ errorMessage: "Internal Server Error, 500" });
        });
})

module.exports = router;