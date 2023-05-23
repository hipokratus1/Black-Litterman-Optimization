import portfolio
from src import utils


@utils.print_time
def run_with_timer():
    portfolio.run()

if __name__ == '__main__':
    run_with_timer()