## Generating Time Series with TransientX

To generate time series data, the [TransientX](https://github.com/ypmen/TransientX) program should be used with the following options:

- `--savetim`: Saves the time series data.
- `--format presto`: Specifies the output format as compatible with PRESTO.

### Example Command:

```bash
transientx_fil -v -o $NAME -t 16 --fd 1 --overlap 0.1 --ddplan $DMFILE -l 1.0 --drop --savetim --format presto -f $FILE
```
