File System -> Persistence
x = 42 -> DB, File System -> File
              OS
 I. Binary I/O -> Byte Stream
II. Text I/O   -> Character Stream

x : int = 1000000
Text I/O -> 4 | 2 -> HRF: CSV, XML, JSON
            3 | 6 | 1 | 5
            1 | 0 | 0 | 0 | 0 | 0 | 0
Binary I/O -> 4-byte
            BSON

numbers = [4,8,15,16,23,42]
4|8|1|5|1|6|2|3|4|2 -> read -> ?
4|8|,|1|5|,|1|6|,|2|3|,|4|2 -> read -> [4,8,15,16,23,42]
4B|4B|4B|....|4B

protocol buffers
protoc --python_out=. employee.proto