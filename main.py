"""
Demo program for fetching trains info
"""

import asyncio
import datetime
from aiorzd import RzdFetcher, TimeRange


async def main():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    fetcher = RzdFetcher()
    trains = await fetcher.trains(
        'МОСКВА',
        'САНКТ-ПЕТЕРБУРГ',
        TimeRange(
            datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day,
                              20, 0),
            datetime.datetime(after_tomorrow.year, after_tomorrow.month,
                              after_tomorrow.day, 4, 0),
        )
    )
    for train in trains:
        print(train)

    trains = RzdFetcher.filter_trains(trains, ['Плацкартный', 'Купе'])
    for train in filter(
            lambda t: any(s for s in t.seats.values() if s.price < 2000),
            trains,
    ):
        print(train)
    await fetcher.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
