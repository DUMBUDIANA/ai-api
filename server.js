// app.js
const express = require('express');
const cors = require('cors');
const messageHandler = require('./messageHandler');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json()); 
app.use(bodyParser.json()); 

// Define routes
app.get('/', (req, res) => {
  res.send('API is running');
});

// Use the messaging API
app.use('/api/messages', messageHandler); 

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
