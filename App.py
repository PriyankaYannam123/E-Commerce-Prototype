import React, { useState } from "react";

function App() {
    const [user, setUser] = useState(null);

    const login = async (username) => {
        const response = await fetch("/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username }),
        });
        const data = await response.json();
        setUser(data.user);
    };

    return (
        <div>
            <h1>E-Commerce Platform</h1>
            {!user ? (
                <button onClick={() => login("testUser")}>Login</button>
            ) : (
                <div>Welcome, {user}</div>
            )}
        </div>
    );
}

export default App;
