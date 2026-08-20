def get_period_number(seconds):

    now = datetime.now()

    date_part = now.strftime("%Y%m%d")

    midnight = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )

    elapsed_seconds = int(
        (now - midnight).total_seconds()
    )

    # One period ahead
    round_number = (
        (elapsed_seconds // seconds) + 1
    )

    last_five = round_number % 100000

    last_five_text = str(
        last_five
    ).zfill(5)

    period_number = (
        date_part
        + "1000"
        + last_five_text
    )

    return period_number
