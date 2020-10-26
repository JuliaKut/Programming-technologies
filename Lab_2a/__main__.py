import argparse
from modules import common
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()
parser = argparse.ArgumentParser(description='Приклад передачі аргументів у Python програму.')
parser.add_argument('-o', '--optional', dest='opt', type=str, help='Цей параметр є вибірковим.')
parser.add_argument('-l', '--logs', dest='logs', action='store_true',
                    help='Якщо виконати команду з цим параметром будуть виводитись логи.')


def main(text):
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    print(common.get_current_platform())
    if text:
        print("З консолі було передано аргумент\n", 10*"=", f">> {text} <<", 10*"=")


def how_to_write_logs():
    logger.info("Тут буде просто інформативне повідомлення")
    logger.warning("Це Warning повідомлення")
    logger.error("Це повідомлення про помилку")


def func2():
    keys= {"a":1,"b":2,"c":3,"d":4}
    try:
        value =keys['e']
    except KeyError:
        logger.error("даного ключа не існує")
    else:
        logger.info("ось ваш ключ")
    finally:
        print("результат")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.logs:
        how_to_write_logs()
    else:
        main(args.opt)
    print("Вивід моєї функції\n")
    common.func(False)
    print("\n------------------------------------------------------")
    print("Вивід моєї другої функції\n")
    func2()
