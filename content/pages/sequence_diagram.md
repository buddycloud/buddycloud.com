Title: Sequence Diagrams Test
url: seq_diag
save_as: sequence_diagram.html

Title: Sequence Diagram Title
A->B: Message
Note right of B: B thinking
B-->A: Message back
A->B: Another message
A->C: Yet another messsage
C->>B: Message with\ndifferent arrow
C-->>A: Other type of message

participant A
participant B
Note over A: A note above A\nin a different Sequence diagram
