const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(bodyParser.json());

const mockUser = {
  username: "admin",
  password: "1234"
};

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === mockUser.username && password === mockUser.password) {
    res.json({ message: "Login successful!" });
  } else {
    res.json({ message: "Invalid username or password." });
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});