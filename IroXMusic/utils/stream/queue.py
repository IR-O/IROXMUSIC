Here are the detailed code comments for the provided code:

- `get_chat_queue(chat_id)`:
This asynchronous function retrieves the queue for a given `chat_id` from the database.

- `add_to_queue(chat_id, original_chat_id, file, title, duration, user, vidid, user_id, stream, forceplay=None)`:
This asynchronous function adds a song to the queue after processing the input data. It converts the duration to seconds, handles invalid durations, and inserts the song into the queue based on the `forceplay` parameter.

- `add_to_queue_index(chat_id, original_chat_id, file, title, duration, user, vidid, stream, forceplay=None)`:
This asynchronous function adds a song to the queue with index checking after processing the input data. If the `vidid` contains a specific IP address, it gets the duration using the `check_duration` function and converts it to a human-readable format. If there's an error, it sets the duration to 'URL stream'.
