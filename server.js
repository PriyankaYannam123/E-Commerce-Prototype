const express = require("express");
const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

let users = [{ username: "testUser", password: "password" }];

app.post("/api/login", (req, res) => {
    const { username } = req.body;
    const user = users.find((u) => u.username === username);
    if (user) res.json({ user: username });
    else res.status(401).json({ error: "User not found" });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
