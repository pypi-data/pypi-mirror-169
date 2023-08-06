# PySpinners

## CLI Progress Spinner collection

PySpinners is a collection of progress spinners for CLI applications.


### Installation
```sh
pip install pyspinners
```

### Usage
```sh
# Create new spinner instance
# Options 1-30 for different spinner type
# True/False shows both progress and spinner or just the spinner
spinner1 = NewSpinner(1, False)

# Any list or any other iterable can be used
lst = [1, 2, 3, 4, 5]

for i, item in enumerate(lst):
    ...do stuff...
    spinner1.spin(i+1, len(lst))
    # Call the .spin() function and give as parameters the iteration number and the length of the iterable.
```

### License

MIT
