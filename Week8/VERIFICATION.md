# Lab 9 verification

The commands below were run from the repository root. The test container used the Python 3.11 image built from the Week8 Dockerfile.

```text
> git log -1 --oneline
2bfcc18 feat: implement Lab 9 inventory patterns and validation

> docker build -t inf1103-lab9 ./Week8
#10 naming to docker.io/library/inf1103-lab9:latest done

> docker run --rm inf1103-lab9 python -m unittest discover -s tests -v
Ran 14 tests in 0.007s
OK

> @('7','1','6') | docker run --rm -i inf1103-lab9
Row 4 skipped: Unknown product type: service
Row 5 skipped: could not convert string to float: 'abc'
3 products loaded.
Load attempt finished.
ID: P001 | Name: Desk Lamp | Price: $25.00 | Stock: 10
ID: D001 | Name: Photo Editor | Price: $49.90 | Stock: 100
ID: P003 | Name: Monitor Stand | Price: $39.50 | Stock: 7
Inventory saved.
```

The Git entry reflects the current implementation commit. The Docker output is excerpted from the successful runs. The terminal screenshots are in [screenshots](screenshots/). The Git screenshot shows the two Lab 9 commits before the report and screenshots were added.
