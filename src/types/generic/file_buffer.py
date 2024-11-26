# Your task is to create a new file type with a “Buffer”.
# Every time you write data to this file, you use the Write method like write(“hello world”), but if you have enough buffer in memory (buffer_size), you write to buffer first. Only write to disk when the buffer is full (using the flush method to write to disk).
# Implement both the Write and flush functions



# chatgpt version
class BufferedFileWriter:
    def __init__(self, file_path: str, buffer_size: int):
        self.file_path = file_path
        self.buffer_size = buffer_size
        self.buffer = ""  # String buffer
        self.current_size = 0  # Keep track of the buffer size
        self.file = open(self.file_path, "a")  # Open the file in append mode

    def write(self, data: str) -> None:
        """Write data to the buffer, and flush to disk if buffer is full."""
        self.buffer += data
        self.current_size += len(data)

        # If buffer exceeds buffer_size, flush it to disk
        if self.current_size >= self.buffer_size:
            self.flush()

    def flush(self) -> None:
        """Flush the buffer to the file and clear the buffer."""
        if self.current_size > 0:
            self.file.write(self.buffer)  # Write buffer to file
            self.file.flush()  # Ensure the data is written to disk
            self.buffer = ""  # Clear the buffer
            self.current_size = 0  # Reset the buffer size

    def close(self) -> None:
        """Flush any remaining data and close the file."""
        self.flush()  # Ensure the remaining data is written
        self.file.close()  # Close the file


# Example Usage
buffered_writer = BufferedFileWriter("output.txt", buffer_size=20)
buffered_writer.write("hello ")
buffered_writer.write("world ")
buffered_writer.write("this is a buffered file writer.")
buffered_writer.flush()  # Write remaining data to disk
buffered_writer.close()  # Close the file
