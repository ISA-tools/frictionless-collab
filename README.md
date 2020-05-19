# frictionless-collab

Frictionless JSON Data Packages for Life Science

## Table layouts

Here is a demo how `dataflows`:

- converts a wide table to a long table
- converts a long table to a wide table
- generates automatically a package descriptor in both cases

```
$ make install
$ python3 layouts/wide.py
$ python3 layouts/long.py
```


## Gene expression data examples

- **GSE60450_Lactation-GenewiseCounts.csv**: gene expression matrix with simple layout, with the first 2 fields being molecular entity descriptors, the remainder of the fields correspond to `read counts` per `samples`. [GSE60450](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60450)

- **P1-SARS-CoV2_Virus_FPKM.csv**: gene expression matrix with simple layout, with the first field being molecular entity identifier, the remaineder of the fields correspond to `FPKM measure` per `sample` (file produced during the Elixir BioHackathon on COVID19).

- **GSE52778_All_Sample_FPKM_Matrix.csv** : gene expression matrix of more complex structure, with the first 9 fields (columns[A-I]) being molecular entity descriptors, then 4 sets of 3 fields, matching the 4 experimental conditions and 3 quantitation types  (including FPKM measures) (columns[J-Y], then individual experimental conditions (per cell line) column[Z-AO], from NCBI GEO experiment [GSE52778](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52778)


## Feature Requests to Transformation:

- [x] allow 'flatening of multi row headers' as documented by @lilwinfree

```bash
!pip install tabulator
```

then:

```python
from tabulator import Stream

with Stream('oxford.csv', headers=[1,2], multiline_headers_joiner='.') as stream:
  print(stream.headers)

  ['Gene Name', 'Sample_id1.mean', 'Sample_id1.standard dev', 'Sample_id2.mean', 'Sample_id2.standard dev']
```


- [ ] pivot/unpivot operation: expand on existing code provided by @roll to enable an offset parameter (fixing the number of field associated with `molecular entity` descriptors) and 2 additional parameters, one to obtain the number of experimental conditions or unique samples, and another one, lising the number of quantitation types)

	:important: possibly agree on a `conventional separator` to detect `flattened headers` as in `Sample_id1.standard dev`. Separator could be selected from [".","|","__"]
