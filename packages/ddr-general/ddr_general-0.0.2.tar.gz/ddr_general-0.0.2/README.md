# ddr_general

Contains basic functionalities used freqeuntly.

```py
import ddr_general
```

### make directory

```py
ddr_general.make_dir(r'C:/user/fold1')
```

makes *fold1* directory in *user* directory. If directory already exists then funtion does nothing.

## get folder information

```py
ddr_general.get_dir_path(r'C:/user/fold1')
```

returns the list of paths of all folders (only) within *fold1* directory.

```py
ddr_general.get_dir_name(r'C:/user/fold1')
```

returns the  list of names of all folders (only) within *fold1* directory.

```py
ddr_general.get_file_path(r'C:/user/fold1')
```

returns the list of paths of all files (only) within *fold1* directory.

```py
ddr_general.get_file_name(r'C:/user/fold1')
```

returns the list of names of all files (only) within *fold1* directory.

