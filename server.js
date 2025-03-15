const express = require("express");
const cors = require("cors");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get("/", (req, res) => {
  res.send("Hello, Railway App! Your backend is running 🚀");
});

// Sample API route
app.get("/api/data", (req, res) => {
  res.json({ message: "Welcome to your backend API!", status: "Success" });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});