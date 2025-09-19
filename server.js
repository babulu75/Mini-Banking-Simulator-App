const express = require("express");
const mysql = require("mysql2");

const app = express();

// Middleware to parse JSON body
app.use(express.json());

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "Vinni@02#feb",
    database: "bank"
});

db.connect((err) => {
    if (err) {
        console.error("Database connection failed:", err.stack);
        return;
    }
    console.log("✅ Connected to MySQL");
});

app.get("/", (req, res) => {
    res.send("hello world");
});

app.post("/getuser", (req, res) => {
    const { username } = req.body;
    console.log("Received request for user:", username);

    db.query("SELECT * FROM USERS WHERE name = ?", [username], (err, results) => {
        if (err) {
            return res.status(500).json({ error: err });
        }
        if (results.length > 0) {
            res.json(results[0]); // send only the first matched user
        } else {
            res.status(404).json({ message: "User not found" });
        }
    });
});

app.put("/withdraw", (req, res) => {
    const { username, amount } = req.body;
    console.log(`${username} requested withdraw. New balance: ${amount}`);
    db.query("UPDATE USERS SET AMOUNT=? WHERE NAME=?", [amount, username], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err });
        }
        if (result.affectedRows > 0) {
            res.json({ message: "Withdraw successful", balance: amount });
        }
        else {
            res.status(400).json({ message: "User not found" });
        }
    });
});

app.put("/deposit", (req, res) => {
    const { username, amount } = req.body;
    console.log(`${username} requested Deposit. New balance: ${amount}`);
    db.query("UPDATE USERS SET AMOUNT=? WHERE NAME=?", [amount, username], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err });
        }
        if (result.affectedRows > 0) {
            res.json({ message: "Withdraw successful", balance: amount });
        }
        else {
            res.status(400).json({ message: "User not found" });
        }
    });
});

app.listen(3000, () => {
    console.log("🚀 Server running on http://localhost:3000");
});
