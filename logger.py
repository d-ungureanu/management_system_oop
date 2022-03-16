from datetime import datetime

now = datetime.now()
datetime_string = now.strftime("%d%m%y_%H%M%S")
log_file_name = f"log_{datetime_string}.log"


def create_log_file():
    global now
    global datetime_string
    global log_file_name
    with open(log_file_name, "w") as log_file:
        log_file.write(f"{now} - {log_file_name} file created.\n")


def update_log_file(log_line):
    global log_file_name
    global now
    now = datetime.now()
    with open(log_file_name, "a") as log_file:
        log_file.write(f"{now} - {log_line}\n")
