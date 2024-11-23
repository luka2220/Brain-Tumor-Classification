
class MessageQueue:
    def __init__(self, max_size=10):
        """Initialize the message queue with a maximum size."""
        self.queue = []
        self.max_size = max_size

    def enqueue(self, message):
        """Add a message to the queue."""
        if len(self.queue) < self.max_size:
            self.queue.append(message)
            return True
        else:
            print("Queue is full. Cannot enqueue message.")
            return False

    def dequeue(self):
        """Remove and return the oldest message from the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None

    def peek(self):
        """View the oldest message without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Get the current number of messages in the queue."""
        return len(self.queue)

    def clear(self):
        """Clear all messages from the queue."""
        self.queue = []
Footer
