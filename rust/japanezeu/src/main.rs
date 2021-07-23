fn main() {
    let path = "./bob.sqlite";
    std::fs::remove_file(&path);
    let connection = sqlite::open(&path).unwrap();
    connection
        .execute(
            "
        CREATE TABLE items (id INTEGER, side_a TEXT, side_b TEXT);
        INSERT INTO items (id, side_a, side_b) VALUES (0, 'former host of jeopardy', 'who is alex trabek');
        INSERT INTO items (id, side_a, side_b) VALUES (1, 'Playing with the queen of hearts', 'Knowing it is not really smart');
        ",
        )
        .unwrap();

    connection
        .execute(
            "
        CREATE TABLE events (time INTEGER, item_id INTEGER, correct_response BOOL);
        INSERT INTO events (time, item_id, correct_response) VALUES (0, 0, false);
        ",
        )
        .unwrap();

    connection
        .iterate("SELECT * FROM items WHERE id > -1", |pairs| {
            for &(column, value) in pairs.iter() {
                println!("{} = {}", column, value.unwrap());
            }
            true
        })
        .unwrap();

    connection
        .iterate("SELECT * FROM events WHERE time >= 0", |pairs| {
            for &(column, value) in pairs.iter() {
                println!("{} = {}", column, value.unwrap());
            }
            true
        })
        .unwrap();

    let mut cursor = connection
        .prepare("SELECT * FROM events WHERE time >= ?")
        .unwrap()
        .into_cursor();
    cursor.bind(&[sqlite::Value::Integer(0)]).unwrap();
    while let Ok(Some(row)) = cursor.next() {
        println!("name = {}", row[0].as_string().unwrap());
        println!("age = {}", row[1].as_integer().unwrap());
    }
}
