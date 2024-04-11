import logging
import sys
import traceback

logging.basicConfig(
    handlers=[logging.FileHandler(filename='error.log', encoding='utf-8')],
    format='%(asctime)s; %(levelname)-8s; %(message)s',
    level=logging.INFO,
)

TEST_DATA = [
    [2, 'str', True],
    [5, 4, 'str', 'str'],
    [6, 4, 5, 10],
]


def sum_variables(list_variable) -> int:
    '''Возвращает сумму переменных.'''
    try:
        return sum(list_variable)
    except Exception as error:
        _, _, exc_tb = sys.exc_info()
        logging.error(
            f'Ошибка на строке: {traceback.extract_tb(exc_tb)[-1].lineno}; '
            f'Тип: {[type(variable) for variable in list_variable]}; '
            f'Значение переменных: {list_variable}; '
            f'Сообщение: {error}.',
        )


if __name__ == '__main__':
    [sum_variables(list_variable) for list_variable in TEST_DATA]
