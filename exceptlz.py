import pandas as pd


class Checkup:
    def __init__(self, input_file_path):
        # Попытка загрузить входной CSV-файл
        try:
            self.input_df = pd.read_csv(input_file_path)
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка: Датафрейм пуст')
            raise SystemExit()
        except FileNotFoundError:
            print(f'Возникла следующая ошибка: [Errno 2] No such file or directory: "{input_file_path}"')
            raise SystemExit()

        # Попытка загрузить эталонный датафрейм и сравнить названия столбцов
        try:
            self.reference_df = pd.read_csv('var8.csv')
            input_columns = self.input_df.columns.to_list()
            reference_columns = self.reference_df.columns.to_list()
            if input_columns != reference_columns:
                raise TypeError
        except TypeError:
            print(f'Структура датафрейма НЕ соответствует ожидаемой:\n'
                  f'Название столбцов не совпадают.\n'
                  f'Ожидаемые: {reference_columns}\nФактические: {input_columns}')

        # Сравнение строковых представлений датафреймов
        try:
            self.input_df_str = str(self.input_df)
            self.reference_df_str = str(self.reference_df)
            if self.input_df_str != self.reference_df_str:
                raise TypeError('Ошибка при проверке типов данных')
            else:
                print('Чтение датафрейма завершено успешно')
        except TypeError:
            print(f'Тип данных не соответствует ожидаемому.\n'
                  f'Ожидаемые:\n{self.reference_df_str}\n'
                  f'Фактические:\n{self.input_df_str}')


def main():
    input_file_path = 'var8 bad.csv'
    checkup = Checkup(input_file_path)


if __name__ == "__main__":
    main()
