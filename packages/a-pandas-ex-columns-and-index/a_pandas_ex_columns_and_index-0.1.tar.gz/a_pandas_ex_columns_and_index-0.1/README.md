## Some useful Pandas methods for df.index and df.columns

```python
pip install a-pandas-ex-columns-and-index 
```

```python
from a_pandas_ex_columns_and_index import pd_add_index_and_columns
pd_add_index_and_columns()
import pandas as pd
df = pd.read_csv("https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_long.csv")
```

**The code above will add some new methods to you df**

- df.d_swap_2_columns 
- df.ds_sort_by_str_length 
- df.d_insert_column_before_another 
- df.ds_reverse 
- df.d_add_prefix_to_column_when_regex_match 
- df.d_add_prefix_to_index_when_regex_match 
- df.d_filter_df_by_regex_in_index 
- df.d_filter_df_by_regex_in_columns 
- df.d_columns_upper 
- df.d_index_upper 
- df.d_index_lower 
- df.d_columns_lower 
- df.d_make_columns_dot_compatible 
- df.d_natsort_index 
- df.d_natort_columns 
- df.d_natsort_df_by_column 

**All methods added to pandas have on of this prefixes:**

- **ds_** (for DataFrames and Series)

- **s_** (only for Series)

- **d_** (only for DataFrames)

### df.d_swap_2_columns

```python
df.columns
Out[3]: 
Index(['city', 'country', 'date.utc', 'location', 'parameter', 'value',
       'unit'],
      dtype='object')
print(df)
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df2=df.d_swap_2_columns('city', 'country')
print(df2.columns)
print(df2)
Index(['country', 'city', 'date.utc', 'location', 'parameter', 'value',
       'unit'],
      dtype='object')
     country       city                   date.utc  ... parameter value   unit
0         BE  Antwerpen  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1         BE  Antwerpen  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2         BE  Antwerpen  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3         BE  Antwerpen  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4         BE  Antwerpen  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
      ...        ...                        ...  ...       ...   ...    ...
5267      GB     London  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268      GB     London  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269      GB     London  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270      GB     London  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271      GB     London  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]

```

### df.ds_sort_by_str_length

```python
df
Out[3]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df2=df.ds_sort_by_str_length('city')
print(df2)
           city country                   date.utc  ... parameter value   unit
2635      Paris      FR  2019-05-15 05:00:00+00:00  ...       no2  46.5  µg/m³
2182      Paris      FR  2019-06-03 09:00:00+00:00  ...       no2  46.0  µg/m³
2183      Paris      FR  2019-06-03 08:00:00+00:00  ...       no2  43.9  µg/m³
2184      Paris      FR  2019-06-03 07:00:00+00:00  ...       no2  50.0  µg/m³
2185      Paris      FR  2019-06-03 06:00:00+00:00  ...       no2  44.1  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
3554  Antwerpen      BE  2019-05-19 15:00:00+00:00  ...       no2  33.0  µg/m³
3555  Antwerpen      BE  2019-05-19 14:00:00+00:00  ...       no2  23.0  µg/m³
3556  Antwerpen      BE  2019-05-19 13:00:00+00:00  ...       no2  14.5  µg/m³
3548  Antwerpen      BE  2019-05-19 21:00:00+00:00  ...       no2  12.5  µg/m³
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
[5272 rows x 7 columns]

```

### d_insert_column_before_another

```python
df
Out[6]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_insert_column_before_another(df.city + df.country, 'city_country', 'value')
Out[7]: 
           city country                   date.utc  ... city_country value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...  AntwerpenBE  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...  AntwerpenBE   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...  AntwerpenBE  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...  AntwerpenBE  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...  AntwerpenBE   7.5  µg/m³
         ...     ...                        ...  ...          ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...     LondonGB  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...     LondonGB  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...     LondonGB  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...     LondonGB  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...     LondonGB  67.0  µg/m³
[5272 rows x 8 columns]

```

### df.ds_reverse

```python
df
Out[3]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.ds_reverse()
Out[4]: 
           city country                   date.utc  ... parameter value   unit
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
[5272 rows x 7 columns]
```

### df.d_add_prefix_to_column_when_regex_match

```python
df
Out[8]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_add_prefix_to_column_when_regex_match(prefix='aa_', regular_expression='^c')
Out[9]: 
        aa_city aa_country                   date.utc  ... parameter value   unit
0     Antwerpen         BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen         BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen         BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen         BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen         BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...        ...                        ...  ...       ...   ...    ...
5267     London         GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London         GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London         GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London         GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London         GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
```

### df.d_add_prefix_to_index_when_regex_match

```python
Out[12]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_add_prefix_to_index_when_regex_match('five_', regular_expression='^5')
Out[13]: 
                city country                   date.utc  ... parameter value   unit
0          Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1          Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2          Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3          Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4          Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
              ...     ...                        ...  ...       ...   ...    ...
five_5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
five_5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
five_5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
five_5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
five_5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
```

### df.d_filter_df_by_regex_in_columns

```python
df
Out[14]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_filter_df_by_regex_in_columns('^[cu]')
Out[15]: 
           city country   unit
0     Antwerpen      BE  µg/m³
1     Antwerpen      BE  µg/m³
2     Antwerpen      BE  µg/m³
3     Antwerpen      BE  µg/m³
4     Antwerpen      BE  µg/m³
         ...     ...    ...
5267     London      GB  µg/m³
5268     London      GB  µg/m³
5269     London      GB  µg/m³
5270     London      GB  µg/m³
5271     London      GB  µg/m³
[5272 rows x 3 columns]
```

### df.d_filter_df_by_regex_in_index

```python
df
Out[16]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_filter_df_by_regex_in_index(r'^5\d\d0$')
Out[17]: 
        city country                   date.utc  ... parameter value   unit
5000  London      GB  2019-04-20 16:00:00+00:00  ...       no2  48.0  µg/m³
5010  London      GB  2019-04-20 06:00:00+00:00  ...       no2  33.0  µg/m³
5020  London      GB  2019-04-19 20:00:00+00:00  ...       no2  58.0  µg/m³
5030  London      GB  2019-04-19 10:00:00+00:00  ...       no2  44.0  µg/m³
5040  London      GB  2019-04-18 23:00:00+00:00  ...       no2  61.0  µg/m³
5050  London      GB  2019-04-18 13:00:00+00:00  ...       no2  49.0  µg/m³
5060  London      GB  2019-04-18 03:00:00+00:00  ...       no2  50.0  µg/m³
5070  London      GB  2019-04-17 17:00:00+00:00  ...       no2  54.0  µg/m³
5080  London      GB  2019-04-17 07:00:00+00:00  ...       no2  51.0  µg/m³
5090  London      GB  2019-04-16 20:00:00+00:00  ...       no2  83.0  µg/m³
5100  London      GB  2019-04-16 09:00:00+00:00  ...       no2  66.0  µg/m³
5110  London      GB  2019-04-15 22:00:00+00:00  ...       no2  47.0  µg/m³
5120  London      GB  2019-04-15 12:00:00+00:00  ...       no2  27.0  µg/m³
5130  London      GB  2019-04-15 02:00:00+00:00  ...       no2  32.0  µg/m³
5140  London      GB  2019-04-14 16:00:00+00:00  ...       no2  23.0  µg/m³
5150  London      GB  2019-04-14 06:00:00+00:00  ...       no2  35.0  µg/m³
5160  London      GB  2019-04-13 20:00:00+00:00  ...       no2  29.0  µg/m³
5170  London      GB  2019-04-13 10:00:00+00:00  ...       no2  45.0  µg/m³
5180  London      GB  2019-04-13 00:00:00+00:00  ...       no2  29.0  µg/m³
5190  London      GB  2019-04-12 14:00:00+00:00  ...       no2  39.0  µg/m³
5200  London      GB  2019-04-12 04:00:00+00:00  ...       no2  33.0  µg/m³
5210  London      GB  2019-04-11 16:00:00+00:00  ...       no2  34.0  µg/m³
5220  London      GB  2019-04-11 06:00:00+00:00  ...       no2  46.0  µg/m³
5230  London      GB  2019-04-10 19:00:00+00:00  ...       no2  35.0  µg/m³
5240  London      GB  2019-04-10 09:00:00+00:00  ...       no2  35.0  µg/m³
5250  London      GB  2019-04-09 23:00:00+00:00  ...       no2  38.0  µg/m³
5260  London      GB  2019-04-09 13:00:00+00:00  ...       no2  56.0  µg/m³
5270  London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
[28 rows x 7 columns]
```

### df.d_columns_upper, df.d_columns_lower,df.d_make_columns_dot_compatible,df.d_index_upper,df.d_index_lower

```python
print(df.columns)
print(df.d_make_columns_dot_compatible().columns)
print(df.d_columns_upper().columns)
print(df.d_columns_lower().columns)
df2=df.copy()
df2.index = df2.parameter
print(df2.index)
print(df2.d_index_upper().index)
print(df2.d_index_lower().index)
Index(['city', 'country', 'date.utc', 'location', 'parameter', 'value',
       'unit'],
      dtype='object')
Index(['city', 'country', 'date_utc', 'location', 'parameter', 'value',
       'unit'],
      dtype='object')
Index(['CITY', 'COUNTRY', 'DATE_UTC', 'LOCATION', 'PARAMETER', 'VALUE',
       'UNIT'],
      dtype='object')
Index(['city', 'country', 'date_utc', 'location', 'parameter', 'value',
       'unit'],
      dtype='object')
Index(['pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25',
       'pm25',
       ...
       'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2'],
      dtype='object', name='parameter', length=5272)
Index(['PM25', 'PM25', 'PM25', 'PM25', 'PM25', 'PM25', 'PM25', 'PM25', 'PM25',
       'PM25',
       ...
       'NO2', 'NO2', 'NO2', 'NO2', 'NO2', 'NO2', 'NO2', 'NO2', 'NO2', 'NO2'],
      dtype='object', length=5272)
Index(['pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25', 'pm25',
       'pm25',
       ...
       'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2', 'no2'],
      dtype='object', length=5272)

```

### df.d_natsort_index

```python
df2 = df.sample(len(df)).copy()
dftempindex = df2.index[:2500].to_list()
tempvalue = df2.loc[dftempindex].parameter.copy()
tempvalue = tempvalue.apply(lambda x: str(x).upper())
df2.loc[dftempindex, 'parameter'] = tempvalue
print(df2)
df2.index = df2.parameter
print(df2.d_natsort_index())
for a,b,c,d in zip(df2.d_natsort_index(sort_numbers_after_non_numbers=True).index.to_list(), df2.d_natsort_index(lowercase_first=True).index.to_list(),df2.d_natsort_index(group_lower_and_uppercase=True).index.to_list(),df2.d_natsort_index(uppercase_first=True).index.to_list()):
    print(a,b,c,d)

no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 no2 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
no2 NO2 PM25 no2
```

### df.d_natsort_df_by_column

```python
df
Out[3]: 
           city country                   date.utc  ... parameter value   unit
0     Antwerpen      BE  2019-06-18 06:00:00+00:00  ...      pm25  18.0  µg/m³
1     Antwerpen      BE  2019-06-17 08:00:00+00:00  ...      pm25   6.5  µg/m³
2     Antwerpen      BE  2019-06-17 07:00:00+00:00  ...      pm25  18.5  µg/m³
3     Antwerpen      BE  2019-06-17 06:00:00+00:00  ...      pm25  16.0  µg/m³
4     Antwerpen      BE  2019-06-17 05:00:00+00:00  ...      pm25   7.5  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
5267     London      GB  2019-04-09 06:00:00+00:00  ...       no2  41.0  µg/m³
5268     London      GB  2019-04-09 05:00:00+00:00  ...       no2  41.0  µg/m³
5269     London      GB  2019-04-09 04:00:00+00:00  ...       no2  41.0  µg/m³
5270     London      GB  2019-04-09 03:00:00+00:00  ...       no2  67.0  µg/m³
5271     London      GB  2019-04-09 02:00:00+00:00  ...       no2  67.0  µg/m³
[5272 rows x 7 columns]
df.d_natsort_df_by_column('date.utc')
Out[4]: 
           city country                   date.utc  ... parameter value   unit
176   Antwerpen      BE  2019-04-09 01:00:00+00:00  ...      pm25  76.0  µg/m³
3500      Paris      FR  2019-04-09 01:00:00+00:00  ...       no2  24.4  µg/m³
3663  Antwerpen      BE  2019-04-09 01:00:00+00:00  ...       no2  22.5  µg/m³
175   Antwerpen      BE  2019-04-09 02:00:00+00:00  ...      pm25  91.5  µg/m³
1824     London      GB  2019-04-09 02:00:00+00:00  ...      pm25  42.0  µg/m³
         ...     ...                        ...  ...       ...   ...    ...
1827      Paris      FR  2019-06-20 22:00:00+00:00  ...       no2  26.5  µg/m³
178      London      GB  2019-06-20 23:00:00+00:00  ...      pm25   7.0  µg/m³
1826      Paris      FR  2019-06-20 23:00:00+00:00  ...       no2  21.8  µg/m³
177      London      GB  2019-06-21 00:00:00+00:00  ...      pm25   7.0  µg/m³
1825      Paris      FR  2019-06-21 00:00:00+00:00  ...       no2  20.0  µg/m³
[5272 rows x 7 columns]
```
