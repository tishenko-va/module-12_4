from unittest import TestCase
import runner
import logging
import runner_new


logging.basicConfig(
        filename='runner_tests.log',
        filemode='w',
        level=logging.INFO,
        encoding='utf-8',
        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(TestCase):


    def test_walk(self):
        try:
            runner1 = runner_new.Runner('name', -5)
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner")


    def test_run(self):
        try:
            runner2 = runner_new.Runner(7, 7)
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner")

    def test_challenge(self):
        runner1 = runner_new.Runner('runner1')
        runner2 = runner_new.Runner('runner2')
        try:
            for i in range(10):
                runner1.walk()
                runner1.run()
                runner2.walk()
                runner2.run()
            self.assertEqual(runner1.distance, runner2.distance)
        except:
            logging.warning('f Неверный тип данных')




if __name__ == '__main__':

    unittest.main()

