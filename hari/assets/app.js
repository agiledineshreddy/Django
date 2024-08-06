const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
const bcrypt = require('bcrypt');

const app = express();
const port = 3000;
const mongoUrl = 'mongodb://admin:password123@localhost:27017/hari_mongo';

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// Serve signup.html directly
app.get('/signup.html', (req, res) => {
    res.sendFile(__dirname + '/public/signup.html');
});

// Serve signin.html directly
app.get('/signin.html', (req, res) => {
    res.sendFile(__dirname + '/public/signin.html');
});

// Serve welcome.html directly
app.get('/welcome.html', (req, res) => {
    res.sendFile(__dirname + '/public/welcome.html');
});

// Sign-up route
app.post('/signup', (req, res) => {
    // Sign-up logic
});

// Sign-in route
app.post('/signin', (req, res) => {
    // Sign-in logic
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
