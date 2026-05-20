from app.database.initializeDb import get_connection

def create_message(data):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO messages (
        session_name,
        recipient,
        message,
        send_at
    )
    VALUES (?, ?, ?, ?)
    """, (
        data["session_name"],
        data["recipient"],
        data["message"],
        data["send_at"]
    ))
    
    conn.commit()
    
    message_id = cursor.lastrowid
    conn.close()
    return {
        "id": message_id,
        "status": "created"
    }
    
    