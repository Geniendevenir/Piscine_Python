import sys

kata = (9, 9, 25, 3, 30)

def write_date(kata):
    year, month, day, hour, minute = kata
    print(f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}")

write_date(kata)