db = db.getSiblingDB("fastapi-mongo");

db.createCollection("my-books");

db.createUser({
    user: "admin",
    pwd: "pass",
    roles: [{ role: "root", db: "admin" }]
});

db.grantRolesToUser("admin", [{ role: "readWrite", db: "fastapi-mongo" }]);