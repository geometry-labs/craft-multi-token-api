from threading import Thread
from time import sleep
from confluent_kafka import Consumer

from kafkaworker.settings import settings
from kafkaworker.workers import logs_etl_worker

def test_logs_etl_worker() -> None:
    thread = Thread(
        target=logs_etl_worker,
        args=(),
    )
    thread.daemon = True
    thread.start()

    # Let worker work
    sleep(10)

    assert thread.is_alive()

