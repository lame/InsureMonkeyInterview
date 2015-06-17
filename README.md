# Insure Monkey Preliminary Interview Coding Exercise

##Flatten:

1. print flatten([['a', 'b'], ['c', ['d', 'e',], ['f'], 'g']])
    1. ['a', 'b', 'c', 'd', 'e', 'f', 'g']
2. print flatten([['a', 'b'], 'a', ['a', 'b',], ['a'], 'b'])
    1. ['a', 'b', 'a', 'a', 'b', 'a', 'b'i]

##Comma separated values
```python
assert comma_separated_numbers(3456) == '3,456'
assert comma_separated_numbers(987654321) == '987,654,321'
assert comma_separated_numbers(12) == '12'
assert comma_separated_numbers(12.3) == '12.3'
assert comma_separated_numbers(3456.3) == '3,456.3'
```

##Get Next Dates

**Return a list of dates based on the following rules**

1. **count**: number of dates to return
2. **month offset**: how many months to move ahead from base_date
3. **day cutoff**: day of the month to roll over to the next month positive number means on that day of month, roll over negative number means on that number of days from the end of the month, roll over 0 means rolling over on the last day of the month
*day_cutoff must be taken into account before the month month_offset*
*after rolling over to another month after base_date.month, all dates must be first of month.*

```python
print get_next_dates(date(2014, 5, 1), 2, 1, 0)
*[date(2014, 6, 1), date(2014, 7, 1)]*
print get_next_dates(date(2014, 5, 2), 3, 0, 3)
*[date(2014, 5, 2), date(2014, 6, 1), date(2014, 7, 1)]*
print get_next_dates(date(2014, 5, 10), 3, 0, 3)
*[date(2014, 6, 1), date(2014, 7, 1), date(2014, 8, 1)]*
print get_next_dates(date(2014, 5, 30), 3, 1, -3)
*[date(2014, 7, 1), date(2014, 8, 1), date(2014, 9, 1)]*
```
##Django boilerplate

- Write a basic set of model(s), form(s), and view(s) to handle saving multiple addresses to a user using Django ORM and class based views
