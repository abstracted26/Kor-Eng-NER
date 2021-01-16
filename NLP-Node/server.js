const express = require("express");
const cors = require("cors");

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

// ROUTES
const nlpRouter = require("./routes/api/nlp");
app.use('/nlp', nlpRouter);

app.listen(port, () => {
    console.log("Server is running on port:" + port);
});