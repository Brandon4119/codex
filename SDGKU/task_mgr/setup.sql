CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    summary,
    description
) VALUES
    (
        "Walk the dog",
        "Take the dog to the park for a walk"
    ),
    (
        "Do the dishes",
        "Wash the dishes after dinner"
    ),
    (
        "Wash he car",
        "Take the car to the car wash and wash it"
    );