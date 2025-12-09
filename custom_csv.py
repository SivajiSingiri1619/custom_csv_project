from typing import List, TextIO


class CustomCsvReader:
    """
    Custom CSV reader that supports:
    - Comma separated values
    - Fields in double quotes
    - Escaped double quotes ("")
    - Newlines inside quoted fields
    """

    def __init__(self, file_obj: TextIO) -> None:
        self.file = file_obj

    def __iter__(self):
        return self

    def __next__(self) -> List[str]:
        current_field: List[str] = []
        current_row: List[str] = []
        in_quotes = False

        while True:
            ch = self.file.read(1)

            # End of file
            if ch == "":
                if current_field or current_row:
                    current_row.append("".join(current_field))
                    return current_row
                raise StopIteration

            if not in_quotes:
                if ch == ",":
                    # end of field
                    current_row.append("".join(current_field))
                    current_field = []
                elif ch == "\n":
                    # end of row
                    current_row.append("".join(current_field))
                    return current_row
                elif ch == '"':
                    # start quoted field
                    in_quotes = True
                else:
                    current_field.append(ch)
            else:
                # inside quotes
                if ch == '"':
                    # peek next char
                    next_ch = self.file.read(1)
                    if next_ch == '"':
                        # escaped quote ("")
                        current_field.append('"')
                    else:
                        # end of quoted field
                        in_quotes = False
                        if next_ch == ",":
                            current_row.append("".join(current_field))
                            current_field = []
                        elif next_ch == "\n":
                            current_row.append("".join(current_field))
                            return current_row
                        elif next_ch == "":
                            current_row.append("".join(current_field))
                            return current_row
                        else:
                            # normal char directly after closing quote
                            current_field.append(next_ch)
                else:
                    # any char (even newline) inside quotes
                    current_field.append(ch)


class CustomCsvWriter:
    """
    Custom CSV writer that:
    - Writes comma separated values
    - Adds quotes if field has comma, quote, or newline
    - Escapes internal double quotes as ""
    """

    def __init__(self, file_obj: TextIO) -> None:
        self.file = file_obj

    def _format_field(self, field: str) -> str:
        """Format one field according to CSV rules."""
        if not isinstance(field, str):
            field = str(field)

        needs_quotes = ("," in field) or ('"' in field) or ("\n" in field)

        if needs_quotes:
            escaped = field.replace('"', '""')
            return f'"{escaped}"'
        else:
            return field

    def write_row(self, row: List[str]) -> None:
        """Write a single row to the file."""
        formatted_fields = [self._format_field(f) for f in row]
        line = ",".join(formatted_fields) + "\n"
        self.file.write(line)

    def write_rows(self, rows: List[List[str]]) -> None:
        """Write multiple rows."""
        for r in rows:
            self.write_row(r)
