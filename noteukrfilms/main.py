import csv


class NoteFilm:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    @staticmethod
    def highest_rating_sorting(x):
        return x["rating"]

    @staticmethod
    def lowest_rating_sorting(x):
        return -x["rating"]

    def read_notes(self, sorting=None):
        """

        :param sorting: NoteFilm.highest_rating_sorting or NoteFilm.lowest_rating_sorting
        :return: List with dict data
        """
        with open(self.file_path) as csv_file:
            self.data = list(csv.DictReader(csv_file, delimiter=','))
        if sorting:
            self.data.sort(key=sorting)
        return self.data

    def add_note(self, film_name: str, note: str, rating: int):
        with open(self.file_path, mode='a') as csv_file:
            employee_writer = csv.writer(csv_file, delimiter=',')
            employee_writer.writerow([film_name, note, rating])
        return self

    def remove_note(self, num: int):
        if not self.data:
            self.read_notes()
        with open(self.file_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["film_name", "note", "rating"])
            counter = 0
            for row in self.data:
                counter += 1
                if counter != num:
                    writer.writerow(row.values())
        return self

    def print_notes(self):
        if not self.data:
            self.read_notes()
        result = "Film name | Note | Rating"
        for row in self.data:
            result += f'\n{row["film_name"]} | {row["note"]} | {row["rating"]}'
        print(result)

    def get_avg_rating(self) -> float:
        if not self.data:
            self.read_notes()
        working_data = [int(n['rating']) for n in self.data]
        return sum(working_data) / len(working_data)

